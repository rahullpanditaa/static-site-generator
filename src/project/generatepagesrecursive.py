from pathlib import Path
from project.generatepage import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_dir_path = Path(dir_path_content).resolve()
    template_file_path = Path(template_path).resolve()
    destination_dir_path = Path(dest_dir_path)

    for child in content_dir_path.iterdir():
        child_rel_path = child.relative_to(content_dir_path)
        dest_path = destination_dir_path / child_rel_path
        if not child.is_dir() and child.suffix == ".md":
            dest_file_path = dest_path.with_suffix(".html")
            dest_file_path.parent.mkdir(parents=True, exist_ok=True)
            generate_page(child, template_file_path, dest_file_path, basepath)
        else:
            dest_path.mkdir(parents=True, exist_ok=True)
            generate_pages_recursive(child, template_file_path, dest_path, basepath)