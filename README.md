# Boilerplate FastAPI + React
 
Un punto de partida moderno que combina **FastAPI** en el backend y **React + Vite** en el frontend.
Incluye configuración de pruebas, linters, gestión de entornos y scripts para acelerar el desarrollo.

## Características principales

- Backend FastAPI estructurado en capas (`core`, `api`, `schemas`, `tests`).
- Configuración de CORS, logging, settings con `pydantic-settings` y ejemplo de endpoint de salud.
- Frontend React con Vite, React Query y Axios listo para consumir el backend.
\- Persistencia de datos con **SQLAlchemy (asyncio)** y **Alembic** para migraciones.
- Tooling completo: ESLint + Prettier, Vitest + Testing Library, Pytest + HTTPX.
- Compatibilidad con Docker Compose para levantar ambos servicios.

## Requisitos previos

- Python 3.11+
- Node.js 20+
- npm 10+
- Docker (opcional, para entorno contenedor)

## Estado del CI

- ![CI](https://github.com/usuario/repo/actions/workflows/ci.yml/badge.svg)
- ![Coverage](https://raw.githubusercontent.com/usuario/repo/main/backend/coverage.xml)

## Puesta en marcha rápida

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
# Ejecutar migraciones (crea base de datos y tablas)
.venv\Scripts\alembic upgrade head
# Iniciar servidor de desarrollo
uvicorn app.main:app --reload
```

La API estará disponible en <http://localhost:8000>.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

La aplicación se abrirá en <http://localhost:5173> y tendrá proxy hacia el backend en desarrollo.

## Variables de entorno

Copiar los ejemplos proporcionados y ajustarlos según corresponda:

- Backend: `backend/.env.example` → `backend/.env`
- Frontend: `frontend/.env.example` → `frontend/.env`

## Scripts útiles

### Backend (scripts)

- `alembic revision --autogenerate -m "<mensaje>"` para scaffold de migración.
- `alembic upgrade head` para aplicar migraciones.
- `pytest` para ejecutar las pruebas.
- `uvicorn app.main:app --reload` para entorno de desarrollo.

### Frontend (scripts)

- `npm run dev`: servidor de desarrollo con Vite.
- `npm run build`: build de producción.
- `npm run preview`: previsualizar build.
- `npm run lint`: ejecutar ESLint.
- `npm run test`: correr Vitest.

## Docker Compose

```bash
docker compose up --build
```

Levanta backend (Uvicorn) y frontend (Vite) con hot reload.

## Estructura del proyecto

```text
backend/
  app/
    api/
    core/
    schemas/
  tests/
frontend/
  public/
  src/
    api/
    components/
    config/
```

## Próximos pasos sugeridos

- Añadir autenticación (JWT, OAuth2).
- Configurar CI/CD (GitHub Actions, GitLab CI, etc.).
- Integrar herramientas de observabilidad (Prometheus, Sentry).
- Añadir temas de UI o librería de componentes.
