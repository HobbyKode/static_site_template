import os
import shutil

def cleanup_directory(destination_dir):
    """Removes all files and folders except those in the exclusion list."""
    # List of things to exclude
    exclusions = {"static_to_public.py", "main.sh", "test.sh", "src"}

    # Walk through the directory
    for item in os.listdir(destination_dir):
        item_path = os.path.join(destination_dir, item)

        # Skip excluded items
        if item in exclusions:
            print(f"Excluding: {item_path}")
            continue

        # Remove files or directories
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)  # Removes file or symbolic link
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Removes directory
            print(f"Deleted directory: {item_path}")

def copy_static_to_public():
    """Recursively copy all contents from `static/` to `public/`, ensuring a clean copy."""
    
    # Define correct paths
    script_dir = os.path.dirname(os.path.abspath(__file__))  # `src/` directory
    static_dir = os.path.abspath(os.path.join(script_dir, "..", "static"))  # `static/` at project root
    public_dir = os.path.abspath(os.path.join(script_dir, "..", "public"))  # Correct path for `public/`

    # Ensure `static/` exists
    if not os.path.exists(static_dir):
        raise FileNotFoundError("\n❌ Error: 'static/' directory not found!\n")
    
    # Ensure `public/` exists before copying
    if not os.path.exists(public_dir):
        os.mkdir(public_dir)
        print(f"Created public directory: {public_dir}")
    
    # Safety check to ensure we're targeting the expected folder
    assert public_dir.endswith("public"), f"Suspicious `public_dir` path: {public_dir}"

    # Step 1: Clean up the `public/` directory using `cleanup_directory`
    cleanup_directory(public_dir)

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