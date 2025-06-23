import re
from blocktype import BlockType

def block_to_block_type(block):
    if re.search(r"^#{1,6} .+$", block):
        return BlockType.HEADING
    elif block.lstrip().startswith("```") and block.rstrip().endswith("```"):
        return BlockType.CODE
    else:
        lines = block.split("\n")
        if all(re.match(r"^>\s*.+$", line.strip()) for line in lines):
            return BlockType.QUOTE
        elif all(line.strip().startswith("- ") for line in lines):
            return BlockType.UNORDERED_LIST
        elif all(re.match(r"^[1-9]+\. .+$", line.strip()) for line in lines):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH



