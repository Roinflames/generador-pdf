from backend import create_app, db
from backend.models import User
from flask import Flask, request  # agrega request aquí

app = create_app()

@app.before_request
def before_request_func():
    if request.method == 'OPTIONS':
        return '', 200
    
with app.app_context():
    db.create_all()
    print("✅ Base de datos creada")
    
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("✅ Base de datos creada")

@app.cli.command("create-user")
def create_user():
    username = input("Usuario: ")
    password = input("Contraseña: ")
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    print("✅ Usuario creado")

if __name__ == '__main__':
    app.run(debug=True)
