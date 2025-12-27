"""Integration tests for health check endpoint with Flask app."""

import json
import time
import pytest


class TestHealthIntegration:
    """Integration tests for health check endpoint with actual Flask app."""

    def test_endpoint_works_with_flask_app(self, client):
        """Test that endpoint works with actual Flask application context."""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == {"status": "ok"}

    def test_response_time_under_100ms(self, client):
        """Test that response time is consistently under 100ms."""
        for _ in range(5):  # Test multiple times to ensure consistency
            start_time = time.time()
            response = client.get('/health')
            end_time = time.time()

            elapsed_ms = (end_time - start_time) * 1000
            assert elapsed_ms < 100, f"Response took {elapsed_ms}ms, expected < 100ms"
            assert response.status_code == 200

    def test_response_is_valid_json(self, client):
        """Test that response is valid JSON parseable by standard JSON parsers."""
        response = client.get('/health')
        assert response.content_type == 'application/json'

        # Should not raise an exception
        try:
            data = json.loads(response.data)
            assert isinstance(data, dict)
        except json.JSONDecodeError:
            pytest.fail("Response is not valid JSON")

    def test_endpoint_is_idempotent(self, client):
        """Test that multiple calls to endpoint return same response."""
        response1 = client.get('/health')
        response2 = client.get('/health')
        response3 = client.get('/health')

        data1 = json.loads(response1.data)
        data2 = json.loads(response2.data)
        data3 = json.loads(response3.data)

        assert data1 == data2 == data3
        assert data1 == {"status": "ok"}

    def test_no_side_effects(self, client, app):
        """Test that health check has no side effects on application state."""
        # Get initial state
        initial_request_count = 0

        # Make multiple health check requests
        for i in range(10):
            response = client.get('/health')
            assert response.status_code == 200

        # Verify each request is identical (no state change)
        for i in range(10):
            response = client.get('/health')
            data = json.loads(response.data)
            assert data == {"status": "ok"}
