import graphviz
import pdfkit
import os

# 1. Create the flowchart using graphviz
dot = graphviz.Digraph(comment='Business Flowchart')

# Crear grafo horizontal
dot.attr(rankdir='LR')  # Horizontal
# Estilo general
dot.attr('node', shape='plaintext')

# Nodos con etiquetas HTML
dot.node('A', '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" BGCOLOR="lightgreen">
        <TR><TD><B>Paso 1</B></TD></TR>
        <TR><TD>Inicio del proceso</TD></TR>
    </TABLE>>''')

dot.node('B', '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" BGCOLOR="lightblue">
        <TR><TD><B>Paso 2</B></TD></TR>
        <TR><TD>Validación inicial</TD></TR>
    </TABLE>>''')

dot.node('C', '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" BGCOLOR="lightyellow">
        <TR><TD><B>Paso 3</B></TD></TR>
        <TR><TD>Procesamiento de datos</TD></TR>
    </TABLE>>''')

dot.node('D', '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" BGCOLOR="orange">
        <TR><TD><B>Paso 4</B></TD></TR>
        <TR><TD>Verificación</TD></TR>
    </TABLE>>''')

dot.node('E', '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" BGCOLOR="lightcoral">
        <TR><TD><B>Paso 5</B></TD></TR>
        <TR><TD>Finalización</TD></TR>
    </TABLE>>''')

# Conectar nodos secuencialmente
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')

# 2. Renderizar el PNG
image_path = os.path.abspath('flowchart.png')
dot.render(filename='flowchart', format='png', view=False)

# Agregar firma
firma_path = os.path.abspath('firma.jpg')
# 3. Create an HTML structure
# El prefijo file:/// es obligatorio para que wkhtmltopdf entienda que es un archivo local.

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Business Flowchart</title>
</head>
<body>
    <img src="file:///{firma_path}" alt="Firma Alfaro Madariaga" width="200">

    <h1>Business Process</h1>
    <img src="file:///{image_path}" alt="Business Flowchart" width="600"><br>
    
    <p>This document shows the business process flow...</p>

</body>
</html>
"""


options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
    'enable-local-file-access': None # TODO averiguar esta línea
    # Habilitar acceso a archivos locales (ya lo hiciste correctamente)
}

# 4. Use pdfkit to convert HTML to PDF
try:
    pdfkit.from_string(html_content, 'business_flowchart.pdf', options=options)
    print("PDF 'business_flowchart.pdf' created successfully.")
except OSError as e:
    print(f"Error creating PDF: {e}")
    print("Please ensure that wkhtmltopdf is installed and in your system's PATH.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")