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
        
    def test_single_link_in_single_node(self):
        node = TextNode("This is plain text with [link-text](https://www.aurl.com) inside it", TextType.PLAIN)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(new_nodes,
                             [
                                 TextNode("This is plain text with ", TextType.PLAIN),
                                 TextNode("link-text", TextType.LINK, "https://www.aurl.com"),
                                 TextNode(" inside it", TextType.PLAIN)
                             ])
        
    def test_multiple_links_in_single_node(self):
        node = TextNode("This is plain text with [link-text](https://www.aurl.com) inside it. Another one [link-text-2](www.blah.com)", TextType.PLAIN)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(new_nodes,
                             [
                                 TextNode("This is plain text with ", TextType.PLAIN),
                                 TextNode("link-text", TextType.LINK, "https://www.aurl.com"),
                                 TextNode(" inside it. Another one ", TextType.PLAIN),
                                 TextNode("link-text-2", TextType.LINK, "www.blah.com")
                             ])
        
    def test_multiple_nodes_with_imgs(self):
        node1 = TextNode("This text has one img inside it : ![alt-text](https://www.imgurl.com)", TextType.PLAIN)
        node2 = TextNode("PSYCH! No images, only plain text", TextType.PLAIN)
        node3 = TextNode("Two images bitch!! First img ![img-one](www.imgone.com), and second ![img-2](https://imgtwo.com)", TextType.PLAIN)
        new_nodes = split_nodes_image([node1, node2, node3])
        self.assertListEqual(new_nodes,
                             [
                                 TextNode("This text has one img inside it : ", TextType.PLAIN),
                                 TextNode("alt-text", TextType.IMAGE, "https://www.imgurl.com"),
                                 TextNode("PSYCH! No images, only plain text", TextType.PLAIN),
                                 TextNode("Two images bitch!! First img ", TextType.PLAIN),
                                 TextNode("img-one", TextType.IMAGE, "www.imgone.com"),
                                 TextNode(", and second ", TextType.PLAIN),
                                 TextNode("img-2", TextType.IMAGE, "https://imgtwo.com"),
                             ])
        
    def test_multiple_nodes_with_links(self):
        node1 = TextNode("This text has one link inside it : [link-text](https://www.url.com)", TextType.PLAIN)
        node2 = TextNode("PSYCH! No LINKS, only plain text", TextType.PLAIN)
        node3 = TextNode("Two LINKS bitch!! First LINK [Link-one](www.blahblah.com), and second [LINK-2](https://sixtyeight.com)", TextType.PLAIN)
        new_nodes = split_nodes_links([node1, node2, node3])
        self.assertListEqual(new_nodes,
                             [
                                 TextNode("This text has one link inside it : ", TextType.PLAIN),
                                 TextNode("link-text", TextType.LINK, "https://www.url.com"),
                                 TextNode("PSYCH! No LINKS, only plain text", TextType.PLAIN),
                                 TextNode("Two LINKS bitch!! First LINK ", TextType.PLAIN),
                                 TextNode("Link-one", TextType.LINK, "www.blahblah.com"),
                                 TextNode(", and second ", TextType.PLAIN),
                                 TextNode("LINK-2", TextType.LINK, "https://sixtyeight.com"),
                             ])
    
    # def test_no_img_links_inside_plain_text(self):
    #     node1 = TextNode("`code block`", TextType.CODE)
    #     node2 = TextNode("img-alt-text", TextType.IMAGE, "www.img.com")
    #     node3 = TextNode("Plain text with **bold** and _italics_ text inside", TextType.PLAIN)
    #     new_nodes = split_nodes_image([node1, node2, node3])
    #     new_nodes = split_nodes_links(new_nodes)
    #     self.assertListEqual(new_nodes,
    #                          [
    #                              TextNode("code block", TextType.CODE),
    #                              TextNode("img-alt-text", TextType.IMAGE, "www.img.com"),
    #                              TextNode("Plain text with **bold** and _italics_ text inside", TextType.PLAIN)
    #                          ])
        
if __name__ == "__main__":
    unittest.main()