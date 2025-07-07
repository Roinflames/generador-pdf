from flask import Blueprint

delega_bp = Blueprint('patrocinio_de_poder', __name__, template_folder='templates')

from . import routes