from splitnodesdelimiter import split_nodes_delimiter
from split_images_and_links import split_nodes_image, split_nodes_link
from textnode import TextNode
from texttype import TextType

def text_to_textnodes(text):
        
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes