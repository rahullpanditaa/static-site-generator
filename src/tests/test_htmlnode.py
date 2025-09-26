import unittest
from project.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode("p", "This is a paragraph", props={"href":"https://www.google.com", "target":"_blank"})
        htmlnode_attributes = htmlnode.props_to_html()
        self.assertEqual(htmlnode_attributes,  ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_none(self):
        htmlnode = HTMLNode()
        attr = htmlnode.props_to_html()
        self.assertEqual(attr, "")





if __name__ == "__main__":
    unittest.main()