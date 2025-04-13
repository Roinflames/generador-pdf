from flask import render_template
from . import escritura_bp

@escritura_bp.route('/escritura_compraventa')
def escritura_compraventa_view():
    return render_template('plantilla_compraventa.html')
