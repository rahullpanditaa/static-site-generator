import unittest
from project.textnode_to_htmlnode import text_node_to_html_node
from project.textnode import TextNode, TextType
from project.htmlnode import HTMLNode
from project.leafnode import LeafNode

class TestTextNodetoHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a Bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(type(html_node), LeafNode)
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.value, "This is a Bold text node")

    def test_italics(self):
        node = TextNode("This is an italics text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.children, None)
    
    def test_code(self):
        node = TextNode("This is an code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.value, "This is an code text node")

    def test_link(self):
        node = TextNode("This is an anchor tag text node", TextType.LINK, "https://www.blahblah.com/api/2.0")
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag, "a")
        self.assertEqual(htmlnode.value, "This is an anchor tag text node")
        self.assertEqual(htmlnode.props, {"href": "https://www.blahblah.com/api/2.0"})
    
    def test_img(self):
        node = TextNode("This is an img tag text node", TextType.IMAGE, "https://www.beautifulpictures.com/koalabears/2.jpeg")
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.tag, "img")
        self.assertEqual(htmlnode.value, "")
        self.assertEqual(htmlnode.children, None)
        self.assertEqual(htmlnode.props, {"src": "https://www.beautifulpictures.com/koalabears/2.jpeg", "alt": "This is an img tag text node"})


if __name__ == "__main__":
    unittest.main()