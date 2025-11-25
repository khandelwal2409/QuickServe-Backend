# QuickServe Backend - Template

This is a minimal Python FastAPI backend template exposing a small dummy API.

Endpoints
- `GET /api/health` — returns service health
- `GET /api/items/{id}` — fetch a dummy item
- `POST /api/items` — create a dummy item (accepts JSON `{name, description}`)

Quick start (PowerShell on Windows)

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/docs` to view the interactive API docs.

Run tests

```powershell
pip install -r requirements.txt
pytest -q
```
