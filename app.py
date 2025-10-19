from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)

# Create database tables (if they don't exist)
with app.app_context():
    db.create_all()

# Import routes after app and extensions are created
import routes

if __name__ == '__main__':
    app.run(debug=True)
