import argparse
import os
from jinja2 import Environment, FileSystemLoader
from extension import NotesExtension

_REPO_ROOT = os.path.dirname(os.path.realpath(__file__)) + "/.."
_NOTES_PATH = _REPO_ROOT + "/notes"
_TOPICS_PATH = _REPO_ROOT + "/topics"

def get_list_of_files():
    """Identify the files to work with."""
    lfiles = []
    for root, _, files in os.walk(_NOTES_PATH):
        lfiles.extend([root + "/" + fil for fil in files if fil.endswith(".md")])
    return lfiles

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", "-t", nargs="+", type=str,
            help="List of topics to build notes for.")
    args = parser.parse_args()

    files = get_list_of_files()

    env = Environment(extensions=[NotesExtension, "jinja2.ext.i18n"], loader=FileSystemLoader(_NOTES_PATH))
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True

    for fil in files:
        target_file = fil.replace(_NOTES_PATH, _TOPICS_PATH)
        target_directory = os.path.dirname(target_file)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        template = env.get_template(fil[len(_NOTES_PATH):]).stream().dump(target_file)

if __name__ == "__main__":
    main()
