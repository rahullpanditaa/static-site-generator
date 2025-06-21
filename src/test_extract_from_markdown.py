import unittest
from extract_from_markdown import extract_markdown_images,extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        text = "Some text with ![image alt text 1](www.hfirhvrifhr.com) and another image ![blah blah](www.frbuvrb.com)"
        self.assertEqual(extract_markdown_images(text), [("image alt text 1", "www.hfirhvrifhr.com"), ("blah blah", "www.frbuvrb.com")])

    def test_extract_links(self):
        text ="Some text with some links such as [pfrfrf bad](www.wikipediablah.com), link 2 [reading is good](www.fnrifnrifn.com)"
        self.assertEqual(extract_markdown_links(text), [("pfrfrf bad", "www.wikipediablah.com"), ("reading is good", "www.fnrifnrifn.com")])