#!/bin/bash

echo "Setting up HikmatApp..."

# Install dependencies
pip install -r setup/requirements.txt

# Initialize the database
python -c "from app import create_app; app = create_app(); with app.app_context(): from app.extensions import db; db.create_all()"

echo "Setup complete. Run 'python app/app.py' to start the server."
