import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_node_output_generation(self):
        md = """
# heading 1

## heading 2

This is **bolded** paragraph
text in a p tag here

This is another paragraph with _italic_ text and some `code` here

- ul item1
- ul item 2
- ul item 3

1. ol item1
2. ol item 2

"""
        # node = markdown_to_html_node(md)
        # html = node.to_html()
        # print(html)

    
    def test_markdown_to_html_codeblock(self):
        md = """
```
This is text that _should_ remain
the same **even** with inline stuff
```
"""
        node = markdown_to_html_node(md)
        print(node.to_html())