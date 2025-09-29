import unittest
from project.markdowntoblocks import markdown_to_blocks

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
            self.assertEqual(
                blocks,
                    [
                        "This is **bolded** paragraph",
                        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                        "- This is a list\n- with items",
                    ],
                )
            
        def test_markdown_excessive_newlines(self):
              md = """
1. This is an ordered list
2. item two
3. another item


This is **bold** text inside a paragraph

- unordered list item one
- unordered list item two
- unordered list item three



"""
              blocks = markdown_to_blocks(md)
              self.assertListEqual(blocks, 
                                   [
                                         "1. This is an ordered list\n2. item two\n3. another item",
                                         "This is **bold** text inside a paragraph",
                                         "- unordered list item one\n- unordered list item two\n- unordered list item three"
                                   ])
            
if __name__ == "__main__":
      unittest.main()