from os import fdopen, remove
from shutil import copymode, move
from tempfile import mkstemp
import os


def replace(file_path: str, new_file_path: str, pattern: str, subst: str) ->  None:

    fh, abs_path = mkstemp()

    if os.path.isfile(file_path):

        if os.path.exists(new_file_path):
            os.remove(new_file_path)

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
