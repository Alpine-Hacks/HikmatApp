from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders the homepage

@app.route('/login')
def login():
    return render_template('login.html')  # Renders the login page

if __name__ == '__main__':
    app.run()
