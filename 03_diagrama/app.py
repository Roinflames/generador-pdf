from seqdiag import parser, builder, drawer

# Definir el diagrama en formato de texto
diagram_definition = """
seqdiag {
    Cliente -> Servidor [label = "Solicitud"];
    Servidor -> Cliente [label = "Respuesta"];
}
"""

# Analizar el texto y construir el diagrama
tree = parser.parse_string(diagram_definition)
diagram = builder.ScreenNodeBuilder.build(tree)

# Dibujar el diagrama y guardarlo como imagen PNG
draw = drawer.DiagramDraw('PNG', diagram)
draw.draw()
draw.save("diagrama_secuencia.png")
