import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_nodes(self):
        html_node_one = HTMLNode("p", "This is a paragraph", props={"href":"https://www.razumikhin.com"})
        html_node_two = HTMLNode()
        self.assertNotEqual(html_node_one, html_node_two)

if __name__ == "__main__":
    unittest.main()