.PHONY: help setup setup-backend setup-frontend dev dev-backend dev-frontend \
        migrate test test-backend test-frontend lint lint-fix format \
        coverage build docker-up docker-down clean install-hooks run-hooks

# Colors for output
CYAN  := \033[0;36m
GREEN := \033[0;32m
NC    := \033[0m

help: ## Show this help message
	@echo "$(CYAN)Available commands:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)  %-18s$(NC) %s\n", $$1, $$2}'

# ---------- Setup ----------
setup: setup-backend setup-frontend ## Set up backend (uv) and frontend (npm)
	@echo "$(GREEN)✓ Development environment ready$(NC)"

setup-backend: ## Install backend deps with uv (creates .venv automatically)
	@echo "$(CYAN)Installing backend dependencies with uv...$(NC)"
	cd backend && uv sync

setup-frontend: ## Install frontend deps
	@echo "$(CYAN)Installing frontend dependencies...$(NC)"
	cd frontend && npm install

# ---------- Dev servers ----------
dev: ## Start backend (background) and frontend
	@echo "$(CYAN)Starting backend and frontend...$(NC)"
	cd backend && uv run uvicorn app.main:app --reload &
	cd frontend && npm run dev

dev-backend: ## Start backend only
	cd backend && uv run uvicorn app.main:app --reload

dev-frontend: ## Start frontend only
	cd frontend && npm run dev

# ---------- DB ----------
migrate: ## Apply alembic migrations
	cd backend && uv run alembic upgrade head

migration: ## Autogenerate a new migration: make migration name="add_users_table"
	cd backend && uv run alembic revision --autogenerate -m "$(name)"

# ---------- Tests ----------
test: test-backend test-frontend ## Run all tests

test-backend: ## Run backend tests
	cd backend && uv run pytest -v

test-frontend: ## Run frontend tests
	cd frontend && npm run test:ci

coverage: ## Generate coverage reports
	cd backend && uv run pytest --cov=app --cov-report=term --cov-report=html
	cd frontend && npm run test:coverage

# ---------- Lint / format ----------
lint: ## Run linters (ruff + biome)
	cd backend && uv run ruff check . && uv run ruff format --check .
	cd frontend && npm run check

lint-fix: ## Auto-fix lint and format issues
	cd backend && uv run ruff check --fix . && uv run ruff format .
	cd frontend && npm run check:fix

format: ## Format code (ruff + biome)
	cd backend && uv run ruff format .
	cd frontend && npm run format

# ---------- Build ----------
build: ## Build production bundles
	cd backend && uv build
	cd frontend && npm run build

# ---------- Docker ----------
docker-up: ## Start services with Docker Compose
	docker compose up --build

docker-down: ## Stop Docker Compose services
	docker compose down

# ---------- Cleanup ----------
clean: ## Remove caches, builds, venvs, node_modules
	cd backend && rm -rf .venv .pytest_cache .ruff_cache __pycache__ build dist *.egg-info .coverage htmlcov coverage.xml
	cd frontend && rm -rf node_modules dist coverage .vite
	find . -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# ---------- Hooks ----------
install-hooks: ## Install pre-commit hooks
	uv tool run pre-commit install || pre-commit install

run-hooks: ## Run pre-commit hooks on all files
	uv tool run pre-commit run --all-files || pre-commit run --all-files

.DEFAULT_GOAL := help
