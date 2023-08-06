# -*- coding: utf-8 -*-
"""
Function accessing the files in a user provided folder and
returning the list of file names

"""


from knowmine.FilesReader import get_file_names
import os


def test_get_file_names():
    pdffilenames = get_file_names(os.getcwd())
    assert len(pdffilenames) > 0
