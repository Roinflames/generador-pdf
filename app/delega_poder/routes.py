from flask import jsonify, make_response
from . import delega_bp
import jinja2
import os
import pdfkit

# Directorio base del módulo
path = os.path.dirname(__file__)
pdf_dir = os.path.join(path, 'static', 'pdfs')
template_path = os.path.join(path, 'templates', 'delega_poder.html')

# Asegura que el directorio de salida exista
os.makedirs(pdf_dir, exist_ok=True)

# Datos de ejemplo (puedes reemplazar por request.json en POST si quieres personalizar)
def get_data():
    return {
        "tribunal": "S.J.L. En lo Civil de Santiago (25º)",
        "abogado_patrocinante": "EDUARDO MAURICIO LARA QUIROZ",
        "caratula": "“TORRES/BANCO DE CHILE”",
        "rol": "Rol C-7440-2024",
        "demandado": "BASTIÁN ADONIS RAMÍREZ ROCHA",
        "rut_demandado": "19.499.895-3",
    }

# ✅ Vista previa (HTML renderizado como string para React)
@delega_bp.route('/api/delega_poder/preview')
def delega_poder_preview():
    data = get_data()
    template_dir = os.path.dirname(template_path)
    template_name = os.path.basename(template_path)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    html = template.render(data)

    return jsonify({"html": html})

# ✅ Generación de PDF desde React
@delega_bp.route('/api/delega_poder/generar_pdf')
def generar_pdf():
    data = get_data()
    template_dir = os.path.dirname(template_path)
    template_name = os.path.basename(template_path)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    html_contenido = template.render(data)

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    }

    pdf_path = os.path.join(pdf_dir, 'delega_poder.pdf')

    if os.path.exists(pdf_path):
        os.remove(pdf_path)

    # Cambia esta ruta si estás en Mac o Linux
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_string(html_contenido, pdf_path, options=options, configuration=config)

    with open(pdf_path, 'rb') as f:
        pdf = f.read()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=delega_poder.pdf'
    return response
