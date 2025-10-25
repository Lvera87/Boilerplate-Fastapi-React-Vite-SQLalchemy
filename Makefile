.PHONY: help setup dev test lint format build clean coverage

# Colors for output
CYAN := \033[0;36m
GREEN := \033[0;32m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(CYAN)Available commands:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)  %-20s$(NC) %s\n", $$1, $$2}'

setup: ## Set up development environment (Python venv + npm)
	@echo "$(CYAN)Setting up development environment...$(NC)"
	cd backend && python -m venv .venv && .venv/Scripts/pip install -r requirements.txt
	cd frontend && npm install
	@echo "$(GREEN)✓ Development environment ready$(NC)"

dev: ## Start both backend and frontend servers
	@echo "$(CYAN)Starting backend and frontend...$(NC)"
	cd backend && .venv/Scripts/uvicorn app.main:app --reload &
	cd frontend && npm run dev

dev-backend: ## Start backend server only
	@echo "$(CYAN)Starting backend...$(NC)"
	cd backend && .venv/Scripts/uvicorn app.main:app --reload

dev-frontend: ## Start frontend server only
	@echo "$(CYAN)Starting frontend...$(NC)"
	cd frontend && npm run dev

migrate: ## Apply database migrations
	@echo "$(CYAN)Running migrations...$(NC)"
	cd backend && .venv/Scripts/alembic upgrade head
	@echo "$(GREEN)✓ Migrations applied$(NC)"

test: ## Run all tests (backend + frontend)
	@echo "$(CYAN)Running backend tests...$(NC)"
	cd backend && .venv/Scripts/pytest -v
	@echo "$(CYAN)Running frontend tests...$(NC)"
	cd frontend && npm run test:ci

test-backend: ## Run backend tests only
	@echo "$(CYAN)Running backend tests...$(NC)"
	cd backend && .venv/Scripts/pytest -v

test-frontend: ## Run frontend tests only
	@echo "$(CYAN)Running frontend tests...$(NC)"
	cd frontend && npm run test:ci

lint: ## Run linters (ruff + eslint)
	@echo "$(CYAN)Running linters...$(NC)"
	cd backend && .venv/Scripts/ruff check . && .venv/Scripts/ruff format --check .
	cd frontend && npm run lint
	@echo "$(GREEN)✓ All linters passed$(NC)"

lint-fix: ## Auto-fix linting issues
	@echo "$(CYAN)Fixing linting issues...$(NC)"
	cd backend && .venv/Scripts/ruff check --fix . && .venv/Scripts/ruff format .
	cd frontend && npm run lint -- --fix
	@echo "$(GREEN)✓ Linting issues fixed$(NC)"

coverage: ## Generate test coverage reports
	@echo "$(CYAN)Generating coverage reports...$(NC)"
	cd backend && .venv/Scripts/pytest --cov=app --cov-report=html
	cd frontend && npm run test:ci -- --coverage
	@echo "$(GREEN)✓ Coverage reports generated$(NC)"

build: ## Build production bundles
	@echo "$(CYAN)Building production bundles...$(NC)"
	cd backend && .venv/Scripts/pip install build && python -m build
	cd frontend && npm run build
	@echo "$(GREEN)✓ Build complete$(NC)"

docker-up: ## Start services with Docker Compose
	@echo "$(CYAN)Starting Docker services...$(NC)"
	docker compose up --build

docker-down: ## Stop Docker Compose services
	@echo "$(CYAN)Stopping Docker services...$(NC)"
	docker compose down

clean: ## Clean up temporary files and caches
	@echo "$(CYAN)Cleaning up...$(NC)"
	cd backend && rm -rf __pycache__ .pytest_cache .venv build dist *.egg-info .coverage htmlcov
	cd frontend && rm -rf node_modules dist .next out coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "$(GREEN)✓ Cleanup complete$(NC)"

install-hooks: ## Install pre-commit hooks
	@echo "$(CYAN)Installing pre-commit hooks...$(NC)"
	pre-commit install
	@echo "$(GREEN)✓ Pre-commit hooks installed$(NC)"

run-hooks: ## Run pre-commit hooks on all files
	@echo "$(CYAN)Running pre-commit hooks...$(NC)"
	pre-commit run --all-files
	@echo "$(GREEN)✓ Pre-commit hooks completed$(NC)"

.DEFAULT_GOAL := help
