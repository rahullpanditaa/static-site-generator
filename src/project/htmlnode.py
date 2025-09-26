class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # getter for tag
    @property
    def tag(self):
        return self._tag
    
    # setter for tag
    @tag.setter
    def tag(self, tag):
        self._tag = tag

    # getter for value
    @property
    def value(self):
        return self._value
    
    # setter for value
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def children(self):
        return self._children #list of html node objects or None
    
    @children.setter
    def children(self, children):
        if (children and isinstance(children, list)) or children == None:
            self._children = children
    
    @property
    def props(self):
        return self._props
    
    @props.setter
    def props(self, props):
        if (props and isinstance(props, dict)) or props == None:
            self._props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            html_node_atributes = ""
            for (k, v) in self.props.items():
                html_node_atributes += f' {k}="{v}"'
            return html_node_atributes
        return None
    
    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props_to_html()})"