import os
import shutil
import zipfile

def parse_type(response: str) -> str:
    if response.__contains__('['):
        type = 'array'
    elif response == 'Int':
        type = 'integer'
    elif response == 'Float':
        type = 'number'
    elif response == 'Boolean':
        type = 'boolean'
    elif response == 'String':
        type = 'string'
    else:
        type = response

    return type


def copy_dir(src: str, dst: str) -> None:
    if os.path.exists(dst):
        shutil.rmtree(dst,  ignore_errors=True)
    shutil.copytree(src, dst)


def zip_directory(directory_path: str, zip_path: str) -> None:
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory_path))
