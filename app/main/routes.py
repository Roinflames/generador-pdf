from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('home.html')  # Asegúrate que exista esta vista
