from project.markdowntohtml import markdown_to_html_node
from project.extract_title import extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read md at from_path
    src_path = Path(from_path).resolve()
    with open(src_path) as f:
        from_path_contents = f.readlines()
        from_path_contents = "".join(from_path_contents)

    # read template file
    temp_path = Path(template_path).resolve()
    with open(temp_path) as f:
        template_contents = f.readlines()
        template_contents = "".join(template_contents)

    # md file -> html str
    md_html_to_str = markdown_to_html_node(from_path_contents).to_html()
    

    title = extract_title(from_path_contents)

    html = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", md_html_to_str)

    dest = Path(dest_path).resolve()

    with open(dest, "w") as f:
        f.write(html)