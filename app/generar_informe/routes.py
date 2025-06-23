from flask import render_template, make_response, redirect, url_for
from . import generar_informe
import pdfkit
import jinja2
import json
from datetime import datetime
import os

# Obtener el directorio actual y construir la ruta del archivo JSON
current_dir = os.path.dirname(__file__)  # Directorio actual
file_path = os.path.join(current_dir, 'static', 'data', 'datos_contactos.json')  # Ubicación del archivo JSON

# Cargar datos de ejemplo desde el archivo JSON
with open(file_path, encoding='utf-8') as f:
    contactos = json.load(f)

# Configurar el entorno Jinja2, con la ruta correcta de las plantillas dentro del blueprint
env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(current_dir, 'templates')))

@generar_informe.route('/')
def generar_informe_view():
    # Renderizar la vista previa del informe con los datos
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    tipo_informe = 2  # Cambia esto según el informe que quieras generar

    # json_path = os.path.join(generar_informe.root_path, 'static', 'data', 'datos_contactos.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        contactos_data = json.load(f)
    
    contactos = contactos_data.get("contactos", [])

    if tipo_informe == 1:
        template = env.get_template('template_contactos.html')  # Tabla de contactos
    elif tipo_informe == 2:
        template = env.get_template('generar_informe.html')  # Tabla con texto extenso
    elif tipo_informe == 3:
        template = env.get_template('chart.html')  # Gráfico de contactos no funcional
    else:
        raise ValueError("Tipo de informe no válido. Debe ser 1, 2 o 3.")

    # Renderizar HTML con datos de contactos y fecha actual
    html_renderizado = template.render(fecha=fecha_actual, contactos=contactos)
    
    # Devolver la vista previa renderizada en HTML
    return render_template('generar_informe_preview.html', contenido=html_renderizado)

@generar_informe.route('/generar_pdf')
def generar_pdf():
    # Cargar los datos y preparar la plantilla para el PDF
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    tipo_informe = 2  # Cambia esto según el informe que quieras generar

    if tipo_informe == 1:
        template = env.get_template('template_contactos.html')  # Tabla de contactos
    elif tipo_informe == 2:
        template = env.get_template('generar_informe.html')  # Tabla con texto extenso
    elif tipo_informe == 3:
        template = env.get_template('chart.html')  # Gráfico de contactos no funcional
    else:
        raise ValueError("Tipo de informe no válido. Debe ser 1, 2 o 3.")

    # Renderizar HTML con datos
    html_renderizado = template.render(fecha=fecha_actual, contactos=contactos)

    # Opciones para pdfkit
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': None  # Permite acceder a archivos locales en la plantilla
    }

    # GenerarPDF a partir del HTML renderizado
    pdf = pdfkit.from_string(html_renderizado, False, options=options)

    # Crear la respuesta PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=informe_contactos.pdf'

    return response
