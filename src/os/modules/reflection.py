from __future__ import annotations

from datetime import date

from personal_ai_os.core.storage import Storage
from personal_ai_os.llm.mock import MockLLM


def daily_reflect(storage: Storage, notes: list[dict[str, str]] | None = None) -> dict[str, str]:
    notes = notes or storage.load("notes")
    llm = MockLLM()
    summary = llm.summarize([note["text"] for note in notes])
    entry = {
        "date": date.today().isoformat(),
        "summary": summary,
        "note_count": len(notes),
    }
    storage.append("reflections", entry)
    return entry
