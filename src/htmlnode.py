
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        properties = ""

        for prop in self.props:
            properties += f"{prop}=\"{self.props[prop]}\" "

        return properties
    
    def __repr__(self):
        return f"HTML Node(Tag : {self.tag}; Value: {self.value}; Children: {self.children}; Properties: {self.props_to_html()})"