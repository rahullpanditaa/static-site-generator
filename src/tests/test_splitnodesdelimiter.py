import unittest
from project.split_nodes_delimiter import split_nodes_delimiter
from project.textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delim(self):
        node = TextNode("This is text with `code block` inside it.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" inside it.", TextType.PLAIN)
        ])

    def test_bold_delim(self):
        node = TextNode("This is text with a **bold** word inside it.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is text with a ", TextType.PLAIN),
                             TextNode("bold", TextType.BOLD),
                             TextNode(" word inside it.", TextType.PLAIN)
                         ])
    
    def test_italics_delim(self):
        node = TextNode("There are words in _italics_ in here.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, 
                         [
                             TextNode("There are words in ", TextType.PLAIN),
                             TextNode("italics", TextType.ITALIC),
                             TextNode(" in here.", TextType.PLAIN)
                         ])
    
    def test_multiple_italics_delims_in_single_node(self):
        node = TextNode("This is plain text with _italics1_ and _italics2_ inside", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is plain text with ", TextType.PLAIN),
                             TextNode("italics1", TextType.ITALIC),
                             TextNode(" and ", TextType.PLAIN),
                             TextNode("italics2", TextType.ITALIC),
                             TextNode(" inside", TextType.PLAIN)
                         ])
        
    def test_multiple_bold_delims_in_single_node(self):
        node = TextNode("This is plain text with **bold1** and **bold2** inside", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is plain text with ", TextType.PLAIN),
                             TextNode("bold1", TextType.BOLD),
                             TextNode(" and ", TextType.PLAIN),
                             TextNode("bold2", TextType.BOLD),
                             TextNode(" inside", TextType.PLAIN)
                         ])
        
    def test_multiple_code_delims_in_single_node(self):
        node = TextNode("This is plain text with `code` and `code2` inside", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is plain text with ", TextType.PLAIN),
                             TextNode("code", TextType.CODE),
                             TextNode(" and ", TextType.PLAIN),
                             TextNode("code2", TextType.CODE),
                             TextNode(" inside", TextType.PLAIN)
                         ])
        
    def test_different_delims_in_single_node(self):
        node = TextNode("This is plain text with `code` inside it, as well as _italics_ and **bold** text.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is plain text with ", TextType.PLAIN),
                             TextNode("code", TextType.CODE),
                             TextNode(" inside it, as well as ", TextType.PLAIN),
                             TextNode("italics", TextType.ITALIC),
                             TextNode(" and ", TextType.PLAIN),
                             TextNode("bold", TextType.BOLD),
                             TextNode(" text.", TextType.PLAIN)
                         ])
        
    def test_multiple_delims_multiple_nodes(self):
        node1 = TextNode("This is plain text with `code` inside it, as well as _italics_ and **bold** text.", TextType.PLAIN)
        # node2 = TextNode("`there is only code here`", TextType.CODE)
        # node3 = TextNode("_only italics_", TextType.ITALIC)
        node4 = TextNode("Plain text. Completely plain. Oh wait! some **bold** text, as well as some _italics_. Have fun testing this.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node1, node4], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is plain text with ", TextType.PLAIN),
                             TextNode("code", TextType.CODE),
                             TextNode(" inside it, as well as ", TextType.PLAIN),
                             TextNode("italics", TextType.ITALIC),
                             TextNode(" and ", TextType.PLAIN),
                             TextNode("bold", TextType.BOLD),
                             TextNode(" text.", TextType.PLAIN),
                            #  TextNode("there is only code here", TextType.CODE),
                            #  TextNode("only italics", TextType.ITALIC),
                             TextNode("Plain text. Completely plain. Oh wait! some ", TextType.PLAIN),
                             TextNode("bold", TextType.BOLD),
                             TextNode(" text, as well as some ", TextType.PLAIN),
                             TextNode("italics", TextType.ITALIC),
                             TextNode(". Have fun testing this.", TextType.PLAIN)
                         ])


if __name__ == "__main__":
    unittest.main()