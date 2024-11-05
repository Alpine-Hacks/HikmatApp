from .models import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Adjust path as needed
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    db.init_app(app)
    login_manager.init_app(app)

    # Register your blueprints here, e.g., routes
    from .routes import main
    app.register_blueprint(main)

    return app
