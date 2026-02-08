from __future__ import annotations

import uuid
from datetime import date, timedelta

from personal_ai_os.core.storage import Storage


def add_task(
    storage: Storage, title: str, due: str, related_goal: str | None = None
) -> dict[str, str]:
    task = {
        "id": str(uuid.uuid4()),
        "title": title,
        "due": due,
        "status": "planned",
        "related_goal": related_goal or "",
    }
    return storage.append("tasks", task)


def plan_week(storage: Storage) -> list[dict[str, str]]:
    today = date.today()
    goals = storage.load("goals")
    planned_tasks: list[dict[str, str]] = []
    for idx, goal in enumerate(goals[:5]):
        due = today + timedelta(days=idx)
        planned_tasks.append(
            add_task(
                storage,
                title=f"Progress for goal: {goal['title']}",
                due=due.isoformat(),
                related_goal=goal["id"],
            )
        )
    if not planned_tasks:
        planned_tasks.append(
            add_task(storage, title="Review and prioritize goals", due=today.isoformat())
        )
    return planned_tasks


def list_tasks(storage: Storage) -> list[dict[str, str]]:
    return storage.load("tasks")
