import jinja2
import pdfkit

def crea_pdf(ruta_template, info, rutacss=''):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template, '')

    print(nombre_template)
    print(ruta_template)

if __name__ == "__main__":
    ruta_template = 'C:\\Users\\rodre\\source\\repos\\generador-pdf\\template.html'
    info = {}
    crea_pdf(ruta_template, info)
