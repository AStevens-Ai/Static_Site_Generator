from htmlnode import *
from inline_markdown import *

def markdown_to_blocks(markdown):
    blocks = []
    current_block = []
    
    for line in markdown.splitlines():
        line = line.strip()
        if line:
            current_block.append(line)
        else:
            if current_block:
                blocks.append("\n".join(current_block))
            current_block = []
    if current_block:
        blocks.append("\n".join(current_block))
    return blocks

def block_to_block_type(block):
    if block.startswith('#'):
        hash_count = 0
        while hash_count < 6 and block[hash_count] == '#':
            hash_count += 1
        if hash_count > 0 and block[hash_count] == ' ':
            return 'heading'
        return 'paragraph'
    
    elif block.startswith('```'):
        if block.endswith('```'):
            return 'code'
        else:
            return 'paragraph'
    
    elif block.startswith('>'):
        lines = block.splitlines()
        if not lines:
            return 'paragraph'
        
        for line in lines:
            if not line.startswith('>'):
                return 'paragraph'
        return 'quote'
    
    elif block.startswith('*') or block.startswith('-'):
        lines = block.splitlines()
        if not lines:
            return 'paragraph'
        
        for line in lines:
            if not (line.startswith('* ') or line.startswith('- ')):
                return 'paragraph'
        return 'unordered_list'
    
    elif block.startswith('1. '):
        lines = block.splitlines()
        if not lines:
            return 'paragraph'
        
        expected_number = 1
        for line in lines:
            if not line.startswith(f"{expected_number}. "):
                return 'paragraph'
            expected_number += 1
        return 'ordered_list'
    
    else:
        return 'paragraph'

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks_list:
        type = block_to_block_type(block)
        block_node = None

        if type == "heading":
            level = block.count('#')
            tag = f'h{level}'
            content = block.lstrip('# ').strip()
            block_node = LeafNode(value=content, tag=tag)

        elif type == "code":
            content = block.strip('`').strip()
            block_node = ParentNode(children=[LeafNode(value=content, tag='code')], tag='pre')

        elif type == "quote":
            content = block.strip('> ').strip()
            block_node = ParentNode(children=[LeafNode(value=content, tag='blockquote')], tag='blockquote')

        elif type == "unordered_list":
            print(f"Processing unordered list block: {block}")
            block_node = ParentNode(children=[], tag='ul')
            lines = block.strip().splitlines()
            for line in lines:
                list_item_content = line.lstrip('* - ')
                print(f"List item content: {list_item_content}")
                children = text_to_children(list_item_content)
                list_item_node = ParentNode(children=children, tag='li')
                block_node.children.append(list_item_node)

        elif type == "ordered_list":
            block_node = ParentNode(children=[], tag='ol')
            lines = block.strip().splitlines()
            for line in lines:
                list_item_content = line.lstrip('1234567890. ')
                children = text_to_children(list_item_content)
                list_item_node = ParentNode(children=children, tag='li')
                block_node.children.append(list_item_node)

        else:
            block_node = ParentNode(children=[], tag="p")
            lines = block.strip().splitlines()
            for line in lines:
                paragraph_content = line.strip()
                children = text_to_children(paragraph_content)
                block_node.children.extend(children)

        if block_node:
            html_nodes.append(block_node)

    div_node = ParentNode(children=html_nodes, tag='div')

    return div_node

