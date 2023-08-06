"""
The module contains SentencesExtraction class which provides functionality
to extract sentences from the given articles

"""


import re
import en_core_web_lg

from collections import OrderedDict
nlp = en_core_web_lg.load()


class SentencesExtraction:

    """
    This class provides methods for recognizing single sentences
    of a given text

    """

    def __init__(self, filetext):
        self.filetext = filetext

    def get_sentences(self):
        """ Class method extracting all the sentences of article texts """
        return self.__find_sentences()

    def __find_sentences(self):
        end = True
        sentences = []
        paragraph = self.filetext
        while end > -1:
            end = self.__find_sentence_end(paragraph)
            if end > -1:
                sentences.append(paragraph[end:].strip())
                paragraph = paragraph[:end]
        sentences.append(paragraph)
        sentences.reverse()

        # Remove incomplete sentences
        sentences = self.__remove_incomplete_sent(sentences)
        # Remove extra spaces
        sentences = self.__remove_extra_spaces(sentences)
        return sentences

    def __find_all(self, a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1:
                return
            yield start
            start += len(sub)

    def __find_sentence_end(self, paragraph):
        # extracting sentences
        abbreviations = {'dr.': 'doctor', 'mr.': 'mister', 'bro.': 'brother',
                         'bro': 'brother', 'mrs.': 'mistress', 'ms.': 'miss',
                         'jr.': 'junior', 'sr.': 'senior',
                         'i.e.': 'for example', 'e.g.': 'for example',
                         'vs.': 'versus', 'Fig.': 'Figure', 'www': 'website',
                         'et al': 'ref', 'et al.': 'ref',
                         'D.magna': 'Daphnia magna',
                         'V. fischeri': 'Photobacterium phosphoreum',
                         'P.phosphoreum': 'Photobacterium phosphoreum',
                         'S. capricornutum': 'Raphidocelis subcapitata',
                         'A.salina': 'Artemia salina,',
                         'P.acuta Drap.': 'Pysella acuta Draparnaud',
                         'No.': 'Number'}
        terminators = ['.', '!', '?']
        wrappers = ['".', "'.", ').', '].', '}.']
        [possible_endings, contraction_locations] = [[], []]
        contractions = abbreviations.keys()
        sentence_terminators = terminators + [terminator + wrapper
                                              for wrapper in wrappers for
                                              terminator in terminators]
        for sentence_terminator in sentence_terminators:
            t_indices = list(self.__find_all(paragraph, sentence_terminator))
            possible_endings.extend(([] if not len(t_indices) else
                                     [[i, len(sentence_terminator)]
                                      for i in t_indices]))
        for contraction in contractions:
            c_indices = list(self.__find_all(paragraph, contraction))
            contraction_locations.extend(([] if not len(c_indices) else
                                          [i + len(contraction)
                                           for i in c_indices]))
        possible_endings = [pe for pe in possible_endings if pe[0] + pe[1]
                            not in contraction_locations]
        if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
            max_end_start = max([pe[0] for pe in possible_endings])
            possible_endings = [pe for pe in possible_endings
                                if pe[0] != max_end_start]
        possible_endings = [pe[0] + pe[1] for pe in possible_endings
                            if sum(pe) > len(paragraph) or
                            (sum(pe) < len(paragraph) and
                             paragraph[sum(pe)] == ' ')]
        end = (-1 if not len(possible_endings) else max(possible_endings))
        return end

    def __remove_extra_spaces(self, all_s):

        full_sent = []
        for sent in all_s:
            sent = re.sub(r'\s+', ' ', sent)
            sent = re.sub("\n", " ", sent)

            full_sent.append(sent)
        return full_sent

    def __remove_incomplete_sent(self, all_s):
        un = []
        comp = []
        for i in range(len(all_s)):
            if len(all_s[i]) > 45:
                if all_s[i][0].isupper() or all_s[i][1].isupper():
                    comp.append(i)
                    continue
                else:
                    un.append(i)
            else:
                continue

        alls = [all_s[0]]
        for i in range(1, len(all_s)):
            if i in comp:
                alls.append(all_s[i])
            else:
                alls[-1] = alls[-1] + all_s[i]

        full_sent = []
        for sent in alls:
            doc = nlp(sent)
            for sent_1 in doc.sents:

                has_noun = 2
                has_verb = 1
                for token in sent_1:
                    if token.pos_ in ["NOUN", "PRON"]:
                        has_noun -= 1
                    elif token.pos_ == "VERB":
                        has_verb -= 1
                if has_noun < 1 and has_verb < 1:
                    full_sent.append(sent)

        full_sent = list(OrderedDict.fromkeys(full_sent))  # removes duplicates
        return full_sent
