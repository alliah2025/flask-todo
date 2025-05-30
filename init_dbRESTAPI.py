##needed to run the flask app
from app_withRESTAPI import db, app
with app.app_context():
    db.create_all()
    print("Database initialized.")