from text_types import *
from textnode import *
import re


def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
        else:
            print(node.text)
            image_tuples = extract_markdown_images(node.text)
            remaining_text = node.text
            if not image_tuples:
                node_list.append(node)
                remaining_text = ""
            else:
                for key, value in image_tuples:
                    split_list = remaining_text.split(f"![{key}]({value})", 1)
    
                if len(split_list) < 2:
        
                    node_list.append(TextNode(remaining_text, text_type_text))
                    break

                first_string, second_string = split_list

                if first_string:
                    node_list.append(TextNode(first_string, text_type_text))
    
                node_list.append(TextNode(key, text_type_image, value))

                remaining_text = second_string
            if remaining_text:
                node_list.append(TextNode(remaining_text,text_type_text))
    return node_list


def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
        else:
            print(node.text)
            link_tuples = extract_markdown_links(node.text)
            remaining_text = node.text
            if not link_tuples:
                node_list.append(node)
                remaining_text = ""
            else:
                for key,value in link_tuples:
                    split_list = remaining_text.split(f"[{key}]({value})", 1)
                    first_string = split_list[0]
                    if len(split_list) > 1:
                        second_string = split_list[1]
                    
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


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches