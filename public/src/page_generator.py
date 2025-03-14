import os
from src.markdown_blocks import markdown_to_html_node
from src.page_generator import extract_title  # ✅ Ensure correct import



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






