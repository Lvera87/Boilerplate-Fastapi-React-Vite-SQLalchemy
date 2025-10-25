# Boilerplate FastAPI + React + Vite + SQLAlchemy# Boilerplate FastAPI + React

 

Un boilerplate moderno y completo para iniciar proyectos full-stack con **FastAPI** (backend) y **React + Vite** (frontend). Incluye toda la configuración necesaria para desarrollo ágil, testing, linting, CI/CD y deployment.Un punto de partida moderno que combina **FastAPI** en el backend y **React + Vite** en el frontend.

Incluye configuración de pruebas, linters, gestión de entornos y scripts para acelerar el desarrollo.

## 🎯 Características principales

## Características principales

- **Backend FastAPI** estructurado en capas (`core`, `api`, `db`, `schemas`, `models`, `tests`).

- **Frontend React + Vite** con Hot Module Replacement (HMR), React Query para manejo de estado remoto, y Axios para HTTP.- Backend FastAPI estructurado en capas (`core`, `api`, `schemas`, `tests`).

- **Base de datos** con SQLAlchemy (async) + Alembic para migraciones versionadas.- Configuración de CORS, logging, settings con `pydantic-settings` y ejemplo de endpoint de salud.

- **Estilos** con Tailwind CSS v3 preconfigurado.- Frontend React con Vite, React Query y Axios listo para consumir el backend.

- **Linting & Formatting**: \- Persistencia de datos con **SQLAlchemy (asyncio)** y **Alembic** para migraciones.

  - Backend: Ruff (linting + formatting)- Tooling completo: ESLint + Prettier, Vitest + Testing Library, Pytest + HTTPX.

  - Frontend: ESLint + Prettier + JSDoc- Compatibilidad con Docker Compose para levantar ambos servicios.

- **Testing**:

  - Backend: Pytest + pytest-asyncio + pytest-cov## Requisitos previos

  - Frontend: Vitest + Testing Library

- **CI/CD**: GitHub Actions con linting, testing, coverage, y builds Docker.- Python 3.11+

- **Pre-commit hooks** para garantizar calidad de código antes de commits.- Node.js 20+

- **Rate limiting** (slowapi) y manejo de errores global en el backend.- npm 10+

- **Health checks** mejorados con estado de base de datos.- Docker (opcional, para entorno contenedor)

- **Logging** centralizado con rotación de archivos.

- **Docker**: Multistage builds optimizados para ambos servicios.## Estado del CI

- **Makefile** con targets para setup, dev, test, lint, build, etc.

