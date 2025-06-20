from textnode import TextNode, TextType

def main():
    text_node = TextNode("anchor text", TextType.LINK, "www.ddd.com")
    print(text_node)

if __name__ == "__main__":
    main()