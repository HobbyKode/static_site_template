import sys
import os
import shutil
from page_generator import generate_pages_recursive
from static_to_docs import copy_files_recursive

# Default basepath
basepath = "/"

# Check if arg was provided
if len(sys.argv) > 1:
    basepath = sys.argv[1]
    print(f"Using basepath: {basepath}")

# Normalize basepath (no trailing slash)
basepath = basepath.rstrip("/")
print(f"Normalized basepath: {basepath}")


sys.dont_write_bytecode = True  # Prevents __pycache__ creation

# Ensure Python can find `static_to_docs.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



# Paths based on your project structure
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) #Correct Root path
dir_path_static = os.path.join(project_root, "static")  # Static assets
dir_path_docs = os.path.join(project_root, "docs")  # Final output folder
content_dir = os.path.join(project_root, "content")  # Markdown pages folder
template_path = os.path.join(project_root, "template.html")  # HTML Template

def main():
    print(f"\nSCRIPT DIR: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"STATIC DIR: {dir_path_static}")
    print(f"DOCS DIR: {dir_path_docs}")
    print(f"CONTENT DIR: {content_dir}")
    print(f"BASEPATH: {basepath}")  # ✅ Debugging output

    print("\n🚀 Deleting contents of the docs directory...\n")
    if os.path.exists(dir_path_docs):
        for item in os.listdir(dir_path_docs):
            item_path = os.path.join(dir_path_docs, item)
            # Do NOT delete `src/`, `.gitignore`
            if os.path.isdir(item_path) and item not in ["src"]:
                shutil.rmtree(item_path)
            elif os.path.isfile(item_path) and item not in [".gitignore"]:
                os.remove(item_path)

    print("\n✅ Copying static files to docs directory...\n")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print(f"\n📝 Using basepath: '{basepath}'\n")

    # Generate HTML files from Markdown in content directory
    print("\n📝 Generating HTML files from Markdown in content...\n")

    if os.path.exists(content_dir):
        generate_pages_recursive(content_dir, template_path, dir_path_docs, basepath) 
        print(f"✅ Successfully generated all pages in {dir_path_docs}")
    else:
        print("❌ Error: No content directory found!")

    print("\n✅ Done!~\n")

main()


