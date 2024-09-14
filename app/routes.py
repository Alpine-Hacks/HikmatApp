from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')  # Renders the homepage

@bp.route('/login')
def login():
    return render_template('login.html')  # Renders the login page

@bp.route('/signup')
def signup():
    return render_template('signup.html')  # Renders the signup page
