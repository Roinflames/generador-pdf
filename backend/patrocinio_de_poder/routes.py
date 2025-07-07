# en routes.py o el archivo de rutas correspondiente
from flask import render_template, make_response, redirect, url_for
from . import patrocinio_de_poder_bp
import os
import pdfkit
import json

# Directorio donde guardar el archivo temporal
pdf_dir = os.path.join(os.path.dirname(__file__), 'static', 'pdfs')
os.makedirs(pdf_dir, exist_ok=True)

# Ruta para mostrar la vista previa
@patrocinio_de_poder_bp.route('/')
def preview():
    json_path = os.path.join(patrocinio_de_poder_bp.root_path, 'static', 'data', 'patrocinio_de_poder_data.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Renderiza la plantilla 'patrocinio_de_poder.html' con los datos
    return render_template('patrocinio_de_poder_preview.html', **data)

# Ruta para generar el PDF
@patrocinio_de_poder_bp.route('/generar_pdf')
def generar_pdf():
    json_path = os.path.join(patrocinio_de_poder_bp.root_path, 'static', 'data', 'patrocinio_de_poder_data.json')

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Renderiza la plantilla 'patrocinio_de_poder.html' con los datos
    html_contenido = render_template('patrocinio_de_poder.html', **data)

    # Opciones para pdfkit (como tamaño de página, etc.)
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': None  # Esto es para permitir que pdfkit acceda a archivos locales si es necesario
    }

    # Ruta del archivo PDF
    pdf_path = os.path.join(pdf_dir, 'patrocinio_de_poder.pdf')

    # Elimina el archivo PDF anterior si ya existe
    if os.path.exists(pdf_path):
        os.remove(pdf_path)

    # Genera el PDF desde el contenido HTML renderizado
    pdfkit.from_string(html_contenido, pdf_path, options=options)

    # Abre el archivo PDF y lee su contenido en binario
    with open(pdf_path, 'rb') as f:
        pdf = f.read()

    # Crear la respuesta PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=patrocinio_de_poder.pdf'

    return response