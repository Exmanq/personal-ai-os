from __future__ import annotations

import uuid
from datetime import UTC, datetime

from personal_ai_os.core.storage import Storage


def add_note(storage: Storage, text: str, tags: list[str] | None = None) -> dict[str, str]:
    record = {
        "id": str(uuid.uuid4()),
        "text": text,
        "tags": tags or [],
        "created_at": datetime.now(tz=UTC).isoformat(),
    }
    return storage.append("notes", record)


def search_notes(storage: Storage, query: str) -> list[dict[str, str]]:
    query_lower = query.lower()
    return [note for note in storage.load("notes") if query_lower in note["text"].lower()]
