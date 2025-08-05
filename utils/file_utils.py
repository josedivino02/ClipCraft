import os

def file_exists(path):
    return os.path.isfile(path)

def remove_file(path):
    if os.path.exists(path):
        os.remove(path)

def ensure_output_folder():
    if not os.path.exists("output"):
        os.makedirs("output")
