import unittest
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode
from texttype import TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_function_works(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"_",TextType.ITALIC)
        print(new_nodes)

if __name__ == "__main__":
    unittest.main()