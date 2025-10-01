import unittest
from project.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def extract_h1_at_start(self):
        md = """
# This is heading level one

This is a plain paragraph block
with some inline `code` and **bold** text"""
        title = extract_title(md)
        self.assertEqual(title, "This is heading level one")

    def extract_h1(self):
        md = """
```
def main():
    return input("What's your name? ").strip()
    
### heading level 3

# H1"""

        title = extract_title(md=md)
        self.assertEqual(title, "H1")

    def no_h1(self):
        md = """
## h2

### heading three

#incorrect h1"""
        with self.assertRaises(ValueError):
            extract_title(md=md)