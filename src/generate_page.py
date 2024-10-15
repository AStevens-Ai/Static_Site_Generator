from blocks import *
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as file:
        from_content = file.read()

    with open(template_path, 'r') as file:
        template_content = file.read()

    title = extract_title(from_content)
    if title is None:
        print("Warning: No title found in the markdown content.")

    markdown_html_node = markdown_to_html_node(from_content)
    html_nodes = markdown_html_node.to_html()
    title_replaced = template_content.replace('{{ Title }}', title)
    content_replaced = title_replaced.replace('{{ Content }}', html_nodes)

    with open(dest_path, 'w') as f:
        f.write(content_replaced)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    with  open(template_path, 'r') as file:
        template = file.read()
    for entry in entries:
        full_path = os.path.join(dir_path_content, entry)
        html_filename = os.path.splitext(entry)[0] + '.html'
        dest_path = os.path.join(dest_dir_path, html_filename)
        
        if os.path.isdir(full_path):
            new_dest_path = os.path.join(dest_dir_path, entry )
            os.makedirs(new_dest_path, exist_ok=True)
            generate_pages_recursive(full_path, template_path, new_dest_path)
        elif entry.endswith('.md'):
            with open(full_path, 'r') as file:
                content = file.read()
            title = extract_title(content)
            markdown_html_node = markdown_to_html_node(content)
            html_nodes = markdown_html_node.to_html()
            title_replaced = template.replace('{{ Title }}', title)
            content_replaced = title_replaced.replace('{{ Content }}', html_nodes)
            with open(dest_path, 'w') as file:
                file.write(content_replaced)

