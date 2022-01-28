# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:09:16 2021

@author: ClaudiaLorusso
"""

from re import sub
# PER ESTRAZIONE KEYPHRASE, tokenizzare e creazione vocabulary:
# PER TOKENIZZAZIONE NLTK
# per rimozione STOPWORDS NLTK
from nltk import word_tokenize
from nltk.corpus import stopwords

# if you haven't done it yet: python3 -m spacy download it_core_news_sm
import sys
from os import path


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
    Removes new lines from the string passed in input (argument)
    :param text: string to clean
    :return: String
    The argument without new lines
    """
    txt = sub(r"(?<!\\)\\n|\n", " ", text)
    txt = " ".join(txt.split())
    return text


# ------------------------------ NLP SPACY ---------------------------------

def __nlp_SPACY__():
    """
    Loads the italian NLP from SPACY
    :return:
        the Italian NLP
    """
    # for computing lemma
    from spacy import load
    return load("it_core_news_sm")


# ------------------------------- LEMMA -------------------------------------

def preprocess_lemma(txt):
    """
    Preprocesses a string (txt = argument):
    -   removes all of the digits
    -   computes the LEMMA using SPACY
    -   lowercases the corresponding LEMMA
    -   removes all of the trailing spaces
    :param txt: string
        the text on which perform the lemma
    :return: string
        the argument lemma

    """

    # removes digits
    txt = remove_digits(txt)
    # gets lemma applying SPACY and lower cases the output
    lemma = (get_lemma_SPACY(txt)).lower()

    # removes unnecessary spaces
    lemma = " ".join(lemma.split())
    return lemma

def get_lemma_targets_laws_df(path_law=""):
    """
    Computes a DataFrame which contains both targets lemma and law's lemma.
    :param path_law: string
        law's path
    :return: DataFrame
        containing the concatenation between law's df and targets df
    """
    from SDG_Preprocessing import get_lemma_dataframe
    from LawPreprocessing import get_df_laws_lemma
    import pandas as pd

    df_laws = get_df_laws_lemma(path_law)
    df_targets = get_lemma_dataframe()

    union = pd.concat([df_targets, df_laws])
    return union

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


# -------------------------------- VOCABULARY ----------------------------

def compute_vocabulary(lemma_path, n_gram=2):
    """
    Computes a vocabulary (list of strings) having in input a lemma (first argument).
    Each keyphrase contained into the vocabulary can be composed of 1, 2 or more tokens.
    By default the computation is setted to bigram (1 or 2 token for each keyphrase) but it's possible
    to change the parameter by passing another value to the n_gram argument, for e.g.:
        n_gram = 2 (bigram, DEFAULT case), possible keyphrases are:
            "cibo scarso",
            "emancipazione femminile",
            "bambini",
            etc.
        n_gram = 1 (unigram), possible keyphrases are:
            "cibo",
            "scarso",
            "emancipazione",
            "femminile",
            "bambini",
            etc.
    :param lemma_path: string
        destination + name of the xlsx file containing the lemma.
    :param n_gram: integer
        it represents the number of words for each keyphrase.
    :return:
        list of strings
            the needed vocabulary. It will be in the form of (in the case of bigram):
            _____|keyphrase
            0     cibo scarso
            1     emancipazione femminile
            2     bambini
        DataFrame
            dataframe containing the vocabulary
    """
    from nltk.util import ngrams
    import pandas as pd
    # convert the xsl into a Dataframe
    df = pd.read_excel(lemma_path)
    vocab = list()
    list_of_descriptions = df["body"].tolist()

    for content in list_of_descriptions:
        txt = remove_new_lines(content)
        token = word_tokenize_NLTK(txt)
        # remove stopwords from token
        tokens_no_sw = [word for word in token if not word in stop_words_ita()]
        tokens_no_sw = list(ngrams(tokens_no_sw, n_gram))
        print(tokens_no_sw)
        for tokens in tokens_no_sw:
            tok = ""
            for key in tokens:
                tok += (key + " ")
            tok = " ".join(tok.split())
            vocab.append(tok)
    vocab = set(vocab)  # in this way I remove duplicates
    vocab = list(vocab)  # now it's a list again (with no duplicates)
    df_vocab = pd.DataFrame(columns=['keyphrase'])
    # I create an xlsx file
    i = 0
    for keyphrase in vocab:
        df_vocab.loc[i] = [keyphrase]
        i += 1

    path_dir = __get_path__("VOCAB\\vocabulary.xlsx")
    df_vocab.to_excel(path_dir)
    return vocab, df_vocab

