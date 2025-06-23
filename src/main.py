from textnode import TextNode
from texttype import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from splitnodesdelimiter import split_nodes_delimiter
from markdown_to_blocks import markdown_to_blocks

def main():
    # node_one = TextNode("blah blah blah `some code block` hfrihfrihfrf", TextType.TEXT)
    # print(split_nodes_delimiter([node_one, node_one], "`", TextType.CODE))
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
    print(markdown_to_blocks(md))
    
    

if __name__ == "__main__":
    main()