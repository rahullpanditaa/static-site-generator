import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchild(self):
        grandchild = LeafNode("b", "grand child")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span><b>grand child</b></span></div>")