from pathlib import Path
from project.generatepage import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir_path = Path(dir_path_content).resolve()
    template_file_path = Path(template_path).resolve()
    destination_dir_path = Path(dest_dir_path)

    for child in content_dir_path.iterdir():
        if not child.is_dir() and child.suffix == ".md":
            generate_page(child.resolve(), template_file_path, destination_dir_path / child)
        else:
            generate_pages_recursive(child.resolve(), template_file_path, destination_dir_path / child)