import os
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """Recursively generates HTML pages from markdown files in content/."""
    print(f"\n📝 Scanning content directory: {dir_path_content}")

    # Ensure destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    # Iterate over all files and directories in content/
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(entry_path):
            # If entry is a directory, recurse into it
            generate_pages_recursive(entry_path, template_path, dest_path)

        elif entry.endswith(".md"):
            # Convert markdown to HTML and replace `.md` with `.html`
            dest_html_path = dest_path.replace(".md", ".html")
            generate_page(entry_path, template_path, dest_html_path)

    print("\n✅ All pages successfully generated!\n")

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_page(from_path, template_path, dest_path):
    """Generates an HTML page from a markdown file using a template."""
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Step 1: Read the markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()  # ✅ Read the actual content

    # Step 2: Read the template file
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Step 3: Convert markdown to HTML
    html_body = markdown_to_html_node(markdown_content).to_html()

    # Step 4: Extract the title correctly (fix the issue here)
    title = extract_title(markdown_content)  # ✅ Ensure this is a string, not a function

    # Step 5: Replace placeholders in the template
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_body)

    # Step 6: Ensure destination directories exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Step 7: Write the final HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ Successfully generated: {dest_path}")






