import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# heading one    

this is a paragraph """
        self.assertEqual(extract_title(md), "heading one")