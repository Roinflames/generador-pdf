import pdfkit
from jinja2 import Environment, FileSystemLoader
import json

# Cargar datos de ejemplo desde el archivo JSON
# with open('datos.json', encoding='utf-8') as f:
#     contactos = json.load(f)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

    
data = {
    "tribunal": "S.J.L. En lo Civil de Santiago (25º)",
    "abogado_patrocinante": f"EDUARDO MAURICIO LARA QUIROZ",
    "caratula": "“TORRES/BANCO DE CHILE”",
    "rol": "Rol C-7440-2024",
    "demandado": f"BASTIÁN ADONIS RAMÍREZ ROCHA",
    "rut_demandado": "19.499.895-3",
}

options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
    'enable-local-file-access': None # TODO averiguar esta línea
}

html_contenido = template.render(data)

pdfkit.from_string(html_contenido, 'delega_poder.pdf', options=options)

