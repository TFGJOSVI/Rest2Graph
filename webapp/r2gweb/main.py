import os
import sys
import tempfile
import json

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
parent_parent_directory = os.path.dirname(parent_directory)
sys.path.append(parent_parent_directory)

from flask import Flask, render_template, request, send_file
from python.oas_analysis.read_open_api import read_open_api
from python.classes import *
from python.build_schemas_resolvers.create_source_code import create_source_code
from python.paths import SOURCE_CODE_RETURN_ZIP



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
def build():
    if request.method == 'POST':
        o = json.loads(request.data)
        openApi = cast_to_openapi(o)
        create_source_code('',openApi)

    return send_file(SOURCE_CODE_RETURN_ZIP, as_attachment=True, download_name="source_code.zip")


if __name__ == "__main__":
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
    app.run(debug=True)

## Utils

def cast_to_openapi(data):
    queries = []
    mutations = []
    servers = []

    for query_data in data.get('queries', []):
        parameters = []
        for param_data in query_data.get('parameters', []):
            parameter = Parameter(**param_data)
            parameters.append(parameter)


        if query_data.get('response'):
            component_data = query_data['response']['schema']['component']
            attributes_data = component_data['attributes']

            attributes = []
            for attr_data in attributes_data:
                attribute = Attribute(**attr_data)
                attributes.append(attribute)

            component = Component(
                name=component_data['name'],
                attributes=attributes
            )

            schema = Schema(
                type=query_data['response']['schema']['type'],
                component=component
            )

            response = Response(schema=schema)
        else:
            response= None


        query = Query(
            description=query_data['description'],
            parameters=parameters,
            url=query_data['url'],
            name=query_data['name'],
            response=response
        )
        queries.append(query)


    for mutation_data in data.get('mutations', []):
        parameters = []
        for param_data in mutation_data.get('parameters', []):
            parameter = Parameter(**param_data)
            parameters.append(parameter)

        request_body = RequestBody(
            required=mutation_data['request']['required'],
            schema=Schema(**mutation_data['request']['schema'])
        )if mutation_data.get('request') else None

        if mutation_data.get('request'):
            component_data = mutation_data['request']['schema']['component']
            attributes_data = component_data['attributes']

            attributes = []
            for attr_data in attributes_data:
                attribute = Attribute(**attr_data)
                attributes.append(attribute)

            component = Component(
                name=component_data['name'],
                attributes=attributes
            )

            schema = Schema(
                type=mutation_data['request']['schema']['type'],
                component=component
            )

            request_body = RequestBody(schema=schema, required=mutation_data['request']['required'])
        else:
            request_body= None

        if mutation_data.get('response'):
            component_data = mutation_data['response']['schema']['component']
            attributes_data = component_data['attributes']

            attributes = []
            for attr_data in attributes_data:
                attribute = Attribute(**attr_data)
                attributes.append(attribute)

            component = Component(
                name=component_data['name'],
                attributes=attributes
            )

            schema = Schema(
                type=mutation_data['response']['schema']['type'],
                component=component
            )

            response = Response(schema=schema)
        else:
            response = None


        mutation = Mutation(
            description=mutation_data['description'],
            request=request_body,
            parameters=parameters,
            url=mutation_data['url'],
            name=mutation_data['name'],
            type=mutation_data['type'],
            response=response
        )
        mutations.append(mutation)

    servers = data.get('servers', [])


    openapi = OpenAPI(
        queries=queries,
        mutations=mutations,
        servers=servers,
        schemas=[]
    )

    return openapi

