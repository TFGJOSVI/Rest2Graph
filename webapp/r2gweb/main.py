import os
import sys
import tempfile

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
parent_parent_directory = os.path.dirname(parent_directory)
sys.path.append(parent_parent_directory)

import yaml
from flask import Flask, render_template, request
from markupsafe import escape
from python.oas_analysis.read_open_api import read_open_api
from python.classes import OpenAPI



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,fla World!</pcle>"

@app.route("/base")
def base():
    return render_template("base.html", p="p")

@app.route('/upload', methods=['GET'])
def upload():



    return render_template("uploadFile.html")

@app.route('/upload-file', methods=['POST'])
def uplodad_file():
    if request.method == 'POST':
        file = request.files['file']

        contenido = file.read()

        directorio_temporal = tempfile.mkdtemp()

        ruta_archivo = os.path.join(directorio_temporal, file.filename)
        file.save(ruta_archivo)

        with open(ruta_archivo, 'wb') as f:
            f.write(contenido)

        OpenAPI = read_open_api(ruta_archivo)

        print(OpenAPI)

    return render_template("uploadFile.html")


