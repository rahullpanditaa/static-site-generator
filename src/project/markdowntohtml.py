import re
from project.markdowntoblocks import markdown_to_blocks
from project.blocktoblocktype import block_to_block_type, BlockType
from project.htmlnode import HTMLNode
from project.parentnode import ParentNode
from project.leafnode import LeafNode
from project.textnode import TextNode, TextType
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
                item = li.removeprefix("- ")
                item = f"<li>{item}</li>"
                ul_items.append(item)
            ul_list = "\n".join(ul_items)
            return ParentNode(tag="ul", children=create_child_nodes_from_text(ul_list))
        case BlockType.ORDERED_LIST:
            ol = block_text.splitlines()
            ol_items = []
            for li in ol:
                item = re.sub(r"^\d{1,} ", "", li)
                item = f"<li>{item}</li>"
                ol_items.append(item)
            ol_list = "\n".join(ol_items)
            return ParentNode(tag="ol", children=create_child_nodes_from_text(ol_list))
        case BlockType.QUOTE:
            quote = block_text.splitlines()
            quote_lines = []
            for line in quote:
                item = line.removeprefix(">")
                quote_lines.append(item)
            complete_quote = "\n".join(quote_lines)
            return ParentNode(tag="blockquote", children=create_child_nodes_from_text(complete_quote))
        case BlockType.CODE:
            code_text = block_text.lstrip("```").rstrip("```").strip()
            code_node = LeafNode(tag="code", value=code_text + "\n")
            return ParentNode(tag="pre", children=[code_node])



def create_child_nodes_from_text(block_text: str):
    # list of TextNodes (smallest inline item) from the block text
    # inline elements include - code, imgs, links, bold, italics
    text_nodes = text_to_textnodes(block_text)

    # now, need to convert text nodes into LeafNodes (HTML Nodes)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))

    return leaf_nodes # inline markdown text as html leaf nodes
    



        
