# Automated GitHub PR Review Agent

This project is an AI-powered system that automatically reviews GitHub pull requests by analyzing code diffs and generating structured review feedback using a multi-agent LLM pipeline.

## What this project does
- Fetches pull request diffs directly from GitHub
- Parses and understands file-level code changes
- Generates review comments with issue descriptions, severity, and suggestions
- Produces a concise summary of the overall PR
- Supports both GitHub PR reviews and manually provided diffs

## How it works
The review process is handled through multiple agents:
1. **Parser Agent** – analyzes and structures code diffs  
2. **Reviewer Agent** – generates detailed review comments  
3. **Summary Agent** – produces a high-level PR summary  

Each agent focuses on a specific responsibility to keep the system modular and extensible.

## Why I built this
Manual code reviews can be time-consuming. This project explores how LLMs can assist developers by providing fast, consistent, and structured feedback on pull requests while keeping humans in the loop.

## Tech stack
- Python
- FastAPI
- Large Language Models (LLMs)
- GitHub API
- Multi-agent architecture

## API Endpoints
- `POST /review/pr` – Review a GitHub pull request
- `POST /review/diff` – Review a manually provided diff
- `GET /health` – Health check

## Notes
This project focuses on code understanding and review assistance, not automated merging or decision-making, making it suitable as a developer productivity tool.