def get_list_vocabulary(dest):
    """
    Returns a list containing each keyphrase of the vocabulary
    :param dest: string
        destination of the vocabulary xlsx
    :return:
        list of strings
            ... containing each keyphrase of the vocabulary

    """
    from pandas import read_excel
    dest = __get_path__(dest)
    df = read_excel(dest)
    vocabulary = df['keyphrase'].tolist()
    return vocabulary

# -------------------------------- TOKENIZER -----------------------------
def word_tokenize_NLTK(text):
    """
    Tokenizes a text (by the italian rules) by the use of NLTK.
    Parameters
    ----------
    text : string
        text to tokenize

    Returns
    -------
    the tokenized text

    """
    return word_tokenize(text, "italian")

# ------------------------------- STOP-WORDS -----------------------------

def stop_words_ita():
    """
    Creates a new set of customized italian stopwords in addition to the ones provided by NLTK.
    :return: set of strings
        set of italian stopwords

    """
    addictional_stop = {"malgrado", "nonostante", "squas", "invece", "#NOME?", "de", "ecc", "ecc.", "etc", "etc.",
                        "cioè",
                        "//ce", "=", "fare", "dare", "sì", "c'è", "c'", "è", "e'", "ovvero", "più", "piu", "gia", "già",
                        "e/o",
                        "ii", "iii", '/', '/b', "t", "questo", "questa", "questi", "essi", "essa", "esso", "tali",
                        "taluni",
                        "nonche", "nonchè", "io", "tu", "egli", "noi", "voi", "essi", "ho", "hai", "hanno", "ha",
                        "gia'",
                        "già", "avere", "essere", "°", "'", "il", "lo", "la", "i", "gli", "le", "un", "uno", "una",
                        "del", "dello",
                        "qualche", "all'", "al", "ovunque", "ogni", "qualunque", "alcun", "alcuna", "qualcuna",
                        "nonché",
                        "della", "dei", "degli", "alcuni", "delle", "alcune", "l'", "un'", "dell'", "dall'",
                        "altro", "altra", "altre", "altri", "altrui", "ciò", "stesso", "medesimo", "tale", "costui",
                        "costei", "costoro", "colui", "colei", "coloro", "sul", "sullo", "sulla", "sui", "sugli",
                        "sulle",
                        "sull'", "così", "di", "a", "da", "in", "con", "su", "per", "tra", "fra", "lì", "là", "qui",
                        "qua",
                        "ci", "vi", "d'", "comunque", "perchè", "–", "f.", "ilo", "of", "the", ">", "x-x", "i-i", "y",
                        "&", "t.",
                        "ix", "$", "r", "<", "%", "art.", "art", "articolo", "nell'", "quali", "quale",
                        "qual", "qualcuno", "qualcuna", "alcun", "alcuno", "alcuna", "situ", "fino", "solo", "oppure",
                        "n°", "mm",
                        "//eu", "NOME", "#", "?", "d", ".", ")", "(", ",", ":", "n.", "[", "]", ";", ".", "d.", "b",
                        "-", "..", "`", "piã¹",
                        "a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                        "v", "z", "w", "y", "k", "j", "//", "+", "``", "à", "--"}
    return addictional_stop.union(stopwords.words('italian'))


# ---------------------------- UTILS -------------------------------------
def __get_path__(relative_path):
    """
    Converts the relative path into an absolute path
    :param relative_path: relative path of the file
    :return:
        absolute path: base path + relative path
    """
    try:
        # NOTE:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        # It's a runtime computation. don't worry about the inline warning.
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)


# test
# remove triple prime to test the class
"""
if __name__ == '__main__':
    print(get_lemma_targets_laws_df("laws\\[2015-2020]LeggiRegionePuglia\\LR_20.2018.pdf"))
"""
