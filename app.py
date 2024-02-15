from flask import Flask
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)
app.secret_key = 'b33b151adaccb5d08c9eb0c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Initialize app with db, migrate
migrate = Migrate(app, db)
db.init_app(app)