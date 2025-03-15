import sys
import os
import shutil
from page_generator import generate_pages_recursive
from static_to_public import copy_files_recursive

sys.dont_write_bytecode = True  # Prevents __pycache__ creation

# Ensure Python can find `static_to_public.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



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

    # Generate HTML files from Markdown in content directory
    print("\n📝 Generating HTML files from Markdown in content...\n")

    if os.path.exists(content_dir):
        generate_pages_recursive(content_dir, template_path, dir_path_public)  # ✅ Fixed function call
        print(f"✅ Successfully generated all pages in {dir_path_public}")
    else:
        print("❌ Error: No content directory found!")

    print("\n✅ Done!~\n")

main()


