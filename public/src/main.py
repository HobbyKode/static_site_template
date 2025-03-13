import os
import sys
import shutil

# Add `public/` to the module search path so `static_to_public.py` can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from static_to_public import copy_files_recursive

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

main()