from textnode import TextNode
from htmlnode import *

print('hello world')

def main():
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"
    print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    print(HTMLNODE('p', 'test', 'test', '[("class", "ice"), ("id", "cream")]'))
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    print(new_nodes)

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




if __name__ == "__main__":
    main()