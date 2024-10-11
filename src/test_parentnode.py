import unittest
from htmlnode import ParentNode
from htmlnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_correct_exp(self):
        node = ParentNode(
           [
                LeafNode( "Bold text", "b",),
                LeafNode( "Normal text",None,),
                LeafNode("italic text","i", ),
                LeafNode( "Normal text",None,),
            ],
              "p"
            
        )

        result = node.to_html()

        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(result, expected)

    def test_no_children(self):
        node = ParentNode(
           [],
              "p"
        )

        result = node.to_html()

        expected = '<p></p>'
        self.assertEqual(result, expected)

    def test_no_tag(self):
        node = ParentNode(
            [
                LeafNode( "Bold text", "b",),
                LeafNode( "Normal text",None,),
                LeafNode("italic text","i", ),
                LeafNode( "Normal text",None,),
            ],
            "html"
        )
        result = node.to_html()

        expected = '<html><b>Bold text</b>Normal text<i>italic text</i>Normal text</html>'
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()