from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    leaf_node = LeafNode("p", "This is a paragraph", {"href":"e3ee3e3ee3", "target":"_blank"})
    print(leaf_node.to_html())
    

if __name__ == "__main__":
    main()