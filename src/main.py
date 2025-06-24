from source_to_dest_dir import source_to_dest_dir
from generate_page import generate_page

def main():
    source_to_dest_dir()
    generate_page("content/index.md", "template.html", "public/index.html")
    
    

if __name__ == "__main__":
    main()