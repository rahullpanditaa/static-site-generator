import unittest
from block_to_block_type import block_to_block_type
from blocktype import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        md = """# heading 1"""
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        md = """```
        def sum(a,b):
            return a + b
            ```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_block_to_block_type_code(self):
        md = """> what a beautiful quote
        > another beautiful quote
        > quote number 3"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_block_to_block_type_ul(self):
        md = """- item 1
        - item 2
        - item 3"""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ul(self):
        md = """1. item 1
        2. item 2
        3. item 3"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
