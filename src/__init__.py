"""Flask application factory for health check API."""

from flask import Flask


def create_app(config=None):
    """
    Create and configure the Flask application.

    Args:
        config: Optional configuration dictionary for the app

    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)

    # Apply configuration if provided
    if config:
        app.config.update(config)

    # Register blueprints
    from src.blueprints.health import health_bp
    app.register_blueprint(health_bp)

    return app
