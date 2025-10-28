# FinGuardian

FinGuardian is a lightweight prototype that helps analyze financial policies, profile risk, and detect scam messages using small, focused modules and prompt templates.

This repository contains helper modules and prompt templates intended for research and demonstration purposes (not production-ready).

## Key components

- `app.py` - small application entry point / demo runner.
- `modules/` - Python modules with small utilities: `chatbot_assistant.py`, `policy_analyzer.py`, `risk_profiler.py`, `scam_detector.py`.
- `prompts/` - plain text prompt templates used by the modules.
- `requirements.txt` - Python dependencies.

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app (example):

```powershell
python app.py
```

Notes:
- This project includes an example `finguardian_env/` virtual environment in the workspace — please do not commit or push any virtual environment folders. Use the provided `.gitignore`.
- If you see an `OPENAI_API_KEY` or similar secrets in files, remove them and rotate the key immediately. Use environment variables (for example a `.env` file + python-dotenv) to load secrets at runtime.

## Development

- To add a new helper, create a module in `modules/` and a prompt in `prompts/` if needed.
- Keep modules small and unit-testable. Consider adding tests under a `tests/` folder.

## Pushing only prompts & modules

If you want to push only `prompts/` and `modules/` (and not the virtualenv), a safe option is to create a separate branch and push that branch.

During recent housekeeping I created a cleaned branch with only these folders (and removed an exposed key from `modules/scam_detector.py`):

- Branch: `push-prompts-modules-clean`
- Pull request URL (review & merge): https://github.com/navyaagrawal20/FinGuardian/pull/new/push-prompts-modules-clean

## Security

- Never commit API keys or credentials to git. If a secret is accidentally committed, rotate it immediately and remove it from history.
- Use `.env` files (ignored by git) or a secret manager for sensitive values.

## License

MIT — see `LICENSE` (or add one) if you plan to open-source the project.

---

If you'd like, I can also:
- Commit and push this updated README to the current branch (I left it as a working-tree edit),
- Clean up the temporary worktree I created earlier, or
- Add a short HOWTO for adding tests and CI.


