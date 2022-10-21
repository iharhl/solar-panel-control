install:
	pip install -r requirements.txt

run:
	python3 .\src\main.py 

.PHONY: clean-build
clean-build: ## Remove build artifacts
	@echo "+ $@"
	@rm -fr build/
	@rm -fr dist/

.PHONY: clean-cache
clean-build: ## Remove py cache
	@echo "+ $@"
	@rm -fr src/__pycache__/