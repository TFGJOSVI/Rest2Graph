from python.build_schemas_resolvers.build_resolvers import build_resolvers
from python.paths import SOURCE_CODE_BASE_PATH, SOURCE_CODE_RETURN_PATH
from python.build_schemas_resolvers.utils import copy_dir
import os
from python.classes import OpenAPI
from python.config_file .load_schemas import write_schemas_string
from python.config_file.utils import replace
from python.build_schemas_resolvers.write_schemas import write_schemas_string_build

INDEX_JS = os.path.join(SOURCE_CODE_RETURN_PATH, 'sourceCode', 'index.js')

def write_resolvers(open_api: OpenAPI) -> None:

    copy_dir(SOURCE_CODE_BASE_PATH, SOURCE_CODE_RETURN_PATH)

    resolvers = build_resolvers(open_api)

    try:

        types = write_schemas_string(open_api, {})

        extra_schemas = open_api.schemas

        schemas = set()

        for q in open_api.queries:
            if q.response:
                schemas.add(q.response.schema)

        for m in open_api.mutations:
            if m.response:
                schemas.add(m.response.schema)
            if m.request:
                schemas.add(m.request.schema)

        extra_schemas = [s for s in extra_schemas if s not in schemas]

    except:
        types = open_api.schemas

        types = write_schemas_string_build(types, True)

        extra_schemas = None



    replace(INDEX_JS, INDEX_JS, '/* TYPES */', types, copy=False)

    if extra_schemas:
        replace(INDEX_JS, INDEX_JS, '/* ex - TYPES */', write_schemas_string_build(extra_schemas,True), copy=False)
    else:
        replace(INDEX_JS, INDEX_JS, '/* ex - TYPES */  ', '', copy=False)

    if resolvers['queries']:
        q = 'type Query {\n'
        for query in resolvers['queries']:
            q += '\t' + query + '\n'
        q += '}'

        replace(INDEX_JS, INDEX_JS, '/* Queries */', q, copy=False)

    if resolvers['mutations']:
        m = 'type Mutation {\n'
        for mutation in resolvers['mutations']:
            m += '\t' + mutation + '\n'
        m += '}'

        replace(INDEX_JS, INDEX_JS, '/* Mutations */', m, copy=False)

    if resolvers['query_resolvers']:
        query_resolvers = resolvers['query_resolvers']
        q = ''.join(query_resolvers)

        replace(INDEX_JS, INDEX_JS, '/* Resolvers Queries */', q, copy=False)

    if resolvers['mutation_resolvers']:
        mutation_resolvers = resolvers['mutation_resolvers']
        m = ''.join(mutation_resolvers)

        replace(INDEX_JS, INDEX_JS, '/* Resolvers Mutations */', m, copy=False)





