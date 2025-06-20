from textnode import TextNode
from texttype import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node

def main():
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(html_node.value)
    print(html_node.tag)
    

if __name__ == "__main__":
    main()