from flask import render_template
from . import diagrama_bp

@diagrama_bp.route('/diagrama')
def diagrama_view():
    # return render_template('diagrama.html')
    return "Es construcción"
