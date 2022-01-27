# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:09:16 2021

@author: ClaudiaLorusso
"""

from re import sub
from spacy import load
# if you haven't done it yet: python3 -m spacy download it_core_news_sm


# ------------------------------ Rimozione di noyse ------------------------

def remove_digits(text):
    """
    Removes all of the digits from text (argument)

    Parameters
    ----------
    text : string
        string to process for the removal of the digits

    Returns
    -------
    string
        the argument without digits

    """
    return sub(r'\d+', "", text)

def replace_symb(symb, digit, text):
    """
    Replaces each occurrence of symb (first argument)
    with digit (second argument) in text (third argument).

    Parameters
    ----------
    text : string
        string on which perform the replacement
    symb : string
        string to be replaced
    digit: string
        string that replaces symb

    Returns
    -------
    string
        text deprived of all the occurrences of symb, replaced by digit
    """
    return sub(symb, digit, text)

def clean_text(text):
    """
    Each apice in the text it's substituted by the classical apice.
    :param text: text to clean
    :return: text cleaned

    """

    txt = replace_symb("’", "'", text)
    txt = replace_symb("“", '"', txt)
    txt = replace_symb("”", '"', txt)
    return txt

def remove_new_lines(text):
    """

    :param text: string to clean
    :return: String
    The argument without new lines
    """
    txt = sub(r"(?<!\\)\\n|\n", " ", text)
    txt = " ".join(txt.split())
    return text

#------------------------------ NLP SPACY ---------------------------------

def __nlp_SPACY__():
    """
    Loads the italian NLP from SPACY
    :return:
        the Italian NLP
    """

    return load("it_core_news_sm")

#------------------------------- LEMMA -------------------------------------

def preprocess_lemma(txt):
    """
    Preprocesses a string (txt, argument):
    -   removes all of the digits
    -   computes the LEMMA using SPACY
    -   lowercases the corresponding LEMMA
    -   removes all of the trailing spaces
    :param txt:
    :return:
        the argument lemma

    """

    # removes digits
    txt = remove_digits(txt)
    # gets lemma applying SPACY and lower cases the output
    lemma = (get_lemma_SPACY(txt)).lower()

    #removes unnecessary spaces
    lemma = " ".join(lemma.split())
    return lemma

#                     ----- SPACY LEMMATIZER -----

def get_lemma_SPACY(tokens):
    """
    Computes the tokens lemma
    Parameters
    ----------
    tokens : token
        a sequence of tokens from which compute the lemma

    Returns
    -------
    lemma
        tokens lemma

    """

    nlp = __nlp_SPACY__()
    doc = nlp(tokens)
    return ' '.join([token.lemma_ for token in doc])