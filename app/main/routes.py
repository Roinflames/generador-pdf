from flask import render_template, jsonify
from flask_login import login_required
from . import main

@main.route('/')
def index():
    return jsonify({"message": "API generador-pdf operativa"})
