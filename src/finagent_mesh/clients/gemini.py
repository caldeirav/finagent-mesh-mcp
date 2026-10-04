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
            from langchain_google_genai import ChatGoogleGenerativeAI

            llm = ChatGoogleGenerativeAI(model=self.model, google_api_key=self.api_key)
            result = llm.invoke(prompt)
        except Exception as exc:  # noqa: BLE001
            raise GeminiError(f"Gemini API error ({self.model}): {exc}") from exc

        content = getattr(result, "content", str(result))
        if isinstance(content, list):
            content = " ".join(str(part) for part in content)
        text = str(content)
        self.last_answer = text
        return text
