from app.routes.course import course_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(course_bp, url_prefix='/course')
    return app
