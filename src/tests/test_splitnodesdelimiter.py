import unittest
from project.split_nodes_delimiter import split_nodes_delimiter
from project.textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delim(self):
        node = TextNode("This is text with `code block` inside it.", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" inside it.", TextType.PLAIN)
        ])


if __name__ == "__main__":
    unittest.main()