from __future__ import annotations

import json
from pathlib import Path

import pytest
from personal_ai_os.cli import app
from personal_ai_os.core.config import Settings
from personal_ai_os.core.storage import Storage
from personal_ai_os.llm.mock import MockLLM
from personal_ai_os.modules.goals import goals_summary, set_goal
from personal_ai_os.modules.knowledge import add_knowledge, search_knowledge
from personal_ai_os.modules.memory import add_note, search_notes
from personal_ai_os.modules.reflection import daily_reflect
from personal_ai_os.modules.tasks import list_tasks, plan_week
from typer.testing import CliRunner


@pytest.fixture()
def tmp_storage(tmp_path: Path) -> Storage:
    settings = Settings(data_dir=tmp_path)
    return Storage(settings)


def test_add_note_and_search(tmp_storage: Storage) -> None:
    add_note(tmp_storage, "test note about focus", tags=["focus"])
    results = search_notes(tmp_storage, "focus")
    assert len(results) == 1
    assert results[0]["tags"] == ["focus"]


def test_set_goal(tmp_storage: Storage) -> None:
    goal = set_goal(tmp_storage, "Ship", deadline="2026-02-15")
    assert goal["deadline"] == "2026-02-15"
    assert goals_summary(tmp_storage)[0]["title"] == "Ship"


def test_plan_week_with_goal(tmp_storage: Storage) -> None:
    set_goal(tmp_storage, "Learn", deadline="2026-02-20")
    tasks = plan_week(tmp_storage)
    assert tasks
    assert list_tasks(tmp_storage)


def test_plan_week_without_goal(tmp_storage: Storage) -> None:
    tasks = plan_week(tmp_storage)
    assert tasks[0]["title"].startswith("Review and prioritize")


def test_daily_reflect(tmp_storage: Storage) -> None:
    add_note(tmp_storage, "Wrapped up design")
    reflection = daily_reflect(tmp_storage)
    assert "Daily recap" in reflection["summary"]


def test_mock_llm_empty() -> None:
    llm = MockLLM()
    assert "No notes" in llm.summarize([])


def test_knowledge_search(tmp_storage: Storage) -> None:
    add_knowledge(tmp_storage, "What", "Answer")
    results = search_knowledge(tmp_storage, "what")
    assert results[0]["answer"] == "Answer"


def test_cli_add_note(tmp_path: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["add-note", "cli note", "--data-dir", str(tmp_path)])
    assert result.exit_code == 0
    data = json.loads(Path(tmp_path / "notes.json").read_text())
    assert data[0]["text"] == "cli note"


def test_cli_plan_week_output(tmp_path: Path) -> None:
    runner = CliRunner()
    runner.invoke(app, ["set-goal", "CLI Goal", "--data-dir", str(tmp_path)])
    result = runner.invoke(app, ["plan-week", "--data-dir", str(tmp_path)])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert isinstance(payload, list)
    assert payload


def test_cli_daily_reflect_output(tmp_path: Path) -> None:
    runner = CliRunner()
    runner.invoke(app, ["add-note", "Reflectable note", "--data-dir", str(tmp_path)])
    result = runner.invoke(app, ["daily-reflect", "--data-dir", str(tmp_path)])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert payload["note_count"] >= 1


def test_doctor_output(tmp_path: Path) -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["doctor", "--data-dir", str(tmp_path)])
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert payload["data_dir_exists"] is True
