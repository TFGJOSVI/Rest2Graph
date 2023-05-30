import os
import shutil
import sys
import time

import click

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from python.paths import SOURCE_CODE_RETURN_ZIP, CONFIG_FILE_PATH, COPIES_TEMPLATE_PATH
from python.build_schemas_resolvers.create_source_code import create_source_code_not_default_path, create_source_code
from python.config_file.create_config_file import create_config_file


@click.command()
@click.pass_context
@click.option('--oas-path', default=None, help='Path to the OpenAPI file.')
@click.option('--destination-path', default=None, help='Path to the destination folder.')
@click.option('--config-file', default=False, is_flag=True, help='If not provided, a config file not will be created.')
def build_graph(ctx, oas_path: str, destination_path: str, config_file: bool):
    if not oas_path:
        click.echo('Please provide a path to the OpenAPI file.')
        ctx.abort()

    if not os.path.exists(oas_path):
        click.echo('The OpenAPI file does not exist.')
        ctx.abort()

    if not destination_path:
        click.echo('Please provide a path to the destination folder.')
        ctx.abort()

    if not os.path.exists(destination_path):
        click.echo('The destination folder does not exist.')
        ctx.abort()

    if config_file:
        click.echo('Creating config file...')

        if os.path.exists(COPIES_TEMPLATE_PATH):
            os.remove(COPIES_TEMPLATE_PATH)
            
        create_config_file(oas_path, COPIES_TEMPLATE_PATH)
        click.edit(filename=COPIES_TEMPLATE_PATH)
        create_source_code_not_default_path(COPIES_TEMPLATE_PATH)
        shutil.copy(SOURCE_CODE_RETURN_ZIP, destination_path)
    else:
        click.echo('Building schemas and resolvers...')
        create_source_code(oas_path)
        shutil.copy(SOURCE_CODE_RETURN_ZIP, destination_path)


if __name__ == '__main__':
    build_graph()
