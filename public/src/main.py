import os
import sys
import shutil

# Ensure Python can find `static_to_public.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from static_to_public import copy_files_recursive

dir_path_static = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "static"))
dir_path_public = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # This is `public/`

def main():
    print(f"\nSCRIPT DIR: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"STATIC DIR: {dir_path_static}")
    print(f"PUBLIC DIR: {dir_path_public}")

    print("\n🚀 Deleting contents of the public directory...\n")
    if os.path.exists(dir_path_public):
        for item in os.listdir(dir_path_public):
            item_path = os.path.join(dir_path_public, item)
            # Do NOT delete `src/`, `static_to_public.py`, or `.gitignore`
            if os.path.isdir(item_path) and item not in ["src"]:
                shutil.rmtree(item_path)
            elif os.path.isfile(item_path) and item not in ["static_to_public.py", ".gitignore"]:
                os.remove(item_path)

    print("\n✅ Copying static files to public directory...\n")
    copy_files_recursive(dir_path_static, dir_path_public)

main()

