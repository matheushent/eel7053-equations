dependencies: ## Install project dependencies needed to run the application
	pip install -U pip wheel
	pip install -r requirements.txt

lint: ## Run flake8 linter. It will checks syntax errors or undefined names
	flake8 $(git ls-files | grep 'ˆscripts\|\.py$') --count --select=E9,F63,F7,F82 --show-source --statistics

autopep: ## Run autopep8
	autopep8 --in-place $(git ls-files | grep 'ˆscripts\|\.py$')

cdk: ## Install CDK and its Python dependencies to develop the AWS architecture
	npm i -g aws-cdk
	pip install -r requirements-cdk.txt

clean: ## Remove temporary file holding the app settings
	rm -rf cdk.out

run: ## Start uvicorn app on port 8080
	uvicorn \
		--host 127.0.0.1 \
		--port 8080 \
		--interface asgi3 \
		src.main:app --reload

test: ## Run tests against the application
	pytest -v

# Display target comments in 'make help'
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'