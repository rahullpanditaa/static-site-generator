
def markdown_to_blocks(markdown):
    blocks_ = markdown.split("\n\n")
    blocks = list(map(lambda s: s.strip(), blocks_))
    try:
        blocks.remove("")
    except ValueError:
        pass
    return blocks