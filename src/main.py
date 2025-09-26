from project.textnode import TextNode, TextType

def main():
    textnode = TextNode("anchor text", TextType.LINK, "www.boot.dev")
    print(textnode)

if __name__ == "__main__":
    main()