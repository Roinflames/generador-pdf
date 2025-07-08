from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager  # 👈 nuevo import

db = SQLAlchemy()
login_manager = LoginManager()
jwt = JWTManager()  # 👈 instancia global

from backend.models import User  # asegúrate que la ruta sea correcta

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.secret_key = 'tu_clave_secreta'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # opcional pero recomendado

    app.config['JWT_SECRET_KEY'] = 'clave-jwt-segura-123'  # 🔐 usa algo más fuerte en prod
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_COOKIE_SECURE'] = False  # True solo en producción HTTPS

    # CORS
    CORS(
        app,
        origins=["http://localhost:5173"],
        supports_credentials=False,  # porque no usas cookies
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"]
    )

    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)  # 👈 inicializa JWT

    # Registrar blueprints
    from .auth.routes import auth as auth_bp
    from .main import main as main_bp
    from .reconocimiento import reconocimiento as reconocimiento_bp
    from .generar_informe import generar_informe as informe_bp
    from .diagrama import diagrama_bp as diagrama_bp
    from .escritura_compraventa import escritura_bp as escritura_bp
    from .liquidacion_de_persona_natural import liquidacion_bp as liquidacion_bp
    from .delega_poder import delega_bp as delega_bp
    from .opone_excepciones import opone_excepciones_bp as opone_excepciones_bp
    from .patrocinio_de_poder import patrocinio_de_poder_bp as patrocinio_de_poder_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(reconocimiento_bp, url_prefix='/reconocimiento')
    app.register_blueprint(informe_bp, url_prefix='/generar_informe')
    app.register_blueprint(diagrama_bp, url_prefix='/diagrama')
    app.register_blueprint(escritura_bp, url_prefix='/escritura_compraventa')
    app.register_blueprint(liquidacion_bp, url_prefix='/liquidacion_de_persona_natural')
    app.register_blueprint(delega_bp, url_prefix='/delega_poder')
    app.register_blueprint(opone_excepciones_bp, url_prefix='/opone_excepciones')
    app.register_blueprint(patrocinio_de_poder_bp, url_prefix='/patrocinio_de_poder')
    
    # Si necesitas ver las rutas registradas, puedes descomentar la siguiente línea
    # print(app.url_map)
    
    return app