from textnode import TextNode
from htmlnode import *
from inline_markdown import *
from text_types import *

print('hello world')

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()