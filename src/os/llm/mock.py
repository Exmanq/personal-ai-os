from __future__ import annotations

from collections.abc import Iterable


class MockLLM:
    """Deterministic mock for offline summaries."""

    def summarize(self, texts: Iterable[str]) -> str:
        snippets: list[str] = []
        for text in texts:
            clean = text.strip().replace("\n", " ")
            if clean:
                snippets.append(clean[:80])
        if not snippets:
            return "No notes yet — set a goal and add your first note."
        joined = "; ".join(snippets)
        return f"Daily recap: {joined}. Action: pick one task to advance a goal."
