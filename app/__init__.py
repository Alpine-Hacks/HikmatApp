from flask import Flask
from app.routes.course import course_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(course_bp, url_prefix='/course')

    return app

app = create_app()