- ![CI](https://github.com/usuario/repo/actions/workflows/ci.yml/badge.svg)

## 📋 Requisitos previos- ![Coverage](https://raw.githubusercontent.com/usuario/repo/main/backend/coverage.xml)



- **Python 3.11+**## Puesta en marcha rápida

- **Node.js 20+** (npm 10+)

- **Docker** (opcional, para entorno contenedor)### Backend

- **Git** (para pre-commit hooks)

```bash

## 🚀 Inicio rápidocd backend

python -m venv .venv

### Opción 1: Usar Makefile (Recomendado).venv\Scripts\activate  # Windows PowerShell

pip install -r requirements.txt

```bash# Ejecutar migraciones (crea base de datos y tablas)

# Clonar el repositorio.venv\Scripts\alembic upgrade head

git clone https://github.com/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy.git# Iniciar servidor de desarrollo

cd Boilerplate-Fastapi-React-Vite-SQLalchemyuvicorn app.main:app --reload

```

# Setup del entorno de desarrollo

make setupLa API estará disponible en <http://localhost:8000>.



# Aplicar migraciones de base de datos### Frontend

make migrate

```bash

# Iniciar ambos servidorescd frontend

make devnpm install

npm run dev

# En otra terminal, solo el backend:```

make dev-backend

La aplicación se abrirá en <http://localhost:5173> y tendrá proxy hacia el backend en desarrollo.

# O solo el frontend:

make dev-frontend## Variables de entorno



# Ejecutar testsCopiar los ejemplos proporcionados y ajustarlos según corresponda:

make test

- Backend: `backend/.env.example` → `backend/.env`

# Ejecutar linters- Frontend: `frontend/.env.example` → `frontend/.env`

make lint

## Scripts útiles

# Arreglar linting issues automáticamente

make lint-fix### Backend (scripts)



# Generar reporte de cobertura- `alembic revision --autogenerate -m "<mensaje>"` para scaffold de migración.

make coverage- `alembic upgrade head` para aplicar migraciones.

- `pytest` para ejecutar las pruebas.

# Ver todos los comandos disponibles- `uvicorn app.main:app --reload` para entorno de desarrollo.

make help

```### Frontend (scripts)



### Opción 2: Setup manual- `npm run dev`: servidor de desarrollo con Vite.

- `npm run build`: build de producción.

#### Backend- `npm run preview`: previsualizar build.

- `npm run lint`: ejecutar ESLint.

```bash- `npm run test`: correr Vitest.

cd backend

## Docker Compose

# Crear virtual environment

python -m venv .venv```bash

docker compose up --build

# Activar (Windows PowerShell)```

.venv\Scripts\Activate.ps1

Levanta backend (Uvicorn) y frontend (Vite) con hot reload.

# Activar (Linux/macOS)

source .venv/bin/activate## Estructura del proyecto



# Instalar dependencias```text

pip install -r requirements.txtbackend/

  app/

# Crear archivo de configuración    api/

cp .env.example .env    core/

    schemas/

# Aplicar migraciones  tests/

alembic upgrade headfrontend/

  public/

# Iniciar servidor de desarrollo  src/

uvicorn app.main:app --reload    api/

```    components/

    config/

La API estará disponible en **http://localhost:8000**.```



#### Frontend## Próximos pasos sugeridos



```bash- Añadir autenticación (JWT, OAuth2).

cd frontend- Configurar CI/CD (GitHub Actions, GitLab CI, etc.).

- Integrar herramientas de observabilidad (Prometheus, Sentry).

# Instalar dependencias- Añadir temas de UI o librería de componentes.

npm install

comando para iniciar el servidor de desarrollo del backend en Windows PowerShell:

# Crear archivo de configuración

cp .env.example .envcd "D:\Trabajo\Boilerplate FastApi y React\backend"

. .\.venv\Scripts\Activate.ps1

# Iniciar servidor de desarrollouvicorn app.main:app --reload --host 127.0.0.1 --port 8000

npm run dev

```comando para iniciar el servidor de desarrollo del frontend en Windows PowerShell:



La aplicación se abrirá en **http://localhost:5173**.cd "D:\Trabajo\Boilerplate FastApi y React\frontend"

npm run dev

## 📁 Estructura del proyecto


```
.
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # Entrypoint FastAPI
│   │   ├── api/
│   │   │   ├── routes.py        # Router principal
│   │   │   └── endpoints/       # Endpoints por dominio
│   │   │       ├── health.py
│   │   │       └── users.py
│   │   ├── core/
│   │   │   ├── config.py        # Configuración (pydantic-settings)
│   │   │   ├── exceptions.py    # Handlers de excepciones
│   │   │   ├── logging.py       # Configuración de logging
│   │   │   └── rate_limit.py    # Rate limiting (slowapi)
│   │   ├── db/
│   │   │   ├── base.py          # Base declarativa SQLAlchemy
│   │   │   └── session.py       # Engine y Session async
│   │   ├── models/
│   │   │   └── user.py          # Modelos SQLAlchemy
│   │   └── schemas/
│   │       ├── health.py        # Schemas para health endpoint
│   │       └── user.py          # Schemas Pydantic
│   ├── tests/
│   │   ├── conftest.py          # Fixtures pytest
│   │   ├── test_health.py
│   │   └── test_users.py
│   ├── alembic/                 # Migraciones de BD
│   ├── .env.example
│   ├── requirements.txt
│   ├── pyproject.toml           # Configuración pytest, ruff
│   ├── ruff.toml                # Configuración Ruff
│   └── Dockerfile               # Multistage build
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx             # Entrypoint React
│   │   ├── App.jsx
│   │   ├── styles.css           # Tailwind + CSS personalizado
│   │   ├── api/
│   │   │   ├── client.js        # Cliente HTTP (Axios)
│   │   │   └── health.js        # Endpoints health
│   │   ├── components/
│   │   │   ├── Layout.jsx
│   │   │   └── HealthStatus.jsx
│   │   └── config/
│   │       └── env.js           # Variables de entorno
│   ├── public/
│   │   └── index.html
│   ├── __tests__/
│   │   └── App.test.jsx
│   ├── .env.example
│   ├── package.json
│   ├── tailwind.config.cjs      # Configuración Tailwind
│   ├── postcss.config.cjs       # Configuración PostCSS
│   ├── vite.config.js           # Configuración Vite
│   ├── vitest.config.js         # Configuración Vitest
│   ├── .eslintrc.cjs            # Configuración ESLint
│   ├── .prettierrc              # Configuración Prettier
│   └── Dockerfile               # Multistage build
│
├── scripts/
│   ├── dev.ps1                  # Script dev para Windows
│   └── test.ps1                 # Script tests para Windows
│
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI/CD
│
├── .pre-commit-config.yaml      # Pre-commit hooks
├── .gitignore
├── docker-compose.yml           # Orquestación Docker
├── Makefile                     # Targets para desarrollo
└── README.md
```

## 🔧 Configuración

### Variables de entorno

#### Backend (`.env`)

Ver `backend/.env.example` para todas las variables disponibles:

```bash
# Environment
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# Application
APP_NAME=FastAPI Boilerplate
PROJECT_VERSION=0.1.0
API_V1_PREFIX=/api/v1

# CORS
BACKEND_CORS_ORIGINS=http://localhost:5173

# Database
DATABASE_URL=sqlite+aiosqlite:///./sql_app.db

# Security (cuando implementes auth)
# SECRET_KEY=your-secret-key
# ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### Frontend (`.env`)

Ver `frontend/.env.example`:

```bash
VITE_API_BASE_PATH=/api
VITE_API_VERSION=v1
VITE_APP_NAME=React Vite Boilerplate
VITE_DEBUG=true
```

## 🧪 Testing

```bash
# Backend: Ejecutar tests con coverage
cd backend
pytest --cov=app --cov-report=html

# Frontend: Ejecutar tests en modo CI
cd frontend
npm run test:ci

# Frontend: Ejecutar tests con coverage
npm run test:coverage

# Ambos (usando Makefile)
make test
make coverage
```

## 🎨 Linting & Formatting

```bash
# Backend: Lint con Ruff
cd backend
ruff check .
ruff format --check .

# Backend: Arreglar issues automáticamente
ruff check --fix .
ruff format .

# Frontend: ESLint + Prettier
cd frontend
npm run lint
npm run format

# Ambos (usando Makefile)
make lint        # Solo verificar
make lint-fix    # Arreglar automáticamente
```

## 🔄 Pre-commit hooks

Instalar hooks para ejecutar linters/tests antes de commits:

```bash
# Instalar pre-commit
pip install pre-commit

# Instalar los hooks en el repo
pre-commit install

# Ejecutar hooks en todos los archivos (opcional)
pre-commit run --all-files
```

Los hooks ejecutarán:
- Ruff (Python linting + formatting)
- ESLint (JavaScript linting)
- Prettier (JavaScript formatting)
- Trailing whitespace y EOF fixes

## 🐳 Docker

### Build y run con Docker Compose

```bash
# Construir e iniciar servicios
docker compose up --build

# Solo iniciar (sin rebuild)
docker compose up

# Detener servicios
docker compose down

# Ver logs
docker compose logs -f backend
docker compose logs -f frontend
```

Backend estará en **http://localhost:8000**, frontend en **http://localhost:5173**.

### Build manual

```bash
# Backend
cd backend
docker build -t fastapi-backend:latest .
docker run -p 8000:8000 fastapi-backend:latest

# Frontend
cd frontend
docker build -t react-frontend:latest .
docker run -p 5173:5173 react-frontend:latest
```

## 📊 CI/CD (GitHub Actions)

El repositorio incluye workflow automático en `.github/workflows/ci.yml` que ejecuta:

1. **Backend Lint** (Ruff) — Verifica calidad de código Python
2. **Backend Tests** — Pytest con cobertura
3. **Frontend Lint** (ESLint + Prettier) — Verifica calidad de código JS
4. **Frontend Tests** — Vitest con cobertura
5. **Build Docker** — Valida Dockerfiles
6. **Security Scan** (Trivy) — Escanea vulnerabilidades

Los reportes de cobertura se suben a **Codecov** automáticamente.

### Estadísticas de CI

- [![CI](https://github.com/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy/actions/workflows/ci.yml/badge.svg)](https://github.com/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy/actions)
- [![codecov](https://codecov.io/gh/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy/graph/badge.svg)](https://codecov.io/gh/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy)

## 🛠 Scripts útiles

### Backend

```bash
# Crear nueva migración
alembic revision --autogenerate -m "descripción de cambio"

# Aplicar migraciones
alembic upgrade head

# Ver estado de migraciones
alembic current

# Revertir última migración
alembic downgrade -1
```

### Frontend

```bash
# Previsualizar build de producción
npm run preview

# Limpiar caché y dist
npm run clean

# Ejecutar tests en watch mode
npm run test
```

## 📚 Documentación de APIs

### Health Check

```bash
GET /health
```

Respuesta:

```json
{
  "status": "ok",
  "timestamp": "2025-10-25T12:00:00Z",
  "database": {
    "connected": true,
    "engine": "SQLite (Async)"
  }
}
```

### Swagger/OpenAPI

La documentación interactiva está disponible en:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🔒 Seguridad

- CORS configurado (localhost:5173 por defecto)
- Rate limiting con slowapi
- Manejo global de excepciones
- Headers de seguridad estándar
- Logging de eventos importantes

## 🚀 Próximos pasos

- [ ] Agregar autenticación (JWT, OAuth2)
- [ ] Integrar Sentry para error tracking
- [ ] Configurar base de datos PostgreSQL para producción
- [ ] Agregar librería de componentes UI (shadcn/ui, etc.)
- [ ] Implementar paginación y filtros en endpoints
- [ ] Agregar validación de input más robusta
- [ ] Configurar deployment a Heroku/Vercel/AWS
- [ ] Agregar E2E tests (Cypress/Playwright)

## 📝 Licencia

Este proyecto está bajo licencia MIT. Ver `LICENSE` para detalles.

## 👤 Autor

- **GitHub**: [@Lvera87](https://github.com/Lvera87)

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/amazing-feature`)
3. Commit cambios (`git commit -m 'Add some amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## 📞 Soporte

Para problemas, sugerencias o preguntas, abre un [issue](https://github.com/Lvera87/Boilerplate-Fastapi-React-Vite-SQLalchemy/issues).
