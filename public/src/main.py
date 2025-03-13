import os
import shutil
from textnode import TextNode, TextType

def copy_static_to_public():
    """Recursively copy all contents from `static/` to `public/`, ensuring a clean copy."""
    
    # Define correct paths
    script_dir = os.path.dirname(os.path.abspath(__file__))  # `src/` directory
    static_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "static"))  # `static/` at project root
    public_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "public"))  # `public/` at project root

    # Ensure `static/` exists
    if not os.path.exists(static_dir):
        print("\n❌ Error: 'static' directory not found!\n")
        return
    
    # Ensure `public/` exists before copying
    if not os.path.exists(public_dir):
        os.mkdir(public_dir)
        print(f"Created public directory: {public_dir}")

    # Step 1: Delete existing contents of `public/`, but not `public/` itself
    for item in os.listdir(public_dir):
        item_path = os.path.join(public_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Remove directories
            print(f"Deleted directory: {item_path}")
        else:
            os.remove(item_path)  # Remove files
            print(f"Deleted file: {item_path}")

    # Step 2: Copy all contents from `static/` into `public/`
    for item in os.listdir(static_dir):
        src_path = os.path.join(static_dir, item)
        dest_path = os.path.join(public_dir, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)  # Copy files
            print(f"Copied file: {src_path} → {dest_path}")

        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)  # Copy directories
            print(f"Copied directory: {src_path} → {dest_path}")

def main():
    print("\n🚀 Running Static Site Generator...\n")

    # Step 1: Copy static files to public/
    copy_static_to_public()

    # Step 2: Debugging Example - Create and Print a TextNode
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    print("\n✅ Static site successfully built!\n")

if __name__ == "__main__":
    main()
