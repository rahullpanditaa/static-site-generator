import re
from texttype import TextType
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if matches := re.search(fr"^(.* ?)({delimiter}.+{delimiter})( ?.*)$", node.text):
                new_nodes.extend([TextNode(matches.group(1), TextType.TEXT),
                                  TextNode(matches.group(2).replace(delimiter,""), text_type),
                                  TextNode(matches.group(3),TextType.TEXT)])
            else:
                raise BaseException("Invalid markdown syntax")
        else:
            new_nodes.extend(node)

    return new_nodes

