def markdown_to_blocks(markdown: str):
    # arg - raw markdown string
    # return - list of block strings
    # every block is separated by a single blank line \n
    blocks = markdown.split("\n\n") #\n at end of line plus next blank line
    result = [block.strip() for block in blocks if block.strip()]
    return result

