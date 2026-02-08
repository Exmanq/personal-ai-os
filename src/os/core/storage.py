from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from personal_ai_os.core.config import Settings


class Storage:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.settings.ensure()

    def _path(self, name: str) -> Path:
        return self.settings.data_dir / f"{name}.json"

    def load(self, name: str) -> list[dict[str, Any]]:
        path = self._path(name)
        if not path.exists():
            return []
        return json.loads(path.read_text(encoding="utf-8"))

    def save(self, name: str, items: list[dict[str, Any]]) -> None:
        path = self._path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

    def append(self, name: str, item: dict[str, Any]) -> dict[str, Any]:
        items = self.load(name)
        items.append(item)
        self.save(name, items)
        return item
