from flask import render_template
from . import reconocimiento

@reconocimiento.route('/reconocimiento')
def reconocimiento_view():
    return render_template('templates/template.html')
