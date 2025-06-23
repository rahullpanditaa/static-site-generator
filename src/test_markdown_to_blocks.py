import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, 
                         [
                             "This is **bolded** paragraph",
                             "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                             "- This is a list\n- with items"
                         ])


    def test_markdown_to_blocks_two(self):
        md = """
# This is a heading

This is a paragraph of text with some **bold** and _italic_ text
Same paragraph continued


- List item one
- List item two
- List item three

"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         [
                             "# This is a heading",
                             "This is a paragraph of text with some **bold** and _italic_ text\nSame paragraph continued",
                             "- List item one\n- List item two\n- List item three"
                         ])