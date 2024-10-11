import unittest
from textnode import TextNode
from main import split_nodes_delimiter

class Test_split_code_delim(unittest.TestCase):
    text_type_text = "text"
    text_type_code = "code"
    text_type_italic = "italic"
    text_type_bold = "bold"

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", self.text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", self.text_type_code)

        expected_nodes = [
            TextNode("This is text with a ", self.text_type_text),
            TextNode("code block", self.text_type_code),
            TextNode(" word", self.text_type_text)
        ]

        for expected, actual in zip(expected_nodes, new_nodes):
            self.assertEqual(expected.text, actual.text)
            self.assertEqual(expected.text_type, actual.text_type)
    
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is a text with a *italic block* word", self.text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", self.text_type_italic)

        expected_nodes = [
            TextNode("This is a text with a ", self.text_type_text),
            TextNode("italic block", self.text_type_italic),
            TextNode(" word", self.text_type_text)
        ]

        for expected, actual in zip(expected_nodes, new_nodes):
            self.assertEqual(expected.text, actual.text)
            self.assertEqual(expected.text_type, actual.text_type)


    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is a text with a **bold block** word", self.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", self.text_type_bold)

        expected_nodes = [
            TextNode("This is a text with a ", self.text_type_text),
            TextNode("bold block", self.text_type_bold),
            TextNode(" word", self.text_type_text)
        ]

        for expected, actual in zip(expected_nodes, new_nodes):
            self.assertEqual(expected.text, actual.text)
            self.assertEqual(expected.text_type, actual.text_type)        
if __name__ == "__main__":
    unittest.main()