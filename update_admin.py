from app import app, db
from models import User

with app.app_context():
    user = User.query.filter_by(email='kabirkapur25@gmail.com').first()
    if user:
        user.role = 'admin'
        db.session.commit()
        print("User role updated to admin.")
    else:
        print("User not found.")
