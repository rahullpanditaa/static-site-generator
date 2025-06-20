from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    html_node = HTMLNode("p", "This is a paragraph", props={"href":"https://www.blah.com", 
                                                            "target" : "_blank"})
    print(html_node.props_to_html())

if __name__ == "__main__":
    main()