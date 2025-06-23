import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_node_output_generation(self):
        md = """
This is **bolded** paragraph
text in a p tag here

This is another paragraph with _italic_ text and some `code` here

- ul item1
- ul item 2
- ul item 3

1. ol item1
2. ol item 2

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)