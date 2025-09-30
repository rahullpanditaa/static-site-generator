from project.markdowntoblocks import markdown_to_blocks
from project.blocktoblocktype import block_to_block_type, BlockType
from project.htmlnode import HTMLNode
from project.texttotextnodes import text_to_textnodes
from project.textnode_to_htmlnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = create_html_node(block, block_type)

def create_html_node(block: str, block_type: BlockType):
    html_node_children = find_children_in_block_text(block)
    match block_type:
        case BlockType.HEADING:
            n = len(block) - len(block.lstrip("#"))
            return HTMLNode(tag=f"h{n}", value=block.lstrip("#").strip(), children=html_node_children)
        case BlockType.QUOTE:
            return HTMLNode(tag="blockquote", value=block.replace(">", ""), children=html_node_children)
        case BlockType.UNORDERED_LIST:
            items = block.splitlines()
            ul_items = []
            for item in items:
                item = item.removeprefix("- ")
                item = f"<li>{item}</li>"
                ul_items.append(item)
            ul_value = "\n".join(ul_items)
            return HTMLNode(tag="ul", value=ul_value, children=html_node_children)
        case BlockType.ORDERED_LIST:
            ...

        
def find_children_in_block_text(block_text: str):
    block_text_to_text_nodes = text_to_textnodes(block_text)
    html_nodes = []
    for node in block_text_to_text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes