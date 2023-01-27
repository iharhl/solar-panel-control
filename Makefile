install:
	pip install -r requirements.txt

run:
	python .\src\main.py 

.PHONY: clean-cache
clean-cache:
	@echo "+ $@"
	@rm -fr src/__pycache__/