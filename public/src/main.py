import os
import shutil
import importlib.util

# Locate static_to_public.py manually
script_dir = os.path.dirname(os.path.abspath(__file__))
static_to_public_path = os.path.abspath(os.path.join(script_dir, "..", "static_to_public.py"))

# Load static_to_public.py
spec = importlib.util.spec_from_file_location("static_to_public", static_to_public_path)
static_to_public = importlib.util.module_from_spec(spec)
spec.loader.exec_module(static_to_public)

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    # Step 1: Load and execute `copy_files_recursive()`
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        
    print("Copying static files to public directory...")
    static_to_public.copy_files_recursive(dir_path_static, dir_path_public)

main()

