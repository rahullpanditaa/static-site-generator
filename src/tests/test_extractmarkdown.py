import unittest
from project.extractlinks import extract_markdown_images, extract_markdown_links

class TestExtractLinks(unittest.TestCase):
    def test_extract_single_img(self):
        text = "This text has ![image alt text](https://www/linktoanimge.com/blah)"
        links = extract_markdown_images(text)
        self.assertListEqual(links,
                         [
                             ("image alt text", "https://www/linktoanimge.com/blah")
                         ])
        
    def test_extract_multiple_imgs(self):
        text = "Several images are in this text. This one ![alt text one](www.blahblah.gov.in) and this one ![alt text two](www.gurgaonrocks.com)"
        links = extract_markdown_images(text)
        self.assertListEqual(links, 
                         [
                             ("alt text one", "www.blahblah.gov.in"),
                             ("alt text two", "www.gurgaonrocks.com")
                         ])
        
    def test_extract_links(self):
        text = "There is a link here [anchor text](www.hshsh.com) and another [anchor text again](https://www.publichost.com)"
        links = extract_markdown_links(text)
        self.assertListEqual(links, 
                             [
                                 ("anchor text", "www.hshsh.com"),
                                 ("anchor text again", "https://www.publichost.com")
                             ])
        

if __name__ == "__main__":
    unittest.main()