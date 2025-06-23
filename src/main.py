from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType

def main():
    md = """
``` 
def sum(a,b):
    return a + b
```
"""
    blocks = markdown_to_blocks(md)
    print(blocks)
    
    
    

if __name__ == "__main__":
    main()