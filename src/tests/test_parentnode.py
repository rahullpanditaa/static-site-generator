import unittest
from project.parentnode import ParentNode
from project.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_single_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_multiple_children(self):
        child_node1 = LeafNode("b", "Bold text")
        child_node2 = LeafNode(None, "Normal text")
        child_node3 = LeafNode("a", "This is a link", {"href":"https://www.blahblah.com"})
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<a href=\"https://www.blahblah.com\">This is a link</a></p>"
        )

    def test_to_html_grandchildren(self):
        grandchild_node1 = LeafNode("b", "this is a grandchild node")
        grandchild_node2 = LeafNode("a", "This is another grandchild node", {"target":"_blank"})
        child_node = ParentNode("div", [grandchild_node1, grandchild_node2])
        parentnode = ParentNode("div", [child_node])
        self.assertEqual(
            parentnode.to_html(),
            "<div><div><b>this is a grandchild node</b><a target=\"_blank\">This is another grandchild node</a></div></div>"
        )

    def test_to_html_no_children(self):
        parentnode = ParentNode(tag="b", children=[])
        with self.assertRaises(ValueError):
            parentnode.to_html()

    def test_to_html_no_tag(self):
        parentnode = ParentNode(tag=None, children=[LeafNode("b", "BOLD"), LeafNode("i", "italics")])
        with self.assertRaises(ValueError):
            parentnode.to_html()

if __name__ == "__main__":
    unittest.main()