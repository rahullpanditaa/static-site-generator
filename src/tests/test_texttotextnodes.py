import unittest
from project.texttotextnodes import text_to_textnodes
from project.textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text_only(self):
        text = "This text has no other types inside"
        text_nodes = text_to_textnodes(text)
        self.assertListEqual(text_nodes, 
                             [
                                 TextNode("This text has no other types inside", TextType.PLAIN)
                             ])
    
    def test_multiple_delims(self):
        text = "This text has `code block`, as well as some **bold** and _italics_ text inside"
        text_nodes = text_to_textnodes(text)
        self.assertListEqual(text_nodes, 
                             [
                                 TextNode("This text has ", TextType.PLAIN),
                                 TextNode("code block", TextType.CODE),
                                 TextNode(", as well as some ", TextType.PLAIN),
                                 TextNode("bold", TextType.BOLD),
                                 TextNode(" and ", TextType.PLAIN),
                                 TextNode("italics", TextType.ITALIC),
                                 TextNode(" text inside", TextType.PLAIN)
                             ])
        
    def test_multiple_delims_imgs_links(self):
        text = "This text has some images : ![alt-text](www.imgurl.com), some links : [link-text](https://www.blah.com), as well as a `code` block and _italics_ text"
        text_nodes = text_to_textnodes(text)
        self.assertListEqual(text_nodes, 
                             [
                                 TextNode("This text has some images : ", TextType.PLAIN),
                                 TextNode("alt-text", TextType.IMAGE, url="www.imgurl.com"),
                                 TextNode(", some links : ", TextType.PLAIN),
                                 TextNode("link-text", TextType.LINK, url="https://www.blah.com"),
                                 TextNode(", as well as a ", TextType.PLAIN),
                                 TextNode("code", TextType.CODE),
                                 TextNode(" block and ", TextType.PLAIN),
                                 TextNode("italics", TextType.ITALIC),
                                 TextNode(" text", TextType.PLAIN)
                             ])
        
    def test_multiple_delims_two(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        self.assertListEqual(text_nodes, 
                             [
                                TextNode("This is ", TextType.PLAIN),
                                TextNode("text", TextType.BOLD),
                                TextNode(" with an ", TextType.PLAIN),
                                TextNode("italic", TextType.ITALIC),
                                TextNode(" word and a ", TextType.PLAIN),
                                TextNode("code block", TextType.CODE),
                                TextNode(" and an ", TextType.PLAIN),
                                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                TextNode(" and a ", TextType.PLAIN),
                                TextNode("link", TextType.LINK, "https://boot.dev"), 
                             ])
        

if __name__ == "__main__":
    unittest.main()