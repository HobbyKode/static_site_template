import unittest

from src.page_generator import extract_title

import sys
sys.dont_write_bytecode = True  # Prevent __pycache__ creation

class TestPageGenerator(unittest.TestCase):
    def test_extract_title(self):
        md = """ 
# This is America
# This is Sparta
# This is Wrong
        """
        title = extract_title(md)  # Extracts only the first heading
        
        self.assertEqual(title, "This is America")  # Expected output


    def test_extract_title_single(self):
        md = """ 
# Ultimate Exorcist Kiyoshi
        """
        title = extract_title(md)  # Extracts only the first heading
        
        self.assertEqual(title, "Ultimate Exorcist Kiyoshi")  # Expected output

if __name__ == "__main__":
    unittest.main()
