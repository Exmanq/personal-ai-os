# Architecture

```mermaid
graph TD
  CLI[paios CLI] -->|reads/writes| Storage[(JSON Files)]
  Storage --> Notes[Memory Module]
  Storage --> Goals[Goals Module]
  Storage --> Tasks[Tasks Module]
  Storage --> Knowledge[Knowledge Module]
  Notes --> Reflection[Reflection Module]
  Reflection --> MockLLM[Mock LLM]
```

- **CLI** exposes commands for notes, goals, planning, reflection, and knowledge search.
- **Storage** is a light JSON layer writing to `data/` (overridable via `PAIOS_DATA_DIR`).
- **Modules** implement domain logic: memory, goals, tasks, knowledge, and reflection.
- **Mock LLM** produces deterministic summaries so the project works offline.
- **Docs & Examples** show flows; `make demo` writes outputs to `examples/output`.
- **CI** enforces lint + tests; Makefile guarantees setup/lint/test/demo/doctor in one step.
