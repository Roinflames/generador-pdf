import pdfkit
import jinja2
import json
from datetime import datetime

# Cargar datos de ejemplo desde el archivo JSON
with open('datos_contactos.json', encoding='utf-8') as f:
    contactos = json.load(f)

# Configurar el entorno Jinja2 y cargar la plantilla
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

tipo_informe = 2  # Cambia esto según el informe que quieras generar

if tipo_informe == 1:
    template = env.get_template('template_contactos.html') #tabla contactos
elif tipo_informe == 2:
    template = env.get_template('contactos.html') #tabla contactos con texto extenso
elif tipo_informe == 3:
    template = env.get_template('chart.html') # gráfico de contactos no funcional
else:
    raise ValueError("Tipo de informe no válido. Debe ser 1, 2 o 3.")

# Renderizar el HTML con los datos y la fecha actual
fecha_actual = datetime.now().strftime('%Y-%m-%d')
html_renderizado = template.render(fecha=fecha_actual, contactos=contactos)

# Opciones para pdfkit (asegúrate de que wkhtmltopdf esté instalado)
options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
    'enable-local-file-access': None # TODO averiguar esta línea
}

# Generar el PDF a partir del HTML renderizado
pdfkit.from_string(html_renderizado, 'informe_contactos.pdf', options=options)