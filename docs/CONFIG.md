# Configuration

| Name | Default | Description |
| --- | --- | --- |
| `PAIOS_DATA_DIR` | `data/demo` | Directory for JSON state (notes/goals/tasks/reflections/knowledge). |
| `PAIOS_VERBOSE` | `false` | Enable verbose logging for CLI operations. |

Flags (CLI):
- `--data-dir PATH` to override data location per command.
- `--verbose` to print debug logs for the command.

Files:
- `data/<dataset>.json` created automatically if missing.
- `examples/output/` contains saved demo outputs from `make demo`.
