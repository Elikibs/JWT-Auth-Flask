from flask import Flask

app = Flask(__name__)
app.secret_key = 'b33b151adaccb5d08c9eb0c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fleets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# app initializing with db
db.init_app(app)