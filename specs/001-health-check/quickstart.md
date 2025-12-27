# Quick Start Guide: Simple Health Check API Endpoint

**Feature**: 001-health-check
**Date**: 2025-12-27

## Setup

### Prerequisites
- Python 3.10+
- Flask 3.1
- pytest 8.4
- uv (package manager, per constitution)

### Initial Setup

```bash
# Install dependencies (handled by project setup)
uv pip install flask pytest

# Navigate to project root
cd /Users/arhigash/workspace/study/python/spec-kit-flask
```

## Running the Application

### Start the Flask Server

```bash
# Using uv as specified in constitution
uv run flask run

# Server will start on localhost:8080
```

### Test the Endpoint

```bash
# Using curl
curl http://localhost:8080/health

# Expected response:
# {"status": "ok"}

# Using Python requests
python -c "import requests; r = requests.get('http://localhost:8080/health'); print(r.json())"
```

## Running Tests

### All Tests

```bash
# Run all tests
uv run pytest tests/

# Run with verbose output
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=src --cov-report=term-missing
```

### Unit Tests Only

```bash
uv run pytest tests/unit/test_health.py -v
```

### Integration Tests Only

```bash
uv run pytest tests/integration/test_health_integration.py -v
```

## Feature Verification Checklist

- [ ] Flask app starts without errors
- [ ] GET /health returns HTTP 200
- [ ] Response is valid JSON: `{"status": "ok"}`
- [ ] POST /health returns HTTP 405
- [ ] PUT /health returns HTTP 405
- [ ] DELETE /health returns HTTP 405
- [ ] Response time is under 100ms
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Code includes docstrings and comments explaining logic
- [ ] No database connections or external API calls made

## Files Modified/Created

### Source Code
- `src/__init__.py` - Flask app factory with blueprint registration
- `src/blueprints/__init__.py` - Blueprint module initialization
- `src/blueprints/health.py` - Health check endpoint implementation

### Tests
- `tests/__init__.py` - Tests package initialization
- `tests/unit/__init__.py` - Unit tests package
- `tests/unit/test_health.py` - Unit tests for health endpoint
- `tests/integration/__init__.py` - Integration tests package
- `tests/integration/test_health_integration.py` - Integration tests with Flask app

## Troubleshooting

### Endpoint not responding
- Ensure Flask server is running (`uv run flask run`)
- Check that server is listening on localhost:8080
- Verify URL path is `/health` (case-sensitive)

### Tests failing
- Ensure pytest is installed: `uv run pytest --version`
- Check that Flask app factory is properly configured
- Verify test fixtures have correct Flask app context

### JSON response format issues
- Verify Flask `jsonify()` is being used
- Check that response includes `"status": "ok"` field
- Validate response Content-Type is `application/json`

## Next Steps

After implementation:
1. Create integration with application startup/health monitoring system
2. Add metrics collection (response times, request counts)
3. Extend to include additional service checks if needed
4. Document in API documentation/OpenAPI spec
