"""
The module provides functionality to extract keywords of the sentences.
Applies a pke module:
https://boudinfl.github.io/pke/build/html/index.html

"""
import re
import pke


def ExtractKeywords(sentences):

    keywords = []
    keywords_strings = []

    separator = ', '

    for i in range(len(sentences)):

        a = []
        b = []

        # define the set of valid Part-of-Speeches
        pos = {'NOUN', 'ADJ', 'VERB'}

        # 1. create a SingleRank extractor.
        extractor = pke.unsupervised.SingleRank()

        # remove citations from the sentence
        input_s = re.sub(r"[\(\[].*?[\)\]]", "", sentences[i])

        # 2. load the content of the sentence
        extractor.load_document(input=input_s,
                                language='en',
                                normalization=None)

        # 3. select the longest sequences of nouns, adjectives
        # and verbs as candidates.
        extractor.candidate_selection(pos=pos)

        try:

            # 4. weight the candidates using the sum of their word's scores
            #    that are computed using random walk. In the graph, nodes are
            #    words of certain part-of-speech (nouns and adjectives) that
            #    are connected if they occur in a window of 10 words.
            extractor.candidate_weighting(window=10, pos=pos)

            # 5. get the 10-highest scored candidates as keyphrases.
            keyphrases = extractor.get_n_best(n=10)

            for k, n in keyphrases:
                a.append(k)
            b = b + [separator.join(a)]

            keywords.append(a)
            keywords_strings.append(b)

        except ValueError:
            keywords.append(["NO"])
            keywords_strings.append(["NO"])

    return keywords_strings
