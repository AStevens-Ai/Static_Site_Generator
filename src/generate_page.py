from blocks import *
from extract_title import extract_title

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


