from flask import render_template, make_response, redirect, url_for
from . import escritura_bp
import pdfkit
import os
import json

@escritura_bp.route('/escritura_compraventa')
def escritura_compraventa_view():
    json_path = os.path.join(escritura_bp.root_path, 'static', 'data', 'escritura_compraventa_data.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Renderizar la plantilla para vista previa en HTML
    return render_template('plantilla_compraventa_preview.html', **data)

@escritura_bp.route('/generar_pdf')
def generar_pdf():
    json_path = os.path.join(escritura_bp.root_path, 'static', 'data', 'escritura_compraventa_data.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Renderizar la plantilla para el PDF
    html = render_template('plantilla_compraventa.html', **data)
    pdf = pdfkit.from_string(html, False)

    # Generar el PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=escritura_compraventa.pdf'

    return response