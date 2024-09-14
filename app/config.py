import os

# Go one level up from the 'app' directory to get the project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Construct the path to the database file
db_path = os.path.join(BASE_DIR, 'database', 'hikmat.db')

# Ensure the path uses forward slashes for the SQLite URI
SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path.replace(os.sep, '/')}"

SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional, disables modification tracking

print(SQLALCHEMY_DATABASE_URI)
