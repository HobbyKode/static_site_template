import os
import shutil

def copy_static_to_public(src, dest):
    """Recursively copy all contents from `src` (static) to `dest` (public), ensuring a clean copy."""
    
    # Step 1: Delete all existing files inside `public/` (but not `public/` itself)
    for item in os.listdir(dest):
        item_path = os.path.join(dest, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Remove directories
            print(f"Deleted directory: {item_path}")
        else:
            os.remove(item_path)  # Remove files
            print(f"Deleted file: {item_path}")

    # Step 2: Recursively copy everything from `static/` into `public/`
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)  # Copy files
            print(f"Copied file: {src_path} → {dest_path}")

        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)  # Copy entire directories
            print(f"Copied directory: {src_path} → {dest_path}")

# Automatically execute when script runs
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    static_dir = os.path.abspath(os.path.join(script_dir, "..", "static"))  # Static is now at root
    public_dir = script_dir  # Destination remains `public/`

    # Ensure the static directory exists before copying
    if os.path.exists(static_dir):
        copy_static_to_public(static_dir, public_dir)
        print("\n✅ Static files successfully copied into public!\n")
    else:
        print("\n❌ Error: 'static' directory not found!\n")