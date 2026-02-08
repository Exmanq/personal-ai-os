from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import typer
from personal_ai_os.core.config import Settings
from personal_ai_os.core.logger import get_console, get_logger
from personal_ai_os.core.storage import Storage
from personal_ai_os.modules.goals import set_goal
from personal_ai_os.modules.knowledge import add_knowledge, search_knowledge
from personal_ai_os.modules.memory import add_note
from personal_ai_os.modules.reflection import daily_reflect
from personal_ai_os.modules.tasks import plan_week

app = typer.Typer(help="Personal AI OS CLI")


def _storage(verbose: bool = False, data_dir: Path | None = None) -> Storage:
    settings = Settings.from_env()
    if data_dir:
        settings.data_dir = data_dir
    settings.verbose = verbose
    logger = get_logger(settings.verbose)
    logger.debug("Using data dir %s", settings.data_dir)
    return Storage(settings)


@app.command("add-note")
def add_note_cli(
    text: str = typer.Argument(..., help="Note text"),
    tags: str = typer.Option("", help="Comma-separated tags"),
    data_dir: Path | None = typer.Option(None, help="Override data directory"),
    verbose: bool = typer.Option(False, help="Verbose output"),
) -> None:
    storage = _storage(verbose=verbose, data_dir=data_dir)
    note = add_note(storage, text=text, tags=[t for t in tags.split(",") if t])
    typer.echo(json.dumps(note, ensure_ascii=False, indent=2))


@app.command("set-goal")
def set_goal_cli(
    title: str = typer.Argument(..., help="Goal title"),
    deadline: str = typer.Option("", help="Deadline (YYYY-MM-DD)"),
    kpi: str = typer.Option("", help="KPI for the goal"),
    data_dir: Path | None = typer.Option(None, help="Override data directory"),
    verbose: bool = typer.Option(False, help="Verbose output"),
) -> None:
    storage = _storage(verbose=verbose, data_dir=data_dir)
    goal = set_goal(storage, title=title, deadline=deadline or None, kpi=kpi or None)
    typer.echo(json.dumps(goal, ensure_ascii=False, indent=2))


@app.command("plan-week")
def plan_week_cli(
    data_dir: Path | None = typer.Option(None, help="Override data directory"),
    verbose: bool = typer.Option(False, help="Verbose output"),
) -> None:
    storage = _storage(verbose=verbose, data_dir=data_dir)
    tasks = plan_week(storage)
    typer.echo(json.dumps(tasks, ensure_ascii=False, indent=2))


@app.command("daily-reflect")
def daily_reflect_cli(
    data_dir: Path | None = typer.Option(None, help="Override data directory"),
    verbose: bool = typer.Option(False, help="Verbose output"),
) -> None:
    storage = _storage(verbose=verbose, data_dir=data_dir)
    reflection = daily_reflect(storage)
    typer.echo(json.dumps(reflection, ensure_ascii=False, indent=2))


@app.command("knowledge-add")
def knowledge_add(
    question: str,
    answer: str,
    data_dir: Path | None = typer.Option(None, help="Override data directory"),
    verbose: bool = typer.Option(False, help="Verbose output"),
) -> None:
    storage = _storage(verbose=verbose, data_dir=data_dir)
    typer.echo(json.dumps(add_knowledge(storage, question=question, answer=answer), indent=2))


@app.command("knowledge-search")
def knowledge_search(
    query: str,
    data_dir: Path | None = typer.Option(None, help="Override data directory"),
    verbose: bool = typer.Option(False, help="Verbose output"),
) -> None:
    storage = _storage(verbose=verbose, data_dir=data_dir)
    results = search_knowledge(storage, query=query)
    console = get_console()
    if results:
        console.print_json(data=results)
    else:
        typer.echo("No results.")


@app.command("doctor")
def doctor(
    data_dir: Path | None = typer.Option(None, help="Override data directory"),
) -> None:
    settings = Settings.from_env()
    if data_dir:
        settings.data_dir = data_dir
    checks = {
        "python": True,
        "data_dir_exists": settings.data_dir.exists(),
        "env": {"PAIOS_DATA_DIR": str(settings.data_dir)},
        "timestamp": datetime.now(tz=UTC).isoformat(),
    }
    typer.echo(json.dumps(checks, indent=2))


if __name__ == "__main__":
    app()
