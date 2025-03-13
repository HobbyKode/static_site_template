from textnode import TextNode, TextType
from static_to_public import copy_static_to_public

def main():
    print("\n🚀 Running Static Site Generator...\n")

    # Step 1: Copy static files to public/
    copy_static_to_public() # Calls the function in static_to_public.py

    # Step 2: Debugging Example - Create and Print a TextNode
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    print("\n✅ Static site successfully built!\n")

if __name__ == "__main__":
    main()
