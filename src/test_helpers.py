import unittest
from helpers import extract_title

class TestHelpers(unittest.TestCase):
    def test_returning_header(self):
        result = extract_title("# helo world")
        self.assertEqual(result, "helo world")
    def test_returning_strip_header(self):
        result = extract_title("# Helo worlds    ")
        self.assertEqual(result, "Helo worlds")
