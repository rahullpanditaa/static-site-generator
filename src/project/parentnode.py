from project.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        # can add these checks to setters for fields if needed
        if not self.tag:
            raise ValueError("Error: Parent Node must have a tag.")
        
        if not isinstance(self.children,list):
            raise ValueError("Error: Parent node must have child nodes, given None")
        
        if len(self.children) == 0:
            raise ValueError("Error: Parent node must have child nodes, given None")    
            
        children_html_str = ""
        for child in self.children:
            children_html_str += child.to_html()

        return f"<{self.tag}>{children_html_str}</{self.tag}>"