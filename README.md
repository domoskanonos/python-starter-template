# Python Project Starter

Ein modernes Python-Projekt-Template, das [uv](https://github.com/astral-sh/uv) für das Abhängigkeitsmanagement und den Build-Prozess verwendet.

## Features

- **uv**: Extrem schneller Python-Paket- und Umgebungsmanager.
- **Hatchling**: Modernes Build-Backend.
- **Pytest**: Test-Framework für Unit-Tests.
- **GitHub Actions**: Automatisierte Veröffentlichung auf PyPI.
- **Ruff**: Schneller Linter und Formatter (in den Dev-Dependencies).

## Voraussetzungen

Stelle sicher, dass `uv` installiert ist:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

Klone das Repository und installiere die Abhängigkeiten:

```bash
git clone https://github.com/domoskanonos/python-starter.git
cd python-starter
uv sync
```

## Entwicklung

### Tests ausführen

Verwende `pytest`, um die Tests im `tests/` Verzeichnis auszuführen:

```bash
uv run pytest
```

### Hauptprogramm starten

```bash
uv run python src/project/main.py
```

## Veröffentlichung auf PyPI

Dieses Projekt ist so konfiguriert, dass es automatisch auf PyPI veröffentlicht wird, wenn ein neuer Git-Tag erstellt wird.

### 1. Projektnamen anpassen

Bevor du veröffentlichst, stelle sicher, dass der Name in der `pyproject.toml` einzigartig ist:

```toml
[project]
name = "dein-einzigartiger-paketname"
```

### 2. Veröffentlichung via Tags

Die GitHub Action reagiert auf Tags, die mit `v` beginnen (z. B. `v0.1.0`).

**Schritte zum Veröffentlichen:**

1.  **Version erhöhen**: Ändere die `version` in der `pyproject.toml`.
2.  **Änderungen committen**:
    ```bash
    git add pyproject.toml
    git commit -m "Bump version to 0.1.0"
    git push origin main
    ```
3.  **Tag erstellen und pushen**:
    ```bash
    git tag v0.1.0
    git push origin v0.1.0
    ```

Sobald der Tag gepusht wird, startet der GitHub Action Workflow "Publish to PyPI" und lädt das Paket hoch.

### 3. Trusted Publishing (Wichtig!)

Damit die GitHub Action auf PyPI hochladen darf, musst du **Trusted Publishing** auf PyPI einrichten:

1. Gehe zu [PyPI Publishing](https://pypi.org/manage/account/publishing/).
2. Füge einen neuen "Publisher" hinzu.
3. Wähle GitHub.
4. Gib den Owner (`domoskanonos`), das Repository (`python-starter`) und den Workflow-Dateinamen (`publish.yml`) an.

## Abhängigkeiten aktuell halten

### Automatische Updates
Dieses Projekt verwendet **Renovate**, um Abhängigkeiten automatisch aktuell zu halten. Renovate scannt regelmäßig die `pyproject.toml` und `uv.lock` und erstellt Pull Requests für neue Versionen.

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
