from main import *
from textnode import TextNode

def test_text_node_to_html_node():
    text_node = TextNode("Hello, world!", "text")
    html_node = text_node_to_html_node(text_node)
    if not (html_node.tag is None and html_node.value == "Hello, world!" and html_node.props is None):
        print("Text node test failed")
        return False
    
    bold_node = TextNode("Bold text", "bold")
    html_node = text_node_to_html_node(bold_node)
    if not (html_node.tag == "b" and html_node.value == "Bold text" and html_node.props is None):
        print("Bold node test failed")
        return False
    

    print("All tests passed!")
    return True

test_result = test_text_node_to_html_node()
print(f"Test result: {'Passed' if test_result else 'Failed'}")

