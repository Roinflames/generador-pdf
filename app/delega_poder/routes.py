from flask import render_template
from . import delega_bp

@delega_bp.route('/delega_poder')
def delega_poder_view():
    return render_template('templates/template.html')
