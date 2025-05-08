from flask import Blueprint

opone_excepciones_bp = Blueprint('opone_excepciones', __name__, template_folder='templates')

from . import routes
