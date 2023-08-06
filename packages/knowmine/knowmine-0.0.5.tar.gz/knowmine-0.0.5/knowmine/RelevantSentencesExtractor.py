"""
This module contains a RelevantSentences class, which, from all
the articles sentences, extracts only the ones containing the
provided main terms and relation words if they are keywords of the sentence

"""

from knowmine.KeywordsExtractor import ExtractKeywords
from knowmine import TextExtractor as txtext
from knowmine import AllSentencesExtractor as allsent
import json


class RelevantSentences:

    def __init__(self, file_name, main_terms, relation_words):
        self.file_name = file_name
        self.main_terms = main_terms
        self.relation_words = relation_words

    def get_relevant_sentences(self):
        """Class method extracting relevant sentences of all the sentences
        of the texts"""
        return self.__output()

    def __sentences_with_terms(self):
        sents = []
        text_obj = txtext.TextExtraction(self.file_name)
        text = text_obj.getText()
        allsents_obj = allsent.SentencesExtraction(text)
        allsentences = allsents_obj.get_sentences()
        n_all_sents = len(allsentences)
        for sent in allsentences:
            if any(word for word in self.main_terms if(word in sent)):
                sents.append(sent)

        return (sents, n_all_sents)

    def __ExtractUsefulSentences(self):

        sents_with_keys, n_all = self.__sentences_with_terms()
        keywords_strings = ExtractKeywords(sents_with_keys)
        sent_to_read = []

        for j in keywords_strings:
            if any(word for word in self.main_terms if(word in j[0])) and  \
               any(word for word in self.relation_words if(word in j[0])):
                sent_to_read.append(sents_with_keys[keywords_strings.index(j)])
        nn = len(sent_to_read)

        return (sent_to_read, n_all, nn)

    def __output(self):
        use_sents, n_all, nn = self.__ExtractUsefulSentences()

        processResult = (str(self.file_name),
                         json.dumps(use_sents,
                                    ensure_ascii=False).encode('utf8'),
                         nn, n_all)
        return processResult
