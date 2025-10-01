from project.markdowntohtml import markdown_to_html_node
from project.extract_title import extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read md at from_path
    with open(from_path) as f:
        from_path_contents = f.read()

    # read template file
    with open(template_path) as f:
        template_contents = f.read()

    # md file -> html str
    md_html_to_str = markdown_to_html_node(from_path_contents).to_html()

    title = extract_title(from_path_contents)

    html = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", md_html_to_str)

    dest = Path(dest_path).resolve()

    with open(dest, "w") as f:
        f.write(html)