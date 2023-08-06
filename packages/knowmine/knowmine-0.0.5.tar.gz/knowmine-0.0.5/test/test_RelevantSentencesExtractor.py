# -*- coding: utf-8 -*-
"""
Unit tests for the knowmine.AllSentencesExtractor module.

"""

from knowmine.RelevantSentencesExtractor import RelevantSentences


words = ["similar", "predict"]

keys = ["toxicit"]


def test_get_relevant_sentences():

    text = RelevantSentences(r"test_article1.pdf", keys, words)

    assert len(text.get_relevant_sentences()) > 0
