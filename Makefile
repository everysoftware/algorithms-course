.PHONY: test
test:
	@echo "Running tests..."
	pytest -s -v tests


.PHONY: format
format:
	@echo "Running ruff..."
	ruff format src tests


.PHONY: freeze
freeze:
	@echo "Freezing requirements..."
	pip freeze > requirements.txt