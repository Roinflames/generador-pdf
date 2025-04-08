import pdfkit
from jinja2 import Environment, FileSystemLoader

# Configurar el entorno de Jinja2
env = Environment(loader=FileSystemLoader('.'))

# Cargar la plantilla
template = env.get_template('plantilla_compraventa.html')

# Definir los valores de las variables
data = {
    "ciudad": "Santiago",
    "dia": "7",
    "mes": "abril",
    "anio": "2025",
    "notario": "Juan Pérez",
    "vendedor_nombre": "Rodrigo Reyes",
    "vendedor_rut": "12.345.678-9",
    "vendedor_domicilio": "Av. Libertador Bernardo O'Higgins 1234",
    "comprador_nombre": "Diego López",
    "comprador_rut": "23.456.789-0",
    "comprador_domicilio": "Calle Ficticia 5678",
    "inmueble_direccion": "Av. Providencia 2500",
    "inmueble_descripcion": "Departamento de 2 dormitorios, 1 baño",
    "precio_venta": "50.000.000",
    "precio_venta_numero": "50000000",
    "metodo_pago": "Transferencia bancaria",
    "declaraciones_adicionales": "El bien se entrega libre de cargas y gravámenes."
}

# Renderizar la plantilla con los datos
html_contenido = template.render(data)

# Generar el PDF
pdfkit.from_string(html_contenido, 'escritura_compraventa.pdf')
