from enum import Enum

class TextType(Enum):
    PLAIN = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "url"

# represents various types of inline text
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        if not text:
            raise ValueError("Error: Missing text content for the node")
        self._text = text

    @property
    def text_type(self):
        return self._text_type
    
    @text_type.setter
    def text_type(self, text_type):
        if not isinstance(text_type, TextType):
            raise ValueError(f"Error: Invalid text type {text_type} given")
        self._text_type = text_type

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"