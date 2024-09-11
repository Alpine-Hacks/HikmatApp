from flask import Blueprint

course_bp = Blueprint('course', __name__)

@course_bp.route('/')
def home():
    return "Course Home"
