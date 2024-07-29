.PHONY: help

help:
	@echo "Site Make Commands"
	@echo "---------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## Sets up the project from a fresh clone
	pip install -r requirements.txt

build: ## Creates the site
	python3 main.py

site: build ## Builds the site and serves it locally
	python3 -m http.server 8007
