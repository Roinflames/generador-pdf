from flask import render_template
from . import generar_informe 

@generar_informe.route('/generar_informe')
def generar_informe_view():
    return render_template('templates/template.html')
