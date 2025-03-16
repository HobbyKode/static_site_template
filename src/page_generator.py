import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """Recursively generates HTML pages from markdown files in content/."""
    print(f"\n📝 Scanning content directory: {dir_path_content}")

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

    print("\n✅ All pages successfully generated!\n")


def generate_page(from_path, template_path, dest_path, basepath):
    """Generates an HTML page from a markdown file using a template."""
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Add this to your generate_page function right before you write the file
    print(f"DEBUG: Basepath is '{basepath}'")


    # Step 1: Read the markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()  # ✅ Read the actual content

    # Step 2: Read the template file
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Step 3: Convert markdown to HTML
    html_body = markdown_to_html_node(markdown_content).to_html()

    # Step 4: Extract the title correctly (fix the issue here)
    title = extract_title(markdown_content)  # ✅ Ensure this is a string, not a function

    # Step 5: Replace placeholders in the template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_body)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    # Step 6: Ensure destination directories exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Step 7: Write the final HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

    print(f"✅ Successfully generated: {dest_path}")


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")






