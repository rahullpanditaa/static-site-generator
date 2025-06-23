from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from blocktype import BlockType
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

# converts an entire md doc into a single parent HTMLNode
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # list of all blocks

    # one parent HTML node will be generated from an entire
    # markdown document
    # every block will be a parent node
    # the inline elements will be leaf nodes and have no children 
    main_html_node_children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        opening_tag = generate_opening_tag(block_type)
        if block_type == BlockType.CODE:
            code_node = ParentNode("code", [])
            node = ParentNode("pre", [code_node])
            main_html_node_children.append(node)
        
        if block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST:
            block = format_list_block(block)

        if block_type == BlockType.HEADING:
            opening_tag += str(block.count("#"))
            
        children = text_to_children(block)
        node = ParentNode(opening_tag, children)
        main_html_node_children.append(node)

    return ParentNode("div", main_html_node_children)

def format_list_block(block):
    block_to_return = []
    items = block.split("\n")
    for item in items:
        item = item.replace("- ", "<li>")
        item += "</li>"
        block_to_return.append(item)

    return "\n".join(block_to_return)


def text_to_children(text):
    children_nodes = text_to_textnodes(text)
    children_html_nodes = [text_node_to_html_node(child_node) for child_node in children_nodes]
    return children_html_nodes


def generate_opening_tag(block_type):
    match block_type:
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.CODE:
            return "code"
        case BlockType.HEADING:
            return "h"
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"