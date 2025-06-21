from splitnodesdelimiter import split_nodes_delimiter
from split_images_and_links import split_nodes_image, split_nodes_link
from textnode import TextNode
from texttype import TextType

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    code_blocks_included = split_nodes_delimiter([text_node], "`", TextType.CODE)
    italics = split_nodes_delimiter(code_blocks_included, "_", TextType.ITALIC)
    bold_text = split_nodes_delimiter(italics, "**", TextType.BOLD)
    return split_nodes_link(split_nodes_image(bold_text))