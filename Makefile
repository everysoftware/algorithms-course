.PHONY: test
test:
	@echo "Running tests..."
	@pytest -s -v tests


.PHONY: format
format:
	@echo "Running ruff..."
	@ruff format .

.PHONY: lint
lint:
	@echo "Running ruff and mypy..."
	@ruff check . --fix
	@mypy src --strict

.PHONY: fix
fix:
	@make lint
	@make format

.PHONY: freeze
freeze:
	@echo "Freezing requirements..."
	@pip freeze > requirements.txt
