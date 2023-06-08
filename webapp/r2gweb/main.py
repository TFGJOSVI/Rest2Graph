import os
import sys
import tempfile
import json

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
def base():
    return render_template("base.html")

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

        posts = [post for post in OpenAPI.mutations if post.type == "post"]
        puts = [put for put in OpenAPI.mutations if put.type == "put"]
        deletes = [delete for delete in OpenAPI.mutations if delete.type == "delete"]

        components = set()
        for query in OpenAPI.queries:
            if query.response:
                components.add(query.response.schema.component)
        for mutation in OpenAPI.mutations:
            if mutation.request:
                components.add(mutation.request.schema.component)
            if mutation.response:
                components.add(mutation.response.schema.component)


    return render_template("uploadFile.html", OpenAPI=OpenAPI, posts=posts, puts=puts, deletes=deletes, schemas=components)

@app.route('/source-code', methods=['POST'])
def create_source_code():
    if request.method == 'POST':
        print(request.data)

    return "Hola"

if __name__ == "__main__":
    app.run(debug=True)


