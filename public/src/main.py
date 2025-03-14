import sys
import os
import shutil
from page_generator import generate_page

sys.dont_write_bytecode = True  # Prevents __pycache__ creation

# Ensure Python can find `static_to_public.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from static_to_public import copy_files_recursive

# Paths based on your project structure
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
dir_path_static = os.path.join(project_root, "static")  # Static assets
dir_path_public = os.path.join(project_root, "public")  # Final output folder
content_dir = os.path.join(project_root, "content")  # Markdown pages folder
template_path = os.path.join(project_root, "template.html")  # HTML Template

def main():
    print(f"\nSCRIPT DIR: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"STATIC DIR: {dir_path_static}")
    print(f"PUBLIC DIR: {dir_path_public}")
    print(f"CONTENT DIR: {content_dir}")

    print("\n🚀 Deleting contents of the public directory...\n")
    if os.path.exists(dir_path_public):
        for item in os.listdir(dir_path_public):
            item_path = os.path.join(dir_path_public, item)
            # Do NOT delete `src/`, `.gitignore`
            if os.path.isdir(item_path) and item not in ["src"]:
                shutil.rmtree(item_path)
            elif os.path.isfile(item_path) and item not in [".gitignore"]:
                os.remove(item_path)

    print("\n✅ Copying static files to public directory...\n")
    copy_files_recursive(dir_path_static, dir_path_public)

    # Generate index.html from content/index.md
    print("\n📝 Generating index.html from content/index.md...\n")
    index_md_path = os.path.join(content_dir, "index.md")  # Path to index.md
    index_html_path = os.path.join(dir_path_public, "index.html")  # Path to index.html

    if os.path.exists(index_md_path):
        generate_page(index_md_path, template_path, index_html_path)
        print(f"✅ Successfully generated: {index_html_path}")
    else:
        print("❌ Error: No index.md found in content/")

    print("\n✅ Done!~\n")

main()

main()


