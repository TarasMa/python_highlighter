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
        self.search_text = b"the"
        self.text = b"The sun in the sky"
        self.highlighted_text = b'<mark>The</mark> sun in <mark>the</mark> sky'
        self.highlighted_text_is_sensitive = b'The sun in <mark>the</mark> sky'
        self.is_sensitive = '0'
        self.is_not_sensitive = '1'

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
        """Test markup process"""
        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text,
                                            'is_sensitive': self.is_sensitive})
        self.assertIn(self.highlighted_text, response.data)

    def test_case_insensitive(self):
        """Test markup process"""
        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text,
                                            'is_sensitive': self.is_not_sensitive})
        self.assertIn(self.highlighted_text_is_sensitive, response.data)
