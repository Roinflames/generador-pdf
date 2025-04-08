import graphviz
import pdfkit

# 1. Create the flowchart using graphviz
dot = graphviz.Digraph(comment='Business Flowchart')

# Add nodes
dot.node('A', 'Start')
dot.node('B', 'Process 1')
dot.node('C', 'Process 2')
dot.node('D', 'Decision')
dot.node('E', 'End')

# Add edges
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E', label='Yes')
dot.edge('D', 'B', label='No')

# Save the graph to a file (e.g., PNG)
image_path = 'flowchart.png'
dot.render(filename='flowchart', format='png', view=False)

# 2. Create an HTML structure
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Business Flowchart</title>
</head>
<body>
    <h1>Business Process</h1>
    <img src="{image_path}" alt="Business Flowchart">
    <p>This document shows the business process flow...</p>
</body>
</html>
"""

options = {
    'page-size': 'Letter',
    'encoding': 'UTF-8',
    'enable-local-file-access': None # TODO averiguar esta línea
}

# 3. Use pdfkit to convert HTML to PDF
try:
    pdfkit.from_string(html_content, 'business_flowchart.pdf', options=options)
    print("PDF 'business_flowchart.pdf' created successfully.")
except OSError as e:
    print(f"Error creating PDF: {e}")
    print("Please ensure that wkhtmltopdf is installed and in your system's PATH.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")