from flask import jsonify, make_response, request
from . import reconocimiento
import jinja2
import pdfkit
import os

# Ruta base del módulo reconocimiento
path = os.path.dirname(__file__)
ruta_template = os.path.join(path, 'templates', 'template.html')

def crea_pdf(ruta_template, info, rutacss=''):
    template_dir = os.path.dirname(ruta_template)
    template_name = os.path.basename(ruta_template)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template(template_name)

    html = template.render(info)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': 'UTF-8'
    }

    # Configuración de wkhtmltopdf (modifica esta ruta si estás en Mac o Linux)
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Ajusta según tu sistema

    os.makedirs(os.path.join(path, 'static'), exist_ok=True)
    ruta_salida = os.path.join(path, 'static', 'reconocimiento_python.pdf')
    pdfkit.from_string(html, ruta_salida, css=rutacss, options=options, configuration=config)

    return ruta_salida

# ✅ Vista que genera PDF y lo devuelve (GET o POST si quieres personalización)
@reconocimiento.route('/api/reconocimiento/generar_pdf', methods=['GET'])
def generar_pdf():
    # Puedes luego cambiar esto para que venga desde el frontend (POST con JSON)
    info = {
        "nombreAlumno": "Fernando Cortés",
        "nombreCurso": "Introducción a Python y HTML5",
        "fecha": "2023-10-01"
    }

    ruta_template = os.path.join(path, 'templates', 'template.html')
    pdf_path = crea_pdf(ruta_template, info)

    with open(pdf_path, 'rb') as f:
        pdf = f.read()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=reconocimiento_python.pdf'

    return response

# ✅ (Opcional) Devolver HTML renderizado como string, útil para vista previa
@reconocimiento.route('/api/reconocimiento/preview', methods=['GET'])
def preview_html():
    info = {
        "nombreAlumno": "Fernando Cortés",
        "nombreCurso": "Introducción a Python y HTML5",
        "fecha": "2023-10-01"
    }

    template_dir = os.path.dirname(ruta_template)
    template_name = os.path.basename(ruta_template)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    html = template.render(info)

    return jsonify({ "html": html })
