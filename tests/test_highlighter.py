"""Test module
file: test_highlighter.py
date: 12.12.2012
author smith@example.com
license: MIT"""

import unittest
from highlighter import create_app


class HighlightTest(unittest.TestCase):
    """Test class for flask app."""

    def setUp(self):
        """This method is called each time the test routine run"""
        self.app = create_app().test_client()
        self.search_text = b"Text"
        self.text = b"Sample text to be highlighted"
        self.highlighted_text = b'Sample <mark>text</mark> to be highlighted'
        self.is_sensitive = '1'
        self.is_not_sensitive = '0'

    def tearDown(self):
        """This method is called after the test routine is finished
        to clear out the data created in setUp method."""
        del self.search_text
        del self.text
        del self.highlighted_text
        del self.is_sensitive

    def test_markup_text(self):
        """Test markup process"""
        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text,
                                            'is_sensitive': self.is_sensitive})
        self.assertIn(self.highlighted_text, response.data)

    def test_case_sensitive(self):

        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text,
                                            'is_sensitive': self.is_sensitive})
        self.assertIn(self.highlighted_text, response.data)

    def test_case_insensitive(self):
        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text,
                                            'is_sensitive': self.is_not_sensitive})
        self.assertIn(self.text, response.data)
