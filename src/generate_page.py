import os
from markdown_to_html_node import *
from parentnode import ParentNode
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    source_file_path = os.path.abspath(from_path)
    template_file_path = os.path.abspath(template_path)
    dest_file_path = os.path.abspath(dest_path)

    with open(source_file_path, "r") as source, open(template_file_path, "r") as template, open(dest_file_path, "w") as destination:
        source_file_contents = source.read() # markdown
        template_file_contents = template.read() # html

        source_node = markdown_to_html_node(source_file_contents) # source md -> html
        source_html = source_node.to_html()
        source_title = extract_title(source_file_contents)
        template_file_contents = template_file_contents.replace("{{ Title }}", source_title).replace("{{ Content }}", source_html)

        # write to a file at dest_path
        destination.write(template_file_contents)

    