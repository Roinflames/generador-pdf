from flask import render_template, make_response, redirect, url_for
from . import reconocimiento
import jinja2
import pdfkit
import os

# Determina la ruta del template dependiendo de si estás en un PC o notebook
machine = 'PC'  # Cambia a 'notebook' si estás en el notebook

if machine == 'notebook':
    path = 'C:/Users/rodre/source/repos/generador-pdf/01_reconocimiento/'
else:
    path = 'C:/Users/Rodrigo/Documents/Code/generador-pdf/01_reconocimiento/'

# Función para crear el PDF
def crea_pdf(ruta_template, info, rutacss=''):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': 'UTF-8'
    }

    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    # Ruta de salida del archivo PDF
    ruta_salida = path + 'reconocimiento_python.pdf'

    # Genera el PDF desde el HTML renderizado
    pdfkit.from_string(html, ruta_salida, css=rutacss, options=options, configuration=config)

    return ruta_salida  # Regresa la ruta del archivo PDF generado

# Vista de Flask para mostrar el formulario o template de reconocimiento
@reconocimiento.route('/reconocimiento')
def reconocimiento_view():
    return render_template('template.html')

# Ruta para vista previa del reconocimiento (no genera PDF, solo muestra la plantilla)
@reconocimiento.route('/reconocimiento_preview')
def reconocimiento_preview():
    # Define la información a pasar a la plantilla
    info = {
        "nombreAlumno": "Fernando Cortés",
        "nombreCurso": "Introducción a Python y HTML5",
        "fecha": "2023-10-01"
    }

    # Define la ruta de la plantilla
    ruta_template = path + 'template.html'

    # Renderiza la plantilla de reconocimiento para vista previa
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))
    template = env.get_template('template.html')
    html = template.render(info)

    # Devuelve el HTML renderizado como una vista previa en la página
    return render_template('reconocimiento_preview.html', contenido=html)

# Ruta para generar el PDF y devolverlo en la respuesta
@reconocimiento.route('/generar_pdf')
def generar_pdf():
    # Define la información a pasar a la plantilla
    info = {
        "nombreAlumno": "Fernando Cortés",
        "nombreCurso": "Introducción a Python y HTML5",
        "fecha": "2023-10-01"
    }

    # Define la ruta de la plantilla
    ruta_template = path + 'template.html'

    # Llama a la función para crear el PDF
    pdf_path = crea_pdf(ruta_template, info)

    # Lee el PDF generado
    with open(pdf_path, 'rb') as f:
        pdf = f.read()

    # Devuelve el archivo PDF como respuesta en la aplicación Flask
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=reconocimiento_python.pdf'

    return response