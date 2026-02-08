from __future__ import annotations

from personal_ai_os.core.storage import Storage


def add_knowledge(storage: Storage, question: str, answer: str) -> dict[str, str]:
    record = {"question": question, "answer": answer}
    return storage.append("knowledge", record)


def search_knowledge(storage: Storage, query: str) -> list[dict[str, str]]:
    query_lower = query.lower()
    return [item for item in storage.load("knowledge") if query_lower in item["question"].lower()]
