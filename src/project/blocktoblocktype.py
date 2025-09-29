import re
from project.blocktypes import BlockType

def block_to_block_type(md: str):
    # arg - single block of md text as str
    # returns -> BlockType representing type of arg block
    if is_block_heading(md):
        return BlockType.HEADING
    if is_block_code(md):
        return BlockType.CODE
    if is_block_quote(md):
        return BlockType.QUOTE
    if is_block_ul(md):
        return BlockType.UNORDERED_LIST
    if is_block_ol(md):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def is_block_heading(block: str):
    return block.startswith(("# ", "## ", "### ", "#### ", "##### ", "##### ", "###### "))

def is_block_code(block: str):
    return block.startswith("```") and block.endswith("```")

def is_block_quote(block: str):
    lines = block.splitlines()
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def is_block_ul(block: str):
    lines = block.splitlines()
    for line in lines:
        if not line.startswith("- "):
            return False
    return True

def is_block_ol(block: str):
    lines = block.splitlines()

    for index, line in enumerate(lines):
        if not line[0].isdigit() or line[1:3] != ". ":
            return False
        if int(line[0]) != index + 1:
            return False
    return True
        
        