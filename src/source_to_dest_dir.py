import shutil
import os

# copy all contents from a source directory to a 
# destination directory
def source_to_dest_dir(source=None, destination=None):
    source_dir_path = os.path.abspath("static")
    dest_dir_path = os.path.abspath("public")
    shutil.rmtree(dest_dir_path) # delete dest dir and its contents
    shutil.copytree(source_dir_path, dest_dir_path)