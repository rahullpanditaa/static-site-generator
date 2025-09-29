import re
from project.blocktypes import BlockType

def block_to_block_type(md: str):
    # arg - single block of md text as str
    # returns -> BlockType representing type of arg block
    ...

def is_block_heading(block):
    if matches := re.search(r"^#{1,6} .+$", block):
        return True
    return False

def is_block_code(block: str):
    return block.startswith("```") and block.endswith("```")

def is_block_code(block: str):
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
        
        