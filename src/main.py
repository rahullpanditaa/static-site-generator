from project.textnode import TextNode, TextType
from project.htmlnode import HTMLNode

def main():
    htmlnode = HTMLNode("p", "this is a paragraph")
    print(htmlnode)

if __name__ == "__main__":
    main()