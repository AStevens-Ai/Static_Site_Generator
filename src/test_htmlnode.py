import unittest
from htmlnode import HTMLNODE

class TestHTMLNode(unittest.TestCase):
    def test_correct_exp(self):
        node = HTMLNODE(props=[("class", "my-class"), ("id", "my-id")])

        result = node.props_to_html()

        expected = ' class="my-class" id="my-id"'
        self.assertEqual(result, expected)

    def test_incorrect_exp(self):
        node = HTMLNODE(props=[])

        result = node.props_to_html()

        expected = ''
        self.assertEqual(result, expected)
    
    def test_incorrect_exp_type(self):
        node = HTMLNODE(props=[("class", "my-class")])

        result = node.props_to_html()

        expected = ' class="my-class"'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()