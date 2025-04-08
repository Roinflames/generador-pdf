import pdfkit

# Plantilla de texto de la escritura
escritura_texto = """
    **ESCRITURA DE COMPRAVENTA**
    
    En [Ciudad], a [día] de [mes] de [año], ante mí, [Nombre del Notario], Notario Público de [Ciudad], comparecen:
    
    **Vendedor:**
    Nombre completo: [Nombre del Vendedor]  
    RUT: [RUT del Vendedor]  
    Domicilio: [Dirección del Vendedor]
    
    **Comprador:**
    Nombre completo: [Nombre del Comprador]  
    RUT: [RUT del Comprador]  
    Domicilio: [Dirección del Comprador]
    
    **OBJETO DEL CONTRATO:**  
    El vendedor transfiere al comprador, quien acepta, el bien inmueble ubicado en [Dirección del Inmueble], cuya descripción es la siguiente: [Descripción detallada del bien inmueble, incluyendo su rol de avalúo y características].
    
    **PRECIO DE LA VENTA:**  
    El precio acordado de la compraventa es la suma de [Valor de la venta] pesos chilenos ($[monto en números]), que el comprador declara haber pagado al vendedor al momento de la firma de esta escritura.
    
    **FORMA DE PAGO:**  
    El pago se realiza de la siguiente manera:  
    - [Método de pago detallado]
    
    **ENTREGA DEL BIEN:**  
    El vendedor entrega al comprador el bien en este acto, quien lo recibe en el estado en que se encuentra, renunciando a cualquier reclamación posterior respecto a su condición o vicios.
    
    **DECLARACIONES ADICIONALES:**  
    [Incluir cualquier otra condición relevante]
    
    En virtud de lo expuesto, las partes firman esta escritura en dos ejemplares de un mismo tenor, a fin de que surta los efectos legales correspondientes.
    
    **FIRMAN:**
    
    _______________________________  
    [Firma del Vendedor]  
    [Nombre del Vendedor]
    
    _______________________________  
    [Firma del Comprador]  
    [Nombre del Comprador]
"""

# Generar el PDF
pdfkit.from_string(escritura_texto, 'escritura_compraventa.pdf')
