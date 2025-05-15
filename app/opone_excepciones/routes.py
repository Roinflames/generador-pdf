from flask import render_template, make_response, redirect, url_for
from . import opone_excepciones_bp
import pdfkit

@opone_excepciones_bp.route('/opone_excepciones_preview')
def opone_excepciones_view():
    data = {
        "tribunal": "SANTIAGO (24°)",
        "nombre_demandado": "MAURICIO ANDRÉS SÁEZ ESCUDERO",
        "direccion_demandado": "calle Concepción 266, oficina 804, comuna de Providencia",
        "caratulados": "BANCO DE CRÉDITO E INVERSIONES / SÁEZ",
        "rol_causa": "C-4044-2025", # no encontrado
        "argumento_excepcion": "la firma del suscriptor no ha sido autorizada ante Notario Público de conformidad a la ley", # no encontrado
        "ABG_PATROCINADOR" : "Eduardo Mauricio Lara Quiroz",
        "ABG_CEDULA" : "17.314.741-4",
        "DIRE_ESTUDIO" : "calle la concepcion 266, oficina 804, comuna de providencia, región metropolitana", # no encontrado
        "ABG_EMAIL" : "jefe.civil@alfaromadariaga.cl"
    }

    return render_template('opone_excepciones_preview.html', **data)

@opone_excepciones_bp.route('/generar_pdf')
def generar_pdf():
    data = {
        "tribunal": "SANTIAGO (24°)",
        "nombre_demandado": "MAURICIO ANDRÉS SÁEZ ESCUDERO",
        "direccion_demandado": "calle Concepción 266, oficina 804, comuna de Providencia",
        "caratulados": "BANCO DE CRÉDITO E INVERSIONES / SÁEZ",
        "rol_causa": "C-4044-2025", # no encontrado
        "argumento_excepcion": "la firma del suscriptor no ha sido autorizada ante Notario Público de conformidad a la ley", # no encontrado
        "ABG_PATROCINADOR" : "Eduardo Mauricio Lara Quiroz",
        "ABG_CEDULA" : "17.314.741-4",
        "DIRE_ESTUDIO" : "calle la concepcion 266, oficina 804, comuna de providencia, región metropolitana", # no encontrado
        "ABG_EMAIL" : "jefe.civil@alfaromadariaga.cl"
    }

    # Renderizar la plantilla para el PDF
    html = render_template('opone_excepciones.html', **data)
    pdf = pdfkit.from_string(html, False)

    # TODO filename=opone_excepciones con nomenclatura de la causa
    # Generar el PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=opone_excepciones.pdf'

    return response