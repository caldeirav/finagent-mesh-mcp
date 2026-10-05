"""Gemini System-2 synthesis via langchain-google-genai (fail-closed)."""

from __future__ import annotations


class GeminiError(RuntimeError):
    """Raised when Gemini credentials or API calls fail — never fabricate answers."""


class GeminiClient:
    def __init__(self, api_key: str | None, model: str) -> None:
        self.api_key = api_key
        self.model = model
        self.last_prompt: str | None = None
        self.last_answer: str | None = None

    def synthesize(self, query: str, chunks: list[tuple[str, str]]) -> str:
        """Synthesize an answer from (chunk_id, text) pairs. Fail closed — no extractive fallback."""
        if not self.api_key:
            raise GeminiError(
                "GOOGLE_API_KEY missing; refuse extractive/local fabrication (fail closed)"
            )

        context = "\n\n".join(f"[{cid}]\n{text}" for cid, text in chunks)
        prompt = (
            "You are a financial research assistant. Answer the question using ONLY "
            "the provided retrieved passages. If insufficient, say you cannot determine.\n\n"
            f"Question: {query}\n\nPassages:\n{context}\n\nAnswer:"
        )
        self.last_prompt = prompt
        self.last_answer = None

        try:
            import mlflow
            from mlflow.entities import SpanType

            span_cm = mlflow.start_span(
                name="gemini_synthesize",
                span_type=SpanType.LLM,
                attributes={
                    "gemini_model": self.model,
                    "n_chunks": len(chunks),
                },
            )
        except Exception:  # noqa: BLE001
            span_cm = None

        def _invoke() -> str:
            try:
                from langchain_google_genai import ChatGoogleGenerativeAI

                llm = ChatGoogleGenerativeAI(model=self.model, google_api_key=self.api_key)
                result = llm.invoke(prompt)
            except Exception as exc:  # noqa: BLE001
                raise GeminiError(f"Gemini API error ({self.model}): {exc}") from exc

            content = getattr(result, "content", str(result))
            if isinstance(content, list):
                content = " ".join(str(part) for part in content)
            return str(content)

        if span_cm is None:
            text = _invoke()
            self.last_answer = text
            return text

        with span_cm as span:
            span.set_inputs(
                {
                    "query": query,
                    "n_chunks": len(chunks),
                    "chunk_ids": [cid for cid, _ in chunks[:20]],
                    "model": self.model,
                }
            )
            try:
                text = _invoke()
                self.last_answer = text
                span.set_outputs(
                    {
                        "answer_chars": len(text),
                        "answer_preview": text[:500],
                    }
                )
                return text
            except Exception as exc:
                span.set_attributes({"error": str(exc)[:500]})
                raise
