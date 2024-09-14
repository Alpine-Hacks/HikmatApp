from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_pyfile('config.py')  # Ensure 'config.py' is in the correct directory

    # Initialize extensions
    db.init_app(app)

    # Register blueprints or routes (if any)
    from . import routes  # Import routes from routes.py (next step)
    app.register_blueprint(routes.bp)

    return app
