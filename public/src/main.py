import os
import importlib.util
import sys
from textnode import TextNode, TextType

sys.dont_write_bytecode = True  # Prevent __pycache__ creation

def load_static_to_public():
    """Dynamically load static_to_public.py from the public directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))  # `src/` directory
    public_dir = os.path.abspath(os.path.join(script_dir, ".."))  # ✅ Fix: Move up one level to `public/`
    static_to_public_path = os.path.join(public_dir, "static_to_public.py")

    print(f"\nSCRIPT DIR: {script_dir}")  # Debugging
    print(f"PUBLIC DIR: {public_dir}")  # Debugging

    if not os.path.exists(static_to_public_path):
        print(f"\n❌ Error: 'static_to_public.py' not found at {static_to_public_path}!\n")
        return None

    spec = importlib.util.spec_from_file_location("static_to_public", static_to_public_path)
    static_to_public = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(static_to_public)
    return static_to_public

def main():
    print("\n🚀 Running Static Site Generator...\n")

    # Step 1: Load and execute `copy_static_to_public()`
    static_to_public = load_static_to_public()
    if static_to_public:
        static_to_public.copy_static_to_public()

    # Step 2: Debugging Example - Create and Print a TextNode
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    print("\n✅ Static site successfully built!\n")

if __name__ == "__main__":
    main()
