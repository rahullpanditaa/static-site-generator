import sys
from project.cp_src_to_dest import src_to_dest
from project.generatepagesrecursive import generate_pages_recursive

def main():
    basepath = get_basepath_from_cmd_line()
    src_to_dest()   
    generate_pages_recursive("content", "template.html", "docs", basepath)

def get_basepath_from_cmd_line():
    return "/" if len(sys.argv) == 1 else sys.argv[1]

if __name__ == "__main__":
    main()