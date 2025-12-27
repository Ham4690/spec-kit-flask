"""Health check endpoint blueprint.

This module provides a lightweight health check endpoint for monitoring service
availability. The endpoint returns a simple JSON response indicating the service
is operational, with no database connections or external API calls to ensure
fast response times (< 100ms).
"""

from flask import Blueprint, jsonify

# Create the health check blueprint
health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def get_health():
    """
    Health check endpoint.

    Returns the current health status of the service. This endpoint is optimized
    for monitoring systems and load balancers and has no external dependencies.

    Returns:
        tuple: JSON response with status code 200 indicating service is healthy.
               Response body: {"status": "ok"}

    Performance:
        - Response time: < 1ms (no I/O operations)
        - No database connections
        - No external API calls
        - Suitable for high-frequency health check polling
    """
    return jsonify({"status": "ok"})
