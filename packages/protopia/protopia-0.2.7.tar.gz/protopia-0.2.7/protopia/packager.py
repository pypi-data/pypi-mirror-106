from os import walk
from os import getcwd
from os import path
from os import sys
from glob import glob

sys.path.append(getcwd())


def packagify():
    paths = []
    start_dir = getcwd()
    pattern = "*.py"
    for dir, subdirs, files in walk(start_dir):
        # Needs to handle ignored directories
        print(dir, subdirs, files)
        if '__init__.py' not in files or len(files) == 0:
            with open('{}/__init__.py'.format(dir), 'w+') as initfile:
                initfile.write('\n')
        paths.extend(glob(path.join(dir, pattern)))
    return paths


packagify()