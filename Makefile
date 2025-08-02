.PHONY: help install run test docker-build docker-run clean

help: ## Show this help message
	@echo "Timestep-OAI-Compatible-App"
	@echo "=========================="
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

run: ## Run the application locally
	python main.py

test: ## Run tests
	python test_example.py

docker-build: ## Build Docker image
	docker build -t timestep-oai-app .

docker-run: ## Run with Docker
	docker run -p 8000:8000 timestep-oai-app

docker-compose-up: ## Start with docker-compose
	docker-compose up -d

docker-compose-down: ## Stop docker-compose services
	docker-compose down

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
