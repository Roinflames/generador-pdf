import pdfkit
import jinja2
import json
from datetime import datetime

# Cargar datos de ejemplo desde el archivo JSON
with open('datos_contactos.json', encoding='utf-8') as f:
    contactos = json.load(f)

# Configurar el entorno Jinja2 y cargar la plantilla
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
# template = env.get_template('template_contactos.html')
# Informe 1
# template = env.get_template('contactos.html')
# informe 2
# template = env.get_template('informe2.html')
# informe 3
template = env.get_template('chart.html')

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