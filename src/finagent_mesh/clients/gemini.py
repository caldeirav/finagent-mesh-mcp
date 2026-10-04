"""Gemini System-2 synthesis via langchain-google-genai."""

from __future__ import annotations


class GeminiClient:
    def __init__(self, api_key: str | None, model: str) -> None:
        self.api_key = api_key
        self.model = model

    def synthesize(self, query: str, chunks: list[tuple[str, str]]) -> str:
        """Synthesize an answer from (chunk_id, text) pairs."""
        context = "\n\n".join(f"[{cid}]\n{text}" for cid, text in chunks)
        prompt = (
            "You are a financial research assistant. Answer the question using ONLY "
            "the provided retrieved passages. If insufficient, say you cannot determine.\n\n"
            f"Question: {query}\n\nPassages:\n{context}\n\nAnswer:"
        )
        if not self.api_key:
            # Offline/dev fallback: extractive concatenation of top chunk heads.
            heads = [text.strip().split("\n")[0][:240] for _, text in chunks[:3]]
            return " ".join(heads) if heads else "Unable to synthesize without credentials."

        from langchain_google_genai import ChatGoogleGenerativeAI

        llm = ChatGoogleGenerativeAI(model=self.model, google_api_key=self.api_key)
        result = llm.invoke(prompt)
        content = getattr(result, "content", str(result))
        if isinstance(content, list):
            return " ".join(str(part) for part in content)
        return str(content)
