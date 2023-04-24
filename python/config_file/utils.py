from os import fdopen, remove
from shutil import copymode, move
from tempfile import mkstemp
import os
from typing import Union

from python.classes import Response


def replace(file_path: str, new_file_path: Union[str, None], pattern: str, subst: str, copy : bool = True) -> None:

    fh, abs_path = mkstemp()

    if copy:

        if os.path.isfile(file_path):

            if os.path.exists(new_file_path):
                os.remove(new_file_path)

            print(f'Copying {file_path} to {new_file_path}')

            with open(file_path, "r") as archivo_orig, open(new_file_path,"w") as archivo_copia:
                for linea in archivo_orig:
                    archivo_copia.write(linea)
            archivo_orig.close()
            archivo_copia.close()

        else:
            print("The file doesn't exist.")

        file_path = new_file_path

    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))

    copymode(file_path, abs_path)

    remove(file_path)

    move(abs_path, file_path)


def parse_type_oas_graphql(type_oas: str) -> str:

    if type_oas == 'string' or type_oas == 'String':
        return 'String'
    elif type_oas == 'integer' or type_oas == 'Integer':
        return 'Int'
    elif type_oas == 'number' or type_oas == 'Number':
        return 'Float'
    elif type_oas == 'boolean' or type_oas == 'Boolean':
        return 'Boolean'
    else:
        return type_oas

def parse_parameters(parameters: list) -> str:
    string_parameters = ''
    for parameter in parameters:
        if not parameter.query:
            if parameter.required:
                string_parameters += f'{parameter.name}: {parse_type_oas_graphql(parameter.type)}!, '
            else:
                string_parameters += f'{parameter.name}: {parse_type_oas_graphql(parameter.type)}, '
    return string_parameters[:-2]

def parse_parameters_query(parameters):
    string_parameters = '\t\t- query_parameters:'
    for parameter in parameters:
        if  parameter.query:
            if parameter.required:
                    string_parameters += f'\n\t\t\t- {parameter.name}: {parameter.type}!'
            else:
                string_parameters += f'\n\t\t\t- {parameter.name}: {parameter.type}'

    return string_parameters

def parse_schema(response: Response) -> Union[str, None]:
    if response:
        if response.schema.type == 'array':
            return f'[{response.schema.component.name}]'
        elif response.schema.type == 'object':
            return response.schema.component.name
        else:
            return parse_type_oas_graphql(response.schema.component.name)
    else:
        return None
