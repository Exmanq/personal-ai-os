# Design Decisions

1. **JSON storage first**: Keeps setup under 5 minutes and works offline; easy to inspect/commit demo data.
2. **Mock LLM**: Deterministic summaries avoid API keys while preserving the shape for future LLM swaps.
3. **Typer CLI**: Human-friendly help + quick extensibility for new commands.
4. **Make targets**: `make setup/lint/test/demo/doctor` align with CI to guarantee reproducibility.
5. **Data dir override**: `PAIOS_DATA_DIR` lets users separate demo vs. real data without code changes.
6. **Cross-platform paths**: `pathlib` everywhere to stay Windows/macOS/Linux friendly.
7. **Fast tests**: All unit and CLI tests run in seconds with temporary dirs and no network calls.
