# Python Project Starter

[![CI](https://github.com/domoskanonos/python-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/domoskanonos/python-starter/actions/workflows/ci.yml)
[![CD](https://github.com/domoskanonos/python-starter/actions/workflows/cd.yml/badge.svg)](https://github.com/domoskanonos/python-starter/actions/workflows/cd.yml)
[![PyPI version](https://img.shields.io/pypi/v/domoskanonos-python-starter.svg)](https://pypi.org/project/domoskanonos-python-starter/)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

A modern, high-performance Python project template powered by [uv](https://github.com/astral-sh/uv). Designed for developers who want a clean, fast, and automated workflow.

---

## 🛠 Prerequisites

This project requires **uv**. If you don't have it installed, run:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 🚀 Quick Start

Get up and running in seconds:

```bash
# Clone the repository
git clone https://github.com/domoskanonos/python-starter.git
cd python-starter

# Install dependencies and create virtualenv automatically
uv sync

# Run the application
uv run python src/project/main.py
```

## ⚙️ Configuration

This project uses **Pydantic Settings** for configuration. You can use a `.env` file to override default values:

```bash
# .env
PROJECT_NAME="My Custom Project"
LOG_LEVEL="DEBUG"
```

## 🛠 Development Workflow

### Running Tests
We use `pytest` for testing.
```bash
uv run pytest
```

### Type Checking
Powered by `mypy` for static type analysis.
```bash
uv run mypy .
```

### Linting & Formatting
Powered by `ruff` for extreme speed.
```bash
# Check for linting issues
uv run ruff check .

# Format code
uv run ruff format .
```

### Pre-commit Hooks
Ensure code quality before every commit:
```bash
uv run pre-commit install
```

---

## 📦 Features

- **[uv](https://github.com/astral-sh/uv)**: Ultra-fast Python package and environment manager.
- **[Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)**: Robust configuration management via environment variables.
- **[Mypy](https://mypy-lang.org/)**: Static type checking for better code quality.
- **[Ruff](https://github.com/astral-sh/ruff)**: All-in-one linter and formatter.
- **[Docker](https://www.docker.com/)**: Multi-stage Dockerfile for optimized container images.
- **GitHub Actions**: 
  - **CI**: Automated testing, linting, and Docker build on every push.
  - **CD**: Automated publishing to PyPI on version tags.
- **Renovate**: Automated dependency updates with auto-merge support.

---

## 🚢 Deployment (PyPI)

This project is configured for **Trusted Publishing**.

1. **Update Version**: Change `version` in `pyproject.toml`.
2. **Tag & Push**:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
3. **Auto-Deploy**: The `cd.yml` workflow will automatically build and publish to PyPI.

---

## 🤖 Dependency Management

Dependencies are managed via `uv`. To add a new package:
```bash
uv add <package-name>
uv add --dev <dev-package-name>
```
3.  **Secret hinzufügen**: Gehe in deinem Repository zu `Settings -> Secrets and variables -> Actions` und erstelle ein Secret namens `RENOVATE_TOKEN` mit dem Wert deines Tokens.

### Manuelle Updates
Du kannst die Abhängigkeiten auch jederzeit manuell mit `uv` aktualisieren:

```bash
# Alle Pakete in der uv.lock auf die neueste kompatible Version heben
uv lock --upgrade

# Ein spezifisches Paket aktualisieren
uv lock --upgrade-package ruff

# Die lokale Umgebung (.venv) mit der uv.lock synchronisieren
uv sync
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE) für Details.
