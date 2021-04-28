import argparse
import os

"""
Converts from this:

close": {
    "message": "Cerrar",
    "description": "This is for closing the menu"
},

{
    "id": "close",
    "en": "Close",
    "fr": "Fermer",
    "es_es": "Cerrar"
},
"""


def remake_json_locales():
    parser = argparse.ArgumentParser(description='Process some json.')
    parser.add_argument('--chrome-translations-json', type=dir_path)

    args = parser.parse_args()
    print(args)


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


if __name__ == '__main__':
    remake_json_locales()
