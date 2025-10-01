from project.cp_src_to_dest import src_to_dest
from project.generatepage import generate_page

def main():
    src_to_dest()   
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()