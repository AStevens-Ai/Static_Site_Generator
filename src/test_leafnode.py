import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_correct_exp(self):
        node = LeafNode("Hello World", "p", props=[("class", "my-class"), ("id", "my-id")])

        result = node.to_html()

        expected = '<p class="my-class" id="my-id">Hello World</p>'
        self.assertEqual(result, expected)

    def test_incorrect_exp(self):
        node = LeafNode("test", props=[])

        result = node.to_html()

        expected = 'test'
        self.assertEqual(result, expected)
    
    def test_incorrect_exp_type(self):
        node = LeafNode("quick brown")

        result = node.to_html()

        expected = 'quick brown'
        self.assertEqual(result, expected)
    def test_link(self):
        node = LeafNode("link press me", 'a', props= [("href", "https://www.google.com")])

        result = node.to_html()

        expected = '<a href="https://www.google.com">link press me</a>'
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()