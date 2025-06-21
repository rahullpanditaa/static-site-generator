from splitnodesdelimiter import split_nodes_delimiter
from split_images_and_links import split_nodes_image, split_nodes_link
from textnode import TextNode
from texttype import TextType

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    