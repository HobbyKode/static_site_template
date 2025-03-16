import sys
import os
import shutil
from page_generator import generate_pages_recursive
from static_to_docs import copy_files_recursive


sys.dont_write_bytecode = True  # Prevents __pycache__ creation

# Ensure Python can find `static_to_docs.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



# Paths based on your project structure
dir_path_static  = "./static"  # Static assets
dir_path_docs = "./docs"  # Final output folder
content_dir = "./content"  # Markdown pages folder
template_path = "./template.html"  # HTML Template
# Default basepath
default_basepath = "/"



def main():
    basepath = default_basepath
    # Check if arg was provided
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        print(f"Using basepath: {basepath}")


    print(f"\nSCRIPT DIR: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"STATIC DIR: {dir_path_static}")
    print(f"DOCS DIR: {dir_path_docs}")
    print(f"CONTENT DIR: {content_dir}")
    print(f"BASEPATH: {basepath}")  # ✅ Debugging output

    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(content_dir, template_path, dir_path_docs, basepath)

main()


