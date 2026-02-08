# FAQ

1. **Does it need API keys?** No. Mock LLM keeps it offline-ready.
2. **Where is my data stored?** In JSON files under `data/` (or `PAIOS_DATA_DIR`).
3. **How do I reset demo data?** Delete `data/` and rerun `make demo`.
4. **Can I add real LLMs later?** Yes—replace `personal_ai_os.llm.mock.MockLLM` with your provider.
5. **Will it run on Windows?** Yes, uses pathlib and avoids POSIX-only paths.
6. **How do I get help?** Run `paios --help` or open an issue using the template.
