##needed to run the flask app
from app import app, db

with app.app_context():
    db.create_all()
    print("Database initialized.")

