from project.extractlinks import extract_markdown_links, extract_markdown_images
from project.textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        old_node_text = node.text
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        links_img = extract_markdown_images(old_node_text)

        for img in links_img:
            current_node_contents = old_node_text.split(f"![{img[0]}]({img[1]})", 1)
            if len(current_node_contents) != 2:  
                raise ValueError("Error: Invalid markdown.")
            if current_node_contents[0]:
                new_nodes.append(TextNode(current_node_contents[0], TextType.PLAIN))
            img_node = TextNode(img[0], TextType.IMAGE, img[1])
            new_nodes.append(img_node)
            old_node_text = current_node_contents[1]
        
        if old_node_text:
            new_nodes.append(TextNode(old_node_text, TextType.PLAIN))
    return new_nodes



        

def split_nodes_links(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        old_node_text = node.text
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        text_links = extract_markdown_links(old_node_text)

        for link in text_links:
            current_node_contents = old_node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(current_node_contents) != 2:
                raise ValueError("Error: Invalid markdown.")
            if current_node_contents[0]:
                new_nodes.append(TextNode(current_node_contents[0], TextType.PLAIN))
            link_node = TextNode(link[0], TextType.LINK, link[1])
            new_nodes.append(link_node)
            old_node_text = current_node_contents[1]

        if old_node_text:
            new_nodes.append(TextNode(old_node_text, TextType.PLAIN))
        
    return new_nodes