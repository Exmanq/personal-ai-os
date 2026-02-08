from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

DEFAULT_DATA_DIR = Path(os.getenv("PAIOS_DATA_DIR", "data/demo")).resolve()


@dataclass
class Settings:
    data_dir: Path = DEFAULT_DATA_DIR
    verbose: bool = False

    @classmethod
    def from_env(cls) -> Settings:
        data_dir = Path(os.getenv("PAIOS_DATA_DIR", DEFAULT_DATA_DIR))
        verbose = os.getenv("PAIOS_VERBOSE", "false").lower() in {"1", "true", "yes"}
        return cls(data_dir=data_dir, verbose=verbose)

    def ensure(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
