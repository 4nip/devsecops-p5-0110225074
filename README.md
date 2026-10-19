# SecureTask — DevSecOps Pipeline Demo

A small command-line task manager built with Python. This repository demonstrates a basic DevSecOps pipeline using GitHub Actions, pytest, Bandit SAST, and a custom Quality Gate.

## Features
- Add a task with input validation
- List tasks
- Mark a task complete
- Reject empty task titles
- Keep application logic separate from CLI interaction

## Requirements
- Python 3.11 or newer
- pip

## Run locally
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install -r requirements.txt
python -m securetask
```

## Run tests
```bash
python -m pytest -v
```

## Run the SAST scan and Quality Gate locally
```bash
python -m pip install -r requirements-dev.txt
python -m bandit -r securetask -f json -o bandit-report.json
python scripts/quality_gate.py bandit-report.json
```

Bandit may return a non-zero exit code when findings are present. To ensure the JSON report is still evaluated by the custom gate, use:
```bash
python -m bandit -r securetask -f json -o bandit-report.json || true
python scripts/quality_gate.py bandit-report.json
```
In PowerShell, if needed, run the Bandit command and then the gate command separately.

## Pipeline overview
The workflow in `.github/workflows/devsecops.yml` runs on:
- `push` to `main`
- `pull_request` targeting `main`

It contains two separate jobs:
1. **build** — installs dependencies and runs unit tests.
2. **sast-scan** — runs Bandit and evaluates its JSON report with a Quality Gate. This job depends on `build`.

The Quality Gate is configured to fail when Bandit reports at least one **HIGH severity, HIGH confidence** finding. This is a simple demonstration policy, not a guarantee that the application is completely secure.

## Repository structure
```text
securetask/
  __init__.py
  __main__.py
  cli.py
  models.py
  service.py
  validators.py
tests/
  test_service.py
scripts/
  quality_gate.py
.github/workflows/
  devsecops.yml
requirements.txt
requirements-dev.txt
README.md
```

## Notes
- Do not commit secrets, access tokens, or passwords.
- A passing SAST scan does not prove that an application has no vulnerabilities.
- GitHub Actions runs remotely on a GitHub-hosted runner; no server deployment is performed by this demo.
