from project.textnode import TextNode, TextType
from project.htmlnode import HTMLNode
from project.split_nodes_delimiter import split_nodes_delimiter

def main():
    node = TextNode("This is text with `code block` inside it.", TextType.CODE)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
    print(TextType.CODE)

if __name__ == "__main__":
    main()