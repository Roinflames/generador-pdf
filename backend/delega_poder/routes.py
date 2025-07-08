from flask import render_template, make_response, request, jsonify
from flask_cors import CORS
from . import delega_bp
import os
import pdfkit
import json

CORS(delega_bp)

@delega_bp.route("/data", methods=["GET"])
def obtener_datos_json():
    try:
        json_path = os.path.join(delega_bp.root_path, 'static', 'data', 'delega_poder_data.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Error al leer JSON: {str(e)}"}), 500

@delega_bp.route("/generar_pdf", methods=["POST"])
def generar_pdf():
    print("🟡 Recibiendo solicitud para generar PDF...")

    if not request.is_json:
        print("🔴 Error: El cuerpo no es JSON válido")
        return jsonify({"error": "El cuerpo de la solicitud debe ser JSON."}), 415

    try:
        data = request.get_json()
        print("✅ Datos recibidos del frontend:")
        print(data)
        for k, v in data.items():
            print(f"   {k}: {v}")

        # Guardar datos en JSON
        json_path = os.path.join(delega_bp.root_path, 'static', 'data', 'delega_poder_data.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ JSON actualizado en: {json_path}")

        # Render template con datos nuevos
        html = render_template('delega_poder.html', **data)
        print("📝 Render HTML exitoso. Previsualización:")
        print(html[:300] + " ...")  # Solo mostramos los primeros 300 caracteres

        options = {
            'page-size': 'Letter',
            'encoding': 'UTF-8',
            'enable-local-file-access': None,
        }

        # Ruta del PDF
        pdf_dir = os.path.join(delega_bp.root_path, 'static', 'pdfs')
        os.makedirs(pdf_dir, exist_ok=True)

        pdf_path = os.path.join(pdf_dir, 'delega_poder.pdf')
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
            print("🔁 PDF viejo eliminado.")

        # Generar PDF desde el HTML
        pdfkit.from_string(html, pdf_path, options=options)
        print(f"✅ PDF generado correctamente en: {pdf_path}")

        return jsonify({
            "message": "PDF generado correctamente",
            "pdf_url": "/delega_poder/pdf_preview"
        }), 200

    except Exception as e:
        import traceback
        print("❌ Error inesperado:")
        print(traceback.format_exc())
        return jsonify({"error": f"Error al generar PDF: {str(e)}"}), 500

@delega_bp.route("/pdf_preview", methods=["GET"])
def pdf_preview():
    pdf_path = os.path.join(delega_bp.root_path, 'static', 'pdfs', 'delega_poder.pdf')
    if not os.path.exists(pdf_path):
        return "PDF no encontrado", 404

    with open(pdf_path, 'rb') as f:
        response = make_response(f.read())
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "inline; filename=delega_poder.pdf"
        return response
