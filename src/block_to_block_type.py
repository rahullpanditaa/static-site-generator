import re
from blocktype import BlockType

def block_to_block_type(block):
    if re.search(r"^#{1,6} .+$", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    else:
        lines = block.split("\n")
        if all(line.startswith(">") for line in lines):
            return BlockType.QUOTE
        elif all(line.startswith("- ") for line in lines):
            return BlockType.UNORDERED_LIST
        elif all(re.match(r"^[1-9]+\. .+$", line) for line in lines):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH



