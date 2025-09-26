from project.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Error: Parent Node must have a tag.")
        if not self.children:
            raise ValueError("Error: Parent node must have child nodes, given None")
        
        children_html_str = ""
        for child in self.children:
            children_html_str += child.to_html()

        return f"<{self.tag}>{children_html_str}</{self.tag}>"