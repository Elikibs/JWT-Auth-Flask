from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db, User
from auth import auth_bp
from users import user_bp

app = Flask(__name__)
app.secret_key = '4b37674a1d174146f65484bb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Initialize app with db, migrate
migrate = Migrate(app, db)
jwt = JWTManager(app)
db.init_app(app)

# register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')

# jwt error handlers
# expired token handler
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify(
        {
            "message": "Token has expired",
            "error": "token_expired"
        }
    ), 401

# invalid token loader
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify(
        {
            "message": "Signature verification failed",
            "error": "invalid_token"
        }
    ), 401

# unauthorized token loader (when token is not provided)
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify(
        {
            "message": "Request doesn't contain a valid token",
            "error": "authorization_header"
        }
    ), 401



if __name__== '__main__':
    app.run(port=5555, debug=True)