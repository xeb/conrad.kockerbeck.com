.PHONY: help

help:
	@echo "Site Make Commands"
	@echo "---------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## Sets up the project from a fresh clone
	pip install -r requirements.txt

site:  ## Builds the site and serves it locally
	python3 server.py

clean: ## cleans up the cruft from macFUSE
	echo "Cleaning up"
	find . -name "._*" -delete
	find . -name ".DS_Store" -delete

upload: ## Uploads the static assets
	./upload.sh
	git push origin main
	ssh xeb@gal.xeb.ai "cd ~/projects/conrad.kockerbeck.com && git pull origin main"
