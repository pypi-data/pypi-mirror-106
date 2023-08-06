# -*- coding: utf-8 -*-
"""
Unit tests for the knowmine.AllSentencesExtractor module.
"""

from knowmine.TextExtractor import TextExtraction


def test_getText():

    article = TextExtraction(r"test_article1.pdf")

    assert article.getText() is not None
    assert article.getText() != ''
