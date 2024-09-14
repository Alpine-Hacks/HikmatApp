from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # This creates all the tables defined in your models
    print("Database initialized successfully.")
