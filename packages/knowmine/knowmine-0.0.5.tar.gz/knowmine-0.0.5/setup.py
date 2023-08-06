# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:11:01 2020

@author: Gulnara Shavalieva
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knowmine",
    version="0.0.5",
    author="Gulnara Shavalieva",
    author_email="gulsha@chalmers.se",
    description="Knowledge mining package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GulnaraSh/knowledge-mining-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=[
        "gitpython",
        "nltk",
        "PyMuPDF",
        "textract",
        "pdfminer3",
        "openpyxl"        
    ]
)
