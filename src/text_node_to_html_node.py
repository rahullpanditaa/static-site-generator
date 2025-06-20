import re
from texttype import TextType
from textnode import TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type not in TextType:
        raise BaseException("Invalid text type")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            matches = re.search(r"^\[(.+)\]\((.+)\)", text_node.text)
            return LeafNode("a", matches.group(1), {"href":f"{matches.group(2)}"})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":"www", "alt":"alt-text"})
