import unittest
from split_images_and_links import split_nodes_image, split_nodes_link
from textnode import TextNode
from texttype import TextType

class TestSplitImagesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode("some text with ![image](www.blah.com)", TextType.TEXT)

        nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("some text with ", TextType.TEXT),
                              TextNode("image", TextType.IMAGE, "www.blah.com")],
                              nodes)