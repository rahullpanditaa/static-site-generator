import re
from texttype import TextType
from textnode import TextNode

# some text with a `code block` in it
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if matches := re.findall(fr"{delimiter}(.+){delimiter}", node.text):
            for match in matches:
                new_nodes.append(TextNode(match, text_type))
        else:
            raise BaseException("Invalid markdown syntax")
        
    return new_nodes

