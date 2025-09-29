from project.split_nodes_delimiter import split_nodes_delimiter
from project.splitnodesimageslinks import split_nodes_image, split_nodes_links
from project.textnode import TextNode, TextType

def text_to_textnodes(text):
    # code
    # imgs
    # links
    # bold
    # italics
    node = TextNode(text, TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    return new_nodes