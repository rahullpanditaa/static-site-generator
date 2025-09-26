import unittest
from project.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_attr(self):
        node = LeafNode("p", "This is a paragraph", {"a1" : "v1"})
        self.assertEqual(node.to_html(), "<p a1=\"v1\">This is a paragraph</p>")

if __name__ == "__main__":
    unittest.main()