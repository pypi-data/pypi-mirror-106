# -*- coding: utf-8 -*-
"""
Test for the knowmine main module

"""
import os
from knowmine import extract_relevant_sentences


def main():

    folder_path = os.getcwd() + "/ "
    main_terms = ["toxicit"]
    relation_words = ["increas", "predict"]
    extract_relevant_sentences(folder_path, main_terms,
                               relation_words, "db", 3)


if __name__ == '__main__':
    main()
