from project.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag != "code":
            self.value = self.value.replace("\n", " ")
        if not self.tag:
            return f"{self.value}"
        if not self.value and self.tag != "img":
            raise ValueError("Error: Leaf node must have a value.")
        
        return f"<{self.tag}{self.props_to_html()}>{self.value if self.value else ""}</{self.tag}>"