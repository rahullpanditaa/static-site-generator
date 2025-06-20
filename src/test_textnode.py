import unittest

from textnode import TextNode
from texttype import TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node_one = TextNode("some text", TextType.CODE)
        node_two = TextNode("an image", TextType.IMAGE)
        self.assertNotEqual(node_one, node_two)


if __name__ == "__main__":
    unittest.main()