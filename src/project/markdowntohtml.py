import re
from project.markdowntoblocks import markdown_to_blocks
from project.blocktoblocktype import block_to_block_type, BlockType
from project.parentnode import ParentNode
from project.leafnode import LeafNode
from project.texttotextnodes import text_to_textnodes
from project.textnode_to_htmlnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    # split the entire md document into blocks
    # each block will have the md text eg. - for ul, # for headings
    blocks = markdown_to_blocks(markdown)

    html_nodes = []

    # loop over each block
    for block in blocks:
        # determine the type of current blcok
        block_type = block_to_block_type(block)

        # create a new HTML node (Parent Node, LeafNode, )
        html_block_node = create_new_html_block_node(block, block_type)
        html_nodes.append(html_block_node)
    return ParentNode(tag="div", children=html_nodes)


def create_new_html_block_node(block_text: str, block_type: BlockType):
    match block_type:
        case BlockType.HEADING:
            heading_text = re.sub(r"^#{1,6} ", "", block_text)
            heading_level = len(block_text) - len(block_text.lstrip("#"))            
            block_node = ParentNode(tag=f"h{heading_level}", children=create_child_nodes_from_text(heading_text))
            return block_node
        case BlockType.PARAGRAPH:
            return ParentNode(tag="p", children=create_child_nodes_from_text(block_text))
        case BlockType.UNORDERED_LIST:
            ul = block_text.splitlines()
            ul_items = []
            for li in ul:
                cleaned_item = li.removeprefix("- ")
                children = create_child_nodes_from_text(cleaned_item)
                ul_items.append(ParentNode(tag="li", children=children))
            return ParentNode(tag="ul", children=ul_items)
        case BlockType.ORDERED_LIST:
            ol = block_text.splitlines()
            ol_items = []
            for li in ol:
                cleaned_item = re.sub(r"^\d{1,}\. ", "", li)
                children = create_child_nodes_from_text(cleaned_item)
                ol_items.append(ParentNode(tag="li", children=children))
            return ParentNode(tag="ol", children=ol_items)
        case BlockType.QUOTE:
            quote = block_text.splitlines()
            quote_lines = []
            for line in quote:
                cleaned_item = re.sub(r"^> *", "", line).rstrip()
                quote_lines.append(cleaned_item)
            quote_text = "\n".join(quote_lines)
            quote_children = create_child_nodes_from_text(quote_text)
            return ParentNode(tag="blockquote", children=quote_children)
        case BlockType.CODE:
            code_text = block_text.lstrip("```").rstrip("```").strip()
            code_node = LeafNode(tag="code", value=code_text + "\n")
            return ParentNode(tag="pre", children=[code_node])



def create_child_nodes_from_text(block_text: str):
    text_nodes = text_to_textnodes(block_text)

    leaf_nodes = []
    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))

    return leaf_nodes # inline markdown text as html leaf nodes
    



        
