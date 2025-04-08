from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# Ruta de la imagen generada por seqdiag
imagen_diagrama = "flowchart.png"
nombre_pdf = "business_flowchart.pdf"

# Cargar imagen para obtener dimensiones
imagen = Image.open(imagen_diagrama)
ancho, alto = imagen.size

# Crear el PDF
c = canvas.Canvas(nombre_pdf, pagesize=letter)
width, height = letter

# Opcional: título
c.setFont("Helvetica-Bold", 20)
c.drawString(100, height - 100, "Business Process")

# Insertar imagen centrada en la página
escala = 0.5  # Ajusta según el tamaño
c.drawImage(imagen_diagrama, x=100, y=height - alto * escala - 150,
            width=ancho * escala, height=alto * escala)

c.save()
print(f"PDF '{nombre_pdf}' generado con éxito.")
