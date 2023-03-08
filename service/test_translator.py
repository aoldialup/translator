"""Unit test for functions in the translator module"""

import unittest
from translator import english_to_french, french_to_english

"""Class for testing the functions"""
class TestEnglishToFrench(unittest.TestCase):
    """Tests for english to french"""
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello world'), "Bonjour le monde")
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestFrenchToEnglish(unittest.TestCase):
    """Tests for french to english"""
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour le monde'), 'Hello World')
        self.assertNotEqual(french_to_english(
            'Bonjour le monde'), 'Bonjour le monde')

unittest.main()