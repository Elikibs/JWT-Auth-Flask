from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import User
from schemas import UserSchema

user_bp = Blueprint('users', __name__)

@user_bp.get('/all')
@jwt_required()
def get_all_users():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=3, type=int)

    users = User.query.paginate(
        page = page,
        per_page = per_page
    )
    
    response = UserSchema().dump(users, many=True)

    return jsonify(response), 200