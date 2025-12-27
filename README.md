# spec-kit-flask

A Flask-based API application with a simple health check endpoint.

## Overview

This project implements a lightweight health check API endpoint (`GET /health`) that returns a simple JSON response indicating service availability. The endpoint is optimized for use with monitoring systems, load balancers, and container orchestration platforms.

## Features

- **Health Check Endpoint**: `GET /health` returns `{"status": "ok"}`
- **No I/O Dependencies**: Fast response time (< 100ms) with no database or external API calls
- **Test-Driven Development**: Comprehensive unit and integration tests
- **Flask Blueprint Architecture**: Modular, scalable endpoint organization

## Requirements

- Python 3.10+
- Flask 3.1
- pytest 8.4
- uv (package manager)

## Setup

### Install Dependencies

```bash
uv sync
```

### Create Virtual Environment

The virtual environment is automatically created by `uv` when running commands.

## Running the Application

### Start the Flask Development Server

```bash
uv run flask run
```

The server will start on `http://localhost:8080`

### Test the Health Endpoint

```bash
# Using curl
curl http://localhost:8080/health

# Expected response:
# {"status":"ok"}

# Using Python
python -c "import requests; print(requests.get('http://localhost:8080/health').json())"
```

## Testing

### Run All Tests

```bash
uv run pytest tests/ -v
```

### Run Unit Tests Only

```bash
uv run pytest tests/unit/ -v
```

### Run Integration Tests Only

```bash
uv run pytest tests/integration/ -v
```

### Run Tests with Coverage

```bash
uv run pytest tests/ --cov=src --cov-report=html
```

## Project Structure

```
.
├── src/
│   ├── __init__.py           # Flask app factory
│   └── blueprints/
│       ├── __init__.py       # Blueprints package
│       └── health.py         # Health check endpoint
├── tests/
│   ├── conftest.py           # Pytest fixtures
│   ├── unit/
│   │   └── test_health.py    # Unit tests
│   └── integration/
│       └── test_health_integration.py  # Integration tests
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

## API Documentation

### Health Check Endpoint

**Endpoint**: `GET /health`

**Response** (200 OK):
```json
{
  "status": "ok"
}
```

**Error Responses**:
- `405 Method Not Allowed`: For non-GET requests (POST, PUT, DELETE, PATCH)

## Development

### Running Tests During Development

```bash
# Watch mode (if using pytest-watch)
uv run pytest-watch tests/

# Run specific test file
uv run pytest tests/unit/test_health.py -v

# Run specific test
uv run pytest tests/unit/test_health.py::TestHealthEndpoint::test_get_health_returns_200_status -v
```

### Code Style

This project follows PEP 8 guidelines. Use:

```bash
# Format code (if using black)
uv run black src/ tests/

# Lint code (if using flake8)
uv run flake8 src/ tests/
```

## Performance

- Response time: < 100ms (typically < 1ms)
- No database queries
- No external API calls
- Suitable for high-frequency health check polling

## License

MIT
