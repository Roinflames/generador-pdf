from flask import request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User
from .. import db

# Registro de usuario
@auth.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar los datos en formato JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Usuario y contraseña requeridos"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado correctamente"}), 201

# Inicio de sesiónx||
@auth.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar los datos en formato JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Usuario y contraseña requeridos"}), 400

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    login_user(user)
    return jsonify({"message": "Inicio de sesión exitoso", "username": user.username}), 200

# Cierre de sesión
@auth.route('/api/logout', methods=['POST'])
@login_required
def api_logout():
    logout_user()
    return jsonify({"message": "Sesión cerrada correctamente"}), 200

# Verificar si el usuario está autenticado
@auth.route('/api/session', methods=['GET'])
def api_session():
    if current_user.is_authenticated:
        return jsonify({
            "authenticated": True,
            "username": current_user.username
        })
    else:
        return jsonify({"authenticated": False}), 200
