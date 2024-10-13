from textnode import TextNode
from htmlnode import *
from extract_markdown_images import *
from extract_markdown_links import *
from text_types import *

print('hello world')

def main():
    print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    print(HTMLNODE('p', 'test', 'test', '[("class", "ice"), ("id", "cream")]'))
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    extract_markdown_images('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)')
    extract_markdown_links('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)')
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(text_node.text, None)
        case "bold":
            return LeafNode(text_node.text, 'b')
        case "italic":
            return LeafNode(text_node.text, 'i')
        case "code":
            return LeafNode(text_node.text, 'code')
        case "link":
            return LeafNode(text_node.text, 'a', [{"href": text_node.href}])
        case "image":
            return LeafNode('', 'img', [{"src", text_node.url, "alt", text_node.text}])
        case _:
            raise Exception("Invalid text node type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != "text":
            node_list.append(node)
        elif delimiter in node.text:
            node_split = node.text.split(delimiter)
            if len(node_split) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for count, part in enumerate(node_split):
                if count % 2 == 0:
                    node_list.append(TextNode(part, node.text_type))
                else:
                    node_list.append(TextNode(part, text_type))
        else:
            node_list.append(node)
    return node_list

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
        else:
            image_tuples = extract_markdown_images(node.text)
            remaining_text = node.text
            if not image_tuples:
                node_list.append(node)
            else:
                for key,value in image_tuples:
                    split_list = remaining_text.split(f"![{key}]({value})", 1)
                    first_string = split_list[0].strip()
                    if len(split_list) > 1:
                        second_string = split_list[1].strip()
                    if first_string:
                        node_list.append(TextNode(first_string, text_type_text))
                    
                    #append image
                    node_list.append(TextNode(key, text_type_image, value))
                    if len(split_list) > 1:
                        if second_string:
                            remaining_text = second_string
                        if not second_string:
                            remaining_text = ""
            if remaining_text:
                node_list.append(TextNode(remaining_text,text_type_text))
    return node_list


def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
        else:
            link_tuples = extract_markdown_links(node.text)
            remaining_text = node.text
            if not link_tuples:
                node_list.append(node)
            else:
                for key,value in link_tuples:
                    split_list = remaining_text.split(f"[{key}]({value})", 1)
                    first_string = split_list[0].strip()
                    if len(split_list) > 1:
                        second_string = split_list[1].strip()
                    
                    if first_string:
                        node_list.append(TextNode(first_string, text_type_text))
                    
                    #append link
                    node_list.append(TextNode(key, text_type_link, value))
                    if len(split_list) > 1:
                        if second_string:
                            remaining_text = second_string
                        if not second_string:
                            remaining_text = ""
                    else:
                        remaining_text = ""
            if remaining_text:
                node_list.append(TextNode(remaining_text,text_type_text))
    return node_list



if __name__ == "__main__":
    main()