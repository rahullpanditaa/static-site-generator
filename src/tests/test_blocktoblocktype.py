import unittest
from project.blocktoblocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        h1 = """
# Heading one"""
        h2 = """
## h2"""
        h3 = """
### h3"""
        h4 = """
#### heading four"""
        h5 = """
##### heading level 5"""
        h6 = """
###### heading 6"""
        t1 = block_to_block_type(h1.strip())
        t2 = block_to_block_type(h2.strip())
        t3 = block_to_block_type(h3.strip())
        t4 = block_to_block_type(h4.strip())
        t5 = block_to_block_type(h5.strip())
        t6 = block_to_block_type(h6.strip())
        self.assertEqual(t1, BlockType.HEADING)
        self.assertEqual(t2, BlockType.HEADING)
        self.assertEqual(t3, BlockType.HEADING)
        self.assertEqual(t4, BlockType.HEADING)
        self.assertEqual(t5, BlockType.HEADING)
        self.assertEqual(t6, BlockType.HEADING)

    def test_code_block(self):
        c1 = """
```def main():
       return input("Enter name: ").strip()```"""
        c2 = """
```def add(x, y):
        return x + y
```"""
        c3 = """
```
def subtract(x, y):
    return x - y```"""
        t1 = block_to_block_type(c1.strip())
        t2 = block_to_block_type(c2.strip())
        t3 = block_to_block_type(c3.strip())
        self.assertEqual(t1, BlockType.CODE)
        self.assertEqual(t2, BlockType.CODE)
        self.assertEqual(t3, BlockType.CODE)

    def test_quote_block(self):
        q1 = """
>quote line 1
> quote line 2
>  quote line 3
>   quote line 4"""
        t1 = block_to_block_type(q1.strip())
        self.assertEqual(t1, BlockType.QUOTE)

    def test_unordered_list_block(self):
        ul_valid = """
- item one
- item two
- item number three"""
        ul_invalid = """
-item one
- item2
-   item3"""
        t_valid = block_to_block_type(ul_valid.strip())
        t_invalid = block_to_block_type(ul_invalid.strip())
        self.assertEqual(t_valid, BlockType.UNORDERED_LIST)
        self.assertEqual(t_invalid, BlockType.PARAGRAPH)

    def test_ordered_list_block(self):
        ol_valid = """
1. python
2. go
3. java"""
        ol_invalid_numbering = """
1. Go
3. Python
2. Java
1. Javascript (lol never)
6. C++"""
        ol_invalid_space_format = """
1. Python
2. Go
3.Java"""
        t_valid = block_to_block_type(ol_valid.strip())
        t_invalid_numbering = block_to_block_type(ol_invalid_numbering.strip())
        t_invalid_spacing = block_to_block_type(ol_invalid_space_format.strip())
        self.assertEqual(t_valid, BlockType.ORDERED_LIST)
        self.assertEqual(t_invalid_numbering, BlockType.PARAGRAPH)
        self.assertEqual(t_invalid_spacing, BlockType.PARAGRAPH)
    
    def test_paragraph_block(self):
        para = """
This is a paragraph with multiple lines
another line
one more line biatch!!!
1. this ordered list line won't count
- same goes for this unordered list
>and this quote"""
        t = block_to_block_type(para.strip())
        self.assertEqual(t, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

