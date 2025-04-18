
.PHONY: install list format lint test all clean synth deploy diff destroy

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

list:
	@echo "Listing installed packages..."
	pip list

format:
	@echo "Formatting code with Black..."
	black .

lint:
	@echo "Linting code with Pylint..."
	pylint --disable=R,C $(shell find . -name "*.py" ! -path "./.venv/*")

test:
	@echo "Running tests..."
	pytest -vv test_*.py

synth:
	@echo "Synthesizing the CDK app..."
	cdk synth

deploy:
	@echo "Deploying the CDK stack..."
	cdk deploy --require-approval never

diff:
	@echo "Showing diff against deployed stack..."
	cdk diff

destroy:
	@echo "Destroying the CDK stack..."
	cdk destroy --force

clean:
	@echo "Cleaning up __pycache__ and .pytest_cache..."
	find . -type d -name "__pycache__" -exec rm -r {} + || true
	rm -rf .pytest_cache

all: install format lint test
