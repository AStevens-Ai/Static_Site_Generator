import unittest
from main import *
from text_types import *
from textnode import *

class TestSplitNodes(unittest.TestCase):
    def test_image_extraction(self):
        test_extraction = split_nodes_image([TextNode('hello from ![my image](https://hulu.com)', text_type_text)])

        expected = ([TextNode('hello from', text_type_text), TextNode("my image", text_type_image, 'https://hulu.com')])
        

        self.assertEqual(test_extraction, expected)

    def test_link_extraction(self):
        test_extraction = split_nodes_link([TextNode('hello from [the other side](https://adele.com) i love [chinese](https://chinesefood.com)', text_type_text)])

        expected = ([TextNode('hello from', text_type_text), TextNode('the other side', text_type_link, 'https://adele.com'), TextNode('i love', text_type_text), TextNode('chinese', text_type_link, 'https://chinesefood.com')])


        self.assertEqual(test_extraction, expected)
    

if __name__ == "__main__":
    unittest.main()
