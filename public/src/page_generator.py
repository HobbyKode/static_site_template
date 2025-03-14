import os
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
def extract_title(markdown):
    """Extracts the first H1 (# Heading) from the markdown content."""
    blocks = markdown_to_blocks(markdown)  # Split markdown into blocks
    
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING and block.startswith("# "):
            return block.split("\n")[0][2:].strip()  # Remove "# " and return the title
            
    return "Untitled"  # Default title if no H1 is found


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #Step 1: Read the markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read

    #Step 2: Read the template   
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read 
    # Step 3: Convert markdown to HTML
    html_body = markdown_to_html_node(markdown_content).to_html()

    #Step 4: Extract Title
    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_body)


     # Step 6: Ensure destination directories exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Step 7: Write the final HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ Successfully generated: {dest_path}")





