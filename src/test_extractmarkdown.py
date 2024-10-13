import unittest
from extract_markdown_images import *
from extract_markdown_links import *

class TestExtractMarkdown(unittest.TestCase):
    def test_image_extraction(self):
        test_extraction = extract_markdown_images('hello from ![my image](https://hulu.com)')

        expected = [('my image', 'https://hulu.com')]

        self.assertEqual(test_extraction, expected)

    def test_link_extraction(self):
        test_extraction = extract_markdown_links('hello from [my website](https://mywebsite.com), and [my site 2](https://mywebsite2.com)')

        expected = [('my website', 'https://mywebsite.com'), ("my site 2", "https://mywebsite2.com")]

        self.assertEqual(test_extraction, expected)
if __name__ == "__main__":
    unittest.main()
