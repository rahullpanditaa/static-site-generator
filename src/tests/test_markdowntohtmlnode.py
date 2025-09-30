import unittest
from project.markdowntohtml import markdown_to_html_node
from project.texttotextnodes import text_to_textnodes
from project.textnode_to_htmlnode import text_node_to_html_node
from project.textnode import TextNode, TextType

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(html)
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_block(self):
        md1 = """
# heading one"""
        md2 = """
## heading level two"""
        md3 = """
### heading level three"""
        md4 = """
#### heading level four"""
        md5 = """
##### heading level 5 with **bold** text inside"""
        md6 = """
###### heading level 6 with **bold** and _italics_ text"""

        node1 = markdown_to_html_node(md1)
        html1 = node1.to_html()

        node2 = markdown_to_html_node(md2)
        html2 = node2.to_html()

        node3 = markdown_to_html_node(md3)
        html3 = node3.to_html()

        node4 = markdown_to_html_node(md4)
        html4 = node4.to_html()

        node5 = markdown_to_html_node(md5)
        html5 = node5.to_html()

        node6 = markdown_to_html_node(md6)
        html6 = node6.to_html()

        self.assertEqual(html1, "<div><h1>heading one</h1></div>")
        self.assertEqual(html2, "<div><h2>heading level two</h2></div>")
        self.assertEqual(html3, "<div><h3>heading level three</h3></div>")
        self.assertEqual(html4, "<div><h4>heading level four</h4></div>")
        self.assertEqual(html5, "<div><h5>heading level 5 with <b>bold</b> text inside</h5></div>")
        self.assertEqual(html6, "<div><h6>heading level 6 with <b>bold</b> and <i>italics</i> text</h6></div>")

    def test_ordered_list_block(self):
        md = """
1. first item in this ordered list
2. second item
3. this item has some **bold** text inside
4. here's some _italics_, some **bold**, and a little bit of `inline code`
5. test this bitch"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
                         "<div><ol><li>first item in this ordered list</li><li>second item</li><li>this item has some <b>bold</b> text inside</li><li>here's some <i>italics</i>, some <b>bold</b>, and a little bit of <code>inline code</code></li><li>test this bitch</li></ol></div>")
        
    def test_unordered_list_block(self):
        md = """
- item one
- item 2 with some **bold** text
- item 3 with some _italics_ and `code` inside"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
                         "<div><ul><li>item one</li><li>item 2 with some <b>bold</b> text</li><li>item 3 with some <i>italics</i> and <code>code</code> inside</li></ul></div>")
        



if __name__ == "__main__":
    unittest.main()