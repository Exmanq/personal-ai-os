from __future__ import annotations

import uuid
from datetime import UTC, datetime

from personal_ai_os.core.storage import Storage


def set_goal(
    storage: Storage, title: str, deadline: str | None = None, kpi: str | None = None
) -> dict[str, str]:
    goal = {
        "id": str(uuid.uuid4()),
        "title": title,
        "deadline": deadline,
        "kpi": kpi or "",
        "status": "planned",
        "created_at": datetime.now(tz=UTC).isoformat(),
    }
    return storage.append("goals", goal)


def goals_summary(storage: Storage) -> list[dict[str, str]]:
    return storage.load("goals")
