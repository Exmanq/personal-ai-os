# Security

- No secrets stored in the repo. Use environment variables (`.env` is gitignored).
- Keep API keys (if added later) in your shell or a secrets manager; never commit.
- Logs avoid printing secrets; verbose mode prints file paths only.
- Report vulnerabilities via GitHub issues or security contacts.
