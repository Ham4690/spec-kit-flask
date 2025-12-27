"""Flask application entry point for development and production."""

from src import create_app

# Create the Flask app instance for 'flask run' discovery
app = create_app()
