import re
from project.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes : list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            non_text_node_value = ((node.text.replace("`","")).replace("**", "")).replace("_", "")
            new_node = TextNode(non_text_node_value, node.text_type)
            new_nodes.append(new_node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Error: Invalid markdown, matching delimiter missing")
        
        current_node_contents = node.text.split(delimiter)
        split_nodes = []
        for i in range(len(current_node_contents)):
            if current_node_contents[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(current_node_contents[i], TextType.PLAIN))
            else:
                split_nodes.append(TextNode(current_node_contents[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

        
        