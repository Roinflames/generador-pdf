from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .. import db
from .forms import LoginForm 

@auth.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)

    # POST
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify({"message": "Login exitoso", "user_id": user.id})
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@auth.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Sesión cerrada"})

@auth.route('/api/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    # POST
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "El nombre de usuario ya existe"}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado correctamente"})
