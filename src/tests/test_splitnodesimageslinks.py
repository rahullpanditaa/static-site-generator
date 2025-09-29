import unittest
from project.splitnodesimageslinks import split_nodes_image, split_nodes_links
from project.textnode import TextNode, TextType

class TestSplitNodesImagesLinks(unittest.TestCase):
    def test_single_img_in_single_node(self):
        node = TextNode("This is plain text with ![img-alt-text](https://www.linktoimg.com) inside it", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes,
                             [
                                 TextNode("This is plain text with ", TextType.PLAIN),
                                 TextNode("img-alt-text", TextType.IMAGE, "https://www.linktoimg.com"),
                                 TextNode(" inside it", TextType.PLAIN)
                             ])
        
    def test_multiple_img_nodes(self):
        node = TextNode("This text has multiple imgs, First img ![img-alt-text-one](https://www.linktoimgone.com) and second ![alt-text-two](www.img2.com)", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes,
                             [
                                 TextNode("This text has multiple imgs, First img ", TextType.PLAIN),
                                 TextNode("img-alt-text-one", TextType.IMAGE, "https://www.linktoimgone.com"),
                                 TextNode(" and second ", TextType.PLAIN),
                                 TextNode("alt-text-two", TextType.IMAGE, "www.img2.com")
                             ])
        
if __name__ == "__main__":
    unittest.main()