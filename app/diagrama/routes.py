from flask import render_template, make_response, redirect, url_for
from . import diagrama_bp
import graphviz
import pdfkit
import os
from pathlib import Path

# Directorio donde guardar el archivo temporal
pdf_dir = os.path.join(os.path.dirname(__file__), 'static', 'pdfs')
image_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
image_path = os.path.join(image_dir, 'flowchart.png')
firma_path = os.path.join(image_dir, 'firma.jpg')
firma_uri = Path(firma_path).as_uri()
image_uri = Path(image_path).as_uri()
print(firma_uri)

os.makedirs(pdf_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)

# Ruta para visualizar el diagrama (vista previa)
@diagrama_bp.route('/diagrama')
def diagrama_view():
    # Crear el diagrama de flujo con graphviz
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

    # Generar el archivo de imagen del diagrama
    image_filename = 'flowchart.png'
    firma_filename = 'firma.jpg'
    # image_path = os.path.join(image_dir, image_filename)
    
    # image_url = url_for('static', filename=f'images/{image_filename}')
    # firma_url = url_for('static', filename=f'images/{firma_filename}')
    image_url = url_for('diagrama.static', filename=f'images/{image_filename}')
    firma_url = url_for('diagrama.static', filename=f'images/{firma_filename}')

    dot.render(filename=os.path.join(image_dir, 'flowchart'), format='png', cleanup=True)

    # return render_template('diagrama_preview.html', image_path=image_path)
    return render_template('diagrama_preview.html', image_url=image_url, firma_url=firma_url)

@diagrama_bp.route('/generar_pdf_diagrama')
def generar_pdf_diagrama():

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Business Flowchart</title></head>
    <body>
        <img src="{firma_uri}" alt="Firma Alfaro Madariaga" width="200">
        <h1>Business Process</h1>
        <img src="{image_uri}" alt="Business Flowchart" width="600"><br>
        <p>This document shows the business process flow...</p>
    </body>
    </html>
    """
    pdf_path = os.path.join(pdf_dir, 'diagrama_flujo.pdf')
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    }

    try:
        pdf = pdfkit.from_string(html_content, pdf_path, options=options)
        # return send_file(pdf_path, as_attachment=True)
    
        # Crear la respuesta PDF
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=informe_contactos.pdf'
    except Exception as e:
        return f"Error generando PDF: {str(e)}"

