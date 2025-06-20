from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "**bold**"
    ITALIC = "_italic_"
    CODE = "`code`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"
