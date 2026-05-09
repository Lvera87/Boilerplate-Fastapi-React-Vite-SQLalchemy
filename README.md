# Boilerplate FastAPI + React + Vite + SQLAlchemy

Boilerplate full-stack moderno con **FastAPI** (backend) y **React + Vite** (frontend). Tooling unificado: **UV** para Python, **Ruff** para lint/format en backend, **Biome** para lint/format/import-sort en frontend.

[![CI](https://github.com/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy/actions/workflows/ci.yml/badge.svg)](https://github.com/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy/actions)
[![codecov](https://codecov.io/gh/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy/graph/badge.svg)](https://codecov.io/gh/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy)

---

## 🎯 Características

- **Backend FastAPI** estructurado en capas (`api`, `core`, `db`, `models`, `schemas`, `services`).
- **SQLAlchemy 2.x async** + **Alembic** para migraciones.
- **Frontend React + Vite** con HMR, **TanStack Query** y **Axios**.
- **Tailwind CSS v3** preconfigurado.
- **UV** como gestor de paquetes y entornos Python (10–100x más rápido que pip).
- **Ruff** para lint y format Python (un solo binario reemplaza black/isort/flake8/pyupgrade).
- **Biome** para lint, format e import-sort en frontend (un solo binario reemplaza ESLint + Prettier).
- **Pytest** + pytest-asyncio + pytest-cov en backend; **Vitest** + Testing Library en frontend.
- **Pre-commit hooks** (ruff, biome, gitleaks).
- **Docker multi-stage** con usuario no-root y `.dockerignore` en ambos servicios.
- **GitHub Actions** con caché de UV/npm, Trivy para escaneo de vulnerabilidades.

---

## 📋 Requisitos previos

- **Python 3.11+**
- **Node.js 20+**
- **UV** ([instalación](https://docs.astral.sh/uv/getting-started/installation/))
  ```bash
  # Linux / macOS
  curl -LsSf https://astral.sh/uv/install.sh | sh
  # Windows (PowerShell)
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
- **Docker** (opcional)
- **Make** (opcional, para usar el `Makefile`)

---

## 🚀 Inicio rápido

```bash
git clone https://github.com/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy.git
cd Boilerplate-Fastapi-React-Vite-SQLalchemy

# Instala backend (uv crea .venv automáticamente) y frontend
make setup

# Aplica migraciones (genera primero una si no existen: make migration name="initial")
make migrate

# Levanta ambos servidores
make dev
```

Backend: <http://localhost:8000> · Frontend: <http://localhost:5173> · Docs: <http://localhost:8000/docs>

---

## 🧰 Comandos (Makefile)

| Comando | Descripción |
|---|---|
| `make setup` | Instala deps backend (`uv sync`) y frontend (`npm install`) |
| `make dev` | Levanta backend (uvicorn --reload) + frontend (vite) |
| `make dev-backend` | Solo backend |
| `make dev-frontend` | Solo frontend |
| `make migrate` | Aplica migraciones Alembic |
| `make migration name="..."` | Autogenera nueva migración |
| `make test` | Ejecuta tests backend + frontend |
| `make lint` | Ruff check + Biome check |
| `make lint-fix` | Auto-fix backend y frontend |
| `make format` | Format con Ruff y Biome |
| `make coverage` | Genera reportes de cobertura |
| `make docker-up` / `docker-down` | Docker Compose |
| `make clean` | Limpia caches, builds, venvs, node_modules |
| `make install-hooks` / `run-hooks` | Pre-commit hooks |

Ejecuta `make help` para ver el listado completo.

---

## 🐍 Backend (FastAPI + UV)

UV reemplaza `pip` + `venv` + `pip-tools`. La fuente de verdad es `backend/pyproject.toml` y el lockfile reproducible es `backend/uv.lock` (commitealo).

### Setup manual

```bash
cd backend
uv sync                  # crea .venv y instala todas las deps (prod + dev)
uv sync --no-dev         # solo prod (para Docker/runtime)
uv add <paquete>         # añadir dep de runtime
uv add --dev <paquete>   # añadir dep de desarrollo
uv lock --upgrade        # actualizar lockfile
uv run uvicorn app.main:app --reload
uv run pytest -v
uv run alembic upgrade head
```

> Nota: con `uv run <cmd>` no necesitas activar el venv manualmente.

### Lint & format con Ruff

```bash
uv run ruff check .              # lint
uv run ruff check --fix .        # auto-fix
uv run ruff format .             # format
uv run ruff format --check .     # check format (CI)
```

Configuración: `backend/ruff.toml` (line-length 120, target Py 3.11, reglas `E,W,F,I,B,C4,UP`).

---

## ⚛️ Frontend (React + Vite + Biome)

Biome reemplaza ESLint + Prettier + eslint-plugin-import (organize-imports nativo). Un solo binario, configuración única (`frontend/biome.json`).

### Setup manual

```bash
cd frontend
npm install
npm run dev
```

### Scripts disponibles

| Script | Acción |
|---|---|
| `npm run dev` | Vite dev server (puerto 5173) |
| `npm run build` | Build de producción |
| `npm run preview` | Previsualiza build (puerto 4173) |
| `npm run lint` | Biome lint |
| `npm run lint:fix` | Biome lint con `--write` |
| `npm run format` | Biome format con `--write` |
| `npm run check` | Lint + format + import-sort |
| `npm run check:fix` | Auto-fix de lo anterior |
| `npm run test` / `test:ci` / `test:coverage` | Vitest |

### Migración desde ESLint/Prettier

Los archivos `.eslintrc.cjs`, `.prettierrc` y `.prettierignore` fueron eliminados. Toda la configuración vive en `frontend/biome.json`. Equivalencias:

| ESLint/Prettier | Biome |
|---|---|
| `printWidth: 88` | `formatter.lineWidth: 88` |
| `singleQuote: true` | `javascript.formatter.quoteStyle: "single"` |
| `trailingComma: "all"` | `javascript.formatter.trailingCommas: "all"` |
| `eslint-plugin-jsx-a11y` | `linter.rules.a11y` (built-in) |
| `eslint-plugin-react-hooks` | `correctness.useExhaustiveDependencies` + `useHookAtTopLevel` |
| `eslint-plugin-import` (order) | `assist.actions.source.organizeImports` |

> ⚠️ `eslint-plugin-jsdoc` no tiene equivalente directo en Biome. Si necesitas validación de JSDoc, considera mantenerlo aparte o usar TypeScript.

---

## 🔧 Variables de entorno

Copia los ejemplos:

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### Backend (`backend/.env`)

```env
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO
APP_NAME=FastAPI Boilerplate
API_V1_PREFIX=/api/v1
BACKEND_CORS_ORIGINS=http://localhost:5173
DATABASE_URL=sqlite+aiosqlite:///./sql_app.db
SECRET_KEY=<genera-uno-fuerte>   # obligatorio en prod
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (`frontend/.env`)

```env
VITE_API_BASE_PATH=/api
VITE_API_VERSION=v1
VITE_APP_NAME=React Vite Boilerplate
```

---

## 🧪 Testing

```bash
# Backend
cd backend && uv run pytest --cov=app --cov-report=term --cov-report=html

# Frontend
cd frontend && npm run test:coverage
```

Umbral de cobertura backend: **70%** (ver `backend/pyproject.toml` → `[tool.coverage.report]`).

---

## 🐳 Docker

```bash
docker compose up --build       # backend (8000) + frontend dev (5173)
docker compose down
docker compose logs -f backend
```

Backend usa `python:3.11-slim` + UV multi-stage + usuario `app` (uid 1000) + healthcheck en `/api/v1/health/`.
Frontend tiene 3 targets: `deps`, `dev` (default) y `prod` (sirve `dist/` con `vite preview`).

```bash
# Build manual de imagen prod del frontend
docker build -t react-frontend:prod --target prod ./frontend
```

---

## 🪝 Pre-commit hooks

```bash
make install-hooks      # equivalente a: pre-commit install
make run-hooks          # corre todos los hooks en todos los archivos
```

Hooks configurados (`.pre-commit-config.yaml`):
- **Ruff** + **ruff-format** (backend)
- **uv-lock** (mantiene `uv.lock` en sync con `pyproject.toml`)
- **Biome check** (frontend)
- `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`, `check-json`, `check-merge-conflict`, `check-added-large-files`, `detect-private-key`
- **gitleaks** (escaneo de secretos)

---

## 📊 CI/CD (GitHub Actions)

`.github/workflows/ci.yml` ejecuta jobs en paralelo:

1. **backend-lint** — Ruff check + format check (con `setup-uv` + caché)
2. **backend-tests** — pytest + coverage → Codecov
3. **frontend-lint** — `biome ci` (lint + format + organize-imports)
4. **frontend-tests** — Vitest + coverage → Codecov
5. **build-docker** — Buildx con caché GHA para backend y `--target prod` del frontend
6. **security-scan** — Trivy con `severity HIGH,CRITICAL` y `exit-code: 1`

---

## 📁 Estructura

```text
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/{routes.py, endpoints/{health,users,auth}.py}
│   │   ├── core/{config,exceptions,logging,rate_limit,security}.py
│   │   ├── db/{base,session}.py
│   │   ├── models/user.py
│   │   ├── schemas/{health,user}.py
│   │   └── services/auth.py
│   ├── tests/{conftest,test_health,test_users}.py
│   ├── alembic/{env.py, versions/}
│   ├── pyproject.toml          # deps + uv config + pytest + coverage
│   ├── ruff.toml
│   ├── uv.lock                 # generado por uv (commit)
│   ├── Dockerfile              # uv multi-stage, non-root
│   └── .dockerignore
├── frontend/
│   ├── src/{main.jsx, App.jsx, api/, components/, config/}
│   ├── biome.json              # lint + format + organize-imports
│   ├── package.json
│   ├── vite.config.js
│   ├── vitest.config.js
│   ├── tailwind.config.cjs
│   ├── Dockerfile              # multi-stage (deps/dev/prod)
│   └── .dockerignore
├── scripts/{dev.ps1, test.ps1}
├── .github/workflows/ci.yml
├── .pre-commit-config.yaml
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## 🔒 Seguridad

- Rate limiting (slowapi) — recuerda aplicar `@limiter.limit(...)` en `/auth/login`.
- CORS configurable vía `BACKEND_CORS_ORIGINS`.
- Logging con rotación.
- Trivy en CI escanea filesystem completo.
- gitleaks en pre-commit detecta secretos antes del commit.

> Pendientes recomendados (ver auditoría): proteger endpoints de `/users` con `Depends(verify_token)`; eliminar default de `SECRET_KEY` en `app/core/config.py`; migrar `datetime.utcnow()` a `datetime.now(timezone.utc)` en `app/core/security.py`.

---

## 📚 API Docs

- **Swagger UI**: <http://localhost:8000/docs>
- **ReDoc**: <http://localhost:8000/redoc>
- **OpenAPI JSON**: <http://localhost:8000/openapi.json>

---

## 🤝 Contribuir

1. Fork → branch (`git checkout -b feature/foo`)
2. Asegura que pasen `make lint` y `make test`
3. Commit (los pre-commit hooks correrán automáticamente)
4. Push y abre un PR

---

## 📝 Licencia

MIT — ver `LICENSE`.
