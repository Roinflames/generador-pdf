from flask import render_template, make_response, redirect, url_for
from . import opone_excepciones_bp
import pdfkit
import os
import json

@opone_excepciones_bp.route('/')
def opone_excepciones_view():
    # TODO: obtener los datos necesarios para la vista a través de JSON
    # Ruta absoluta al archivo JSON
    json_path = os.path.join(opone_excepciones_bp.root_path, 'static', 'data', 'opone_excepciones_data.json')
    # Leer archivo JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('opone_excepciones_preview.html', **data)

@opone_excepciones_bp.route('/generar_pdf')
def generar_pdf():
    # Ruta absoluta al archivo JSON
    json_path = os.path.join(opone_excepciones_bp.root_path, 'static', 'data', 'opone_excepciones_data.json')
    # Leer archivo JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Renderizar la plantilla para el PDF
    html = render_template('opone_excepciones.html', **data)
    pdf = pdfkit.from_string(html, False)
    # TODO filename=opone_excepciones con nomenclatura de la causa
    # Generar el PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=opone_excepciones.pdf'
    return response