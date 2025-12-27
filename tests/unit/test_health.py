"""Unit tests for health check endpoint."""

import json
import pytest


class TestHealthEndpoint:
    """Test cases for the health check endpoint."""

    def test_get_health_returns_200_status(self, client):
        """Test that GET /health returns HTTP 200 status code."""
        response = client.get('/health')
        assert response.status_code == 200

    def test_get_health_returns_json_response(self, client):
        """Test that GET /health returns JSON response with status field."""
        response = client.get('/health')
        assert response.content_type == 'application/json'
        data = json.loads(response.data)
        assert 'status' in data

    def test_get_health_returns_ok_status(self, client):
        """Test that GET /health response body equals {"status": "ok"}."""
        response = client.get('/health')
        data = json.loads(response.data)
        assert data == {"status": "ok"}
        assert data['status'] == "ok"

    def test_post_health_returns_405(self, client):
        """Test that POST /health returns HTTP 405 Method Not Allowed."""
        response = client.post('/health')
        assert response.status_code == 405

    def test_put_health_returns_405(self, client):
        """Test that PUT /health returns HTTP 405 Method Not Allowed."""
        response = client.put('/health')
        assert response.status_code == 405

    def test_delete_health_returns_405(self, client):
        """Test that DELETE /health returns HTTP 405 Method Not Allowed."""
        response = client.delete('/health')
        assert response.status_code == 405

    def test_patch_health_returns_405(self, client):
        """Test that PATCH /health returns HTTP 405 Method Not Allowed."""
        response = client.patch('/health')
        assert response.status_code == 405
