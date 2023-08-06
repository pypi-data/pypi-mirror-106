"""

This module contains the TextExtraction class, which allows
to extract and clean text from pdf articles

"""

import re
import fitz
import textract
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
from io import StringIO


class TextExtraction:

    def __init__(self, filepath):
        self.filepath = filepath

    def getText(self):
        """Class method extracting texts of articles"""

        return self.__gettexts()

    def __extracttxt1(self):
        """Helper function to extract text by PyMupdf, fastest"""

        x = fitz.open(self.filepath)
        ps = ''
        pageN = x.pageCount
        for i in range(pageN):
            pages = x.loadPage(i)
            text = ''
            text = pages.getText('text')
            ps = ps + text
        return (ps)

    def __extracttxt2(self):
        """Helper function to extract text by pdfminer, slower but handles
        formats not recongnised by PyMupdf"""

        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(str(self.filepath), 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                      password=password, caching=caching,
                                      check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        return text

    def __extracttxt3(self):
        """Helper function to extract text of formats not recognized by
        PyMupdf and pdfminer"""

        text = textract.process(str(self.filepath), encoding='utf-8')
        return (str(text))

    def __ref_remove(self, text):
        """Helper function to remove the References block of articles"""

        words1 = ['Acknowledgments', 'Acknowledgement', 'ACKNOWLEDGEMENTS',
                  'ACKNOWLEDGEMENT', 'ACKNOWLEDGMENT', 'Acknowledgment']

        words2 = ['References', 'REFERENCES', 'LITERATURE CITED']
        p = []
        for w in words1:
            pp = [m.start() for m in re.finditer(w, text)]
            if pp:
                p.append(pp)
        if not p:
            for w in words2:
                pp = [m.start() for m in re.finditer(w, text)]
                if pp:
                    p.append(pp)

        try:
            t = max(p)[0]
            head, s, tail = text.partition(text[t:t+16])
            return (head)
        except ValueError:
            return (text)

    def __head_remove(self, text, k):
        """Helper function to remove the heading of articles
        (all until the Introduction part)"""

        words = ['Introduction', 'INTRODUCTION', 'Background', 'BACKGROUND']
        p = []
        for w in words:
            pp = [m.start() for m in re.finditer(w, text)]
            if pp:
                p.append(pp)
        try:
            if k == 0:
                t = min(p)[0]
            if k == 1:
                if len(p[0]) > 1:
                    del min(p)[0]
                t = min(p)[0]
            head, s, tail = text.partition(text[t:t+14])
            return (s[-1]+tail)
        except ValueError:
            return (text)

    def __cleanText(self, text, k):
        """  function to remove the heading and references
             block of articles """

        txt = self.__head_remove(text, k)
        txt = self.__ref_remove(txt)
        txt = re.sub(r'\S*@\S*\s?', '', txt)  # remove emails
        txt = re.sub(r'\s\s*', ' ', txt)  # remove extra spaces
        txt = re.sub(r'[a-]\s', '', txt)

        return txt

    def __gettexts(self):
        """Helper function applying text extraction functions"""
        x = fitz.open(self.filepath)
        page0 = x.loadPage(0)
        txt = ''
        txt = page0.getText('text')
        words = ['Contents', 'CONTENTS']
        p = []
        if (". . . . . ." in txt) or any(word for word in
           words if (word in txt)):
            k = 1
            for w in words:
                p.append([m.start() for m in re.finditer(w, txt)])
            if txt[p[0][0]+9].isalpha() or txt[p[0][0]+10].isalpha():
                k = 0
        else:
            k = 0

        if '���' in txt[0:10]:

            try:
                text = self.__extracttxt2()

            except TypeError:
                text = self.__extracttxt3()

        else:
            text = self.__extracttxt1()

        text = self.__cleanText(text, k)

        return text
