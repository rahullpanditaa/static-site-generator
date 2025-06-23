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
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            matches = re.search(r"^\[(.+)\]\((.+)\)", text_node.text)
            return LeafNode(tag="a", value=matches.group(1), props={"href":f"{matches.group(2)}"})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src":"www", "alt":"alt-text"})
