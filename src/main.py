from project.cp_src_to_dest import src_to_dest
from project.generatepagesrecursive import generate_pages_recursive

def main():
    src_to_dest()   
    generate_pages_recursive("content", "template.html", "public")
    # generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()