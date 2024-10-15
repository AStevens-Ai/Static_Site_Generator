import os
import shutil

def copy_to_source(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)