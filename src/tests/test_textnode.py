import unittest

from project.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("A text node", TextType.BOLD)
        node2 = TextNode("A text node", TextType.BOLD)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()