from flask import request, jsonify, Blueprint
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from ..models import User
from .. import db

auth = Blueprint("auth", __name__)

# 👤 Obtener datos del usuario autenticado
@auth.route('/api/me', methods=['GET', 'OPTIONS'])
def me():
    # Ahora la ruta GET queda protegida con jwt_required:
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify({
            "authenticated": True,
            "username": current_user['username'],
            "user_id": current_user['id']
        })

    return protected()

# 🔐 Login con JWT
@auth.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    # Aquí solo se ejecuta para POST
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={"id": user.id, "username": user.username})
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# 🧾 Registro de usuario
@auth.route('/api/register', methods=['POST', 'OPTIONS'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado correctamente"}), 201