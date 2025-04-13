from flask import Blueprint

diagrama_bp = Blueprint('diagrama', __name__, template_folder='templates')

from . import routes