# -*- coding: utf-8 -*-
"""
Unit tests for the knowmine.KeywordsExtractor module.
"""

from knowmine.KeywordsExtractor import ExtractKeywords


def test_ExtractKeywords():

    sentences = ['The European Union established the regulation'
                 + 'registration, evaluation, authorization and restriction of'
                 + 'chemicals (REACH) to protect human health and the'
                 + 'environment from hazards of industrial chemicals.',
                 'Industry has to register all substances produced in or'
                 + 'imported into the EU at rate �1 t/y.',
                 'Physicochemical, (eco) toxicological and exposure-relevant'
                 + 'information have to be supplied for registration depending'
                 + 'on the production rate.',
                 'For environmental assessment of chemicals to be registered'
                 + ' by 2018 (1e100 t/y) at least the following information'
                 + 'has to be presented: - Acute toxicity to algae, daphniand'
                 + 'fish (the latter only for substances >10 t/y)'
                 + 'Octanol/water partition coefficient (log KOW)'
                 + 'Water solubility (SW) - Biodegradability '
                 + 'This information is used to decide whether substance'
                 + 'has to be classified as hazardous to the aquatic'
                 + 'environment and labelled according to the CLP regulation'
                 + '(European Commission, 2009).',
                 'For substances >10 t/y chemical safety assessment (CSA)'
                 + 'has to be performed, including the derivation of the'
                 + 'predicted environmental concentration (PEC) as well as'
                 + 'the predicted no effect concentration (PNEC) and'
                 + 'the assessment of (very) persistent,'
                 + '(very) bioaccumulative and toxic (PBT/vPvB) properties.']

    keywords = ExtractKeywords(sentences)

    assert len(keywords) == 5
    assert len(keywords[0]) != 0
