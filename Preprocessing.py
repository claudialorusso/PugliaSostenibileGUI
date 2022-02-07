# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:09:16 2021
Provides the methods to perform different kinds of text preprocessing:
    - Remove noise:
        - remove_digits:    remove digits;
        - replace_syb:  replace a substring with another substring;
        - clean_text:   cleans text from special characters;
        - remove_new_lines: removes unnecessary new lines;
    - NLP spacy:
        - nlp_SPACY:    loads the italian NLP from SPACY
    - LEMMA:
        - preprocess_lemma:   computes the lemma of a text;
        - get_lemma_SPACY:    provides the SPACY lemma.
    - VOCABULARY:
        - compute_vocabulary: computes the vocabulary.
    - TOKENIZER:
        - word_tokenize_NLTK: provides the NLTK tokenizer.
    - STOPWORDS:
        - stop_words_ita: computes a customized set of italian stopwords.
    - TFIDF:
        - tfidf:    computes the tfidf matrix

@author: ClaudiaLorusso
"""

from re import sub
# PER ESTRAZIONE KEYPHRASE, tokenizzare e creazione vocabulary:
# PER TOKENIZZAZIONE NLTK
# per rimozione STOPWORDS NLTK
from nltk import word_tokenize
from nltk.corpus import stopwords
# if you haven't done it yet: python3 -m spacy download it_core_news_sm (not needed if you use the requirement.txt file)
import sys
from os import path, stat, makedirs


# ------------------------------ Remove noise ------------------------

def remove_digits(text):
    """
    Removes all of the digits from text (argument)

    ----------
    :parameter: text : string
        string to process for the removal of the digits

    Returns
    -------
    :return: string
        the argument without digits

    """
    return sub(r'\d+', "", text)


def replace_symb(symb, digit, text):
    """
    Replaces each occurrence of symb (first argument)
    with digit (second argument) in text (third argument).

    ----------
    :parameter: text : string
        string on which perform the replacement
    :parameter: symb : string
        string to be replaced
    parameter: digit: string
        string that replaces symb
    :return: string
        text deprived of all the occurrences of symb, replaced by digit
    """
    return sub(symb, digit, text)


def clean_text(text):
    """
    Each apice in the text it's substituted by the classical apice.
    :param text: string: text to clean
    :return: string: text cleaned

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
    :return: (Language)
        the loaded Italian NLP object
    """
    # for computing lemma
    from spacy import load

    #use this return for CLI use
    return load("it_core_news_sm")   #
    # use this return (with your virtual env path) for exe extraction purposes
    # !!remember to create the hook file for pyinstaller!!
    #return load(__get_path__(r"C:\\PUGLIA_SOSTENIBILE_GUI\\venvPS_GUI\\Lib\\site-packages\\it_core_news_sm\\it_core_news_sm-3.2.0"))#


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


def get_lemma_targets_laws_df(path_law="", sim_target = False):
    """
    Computes a DataFrame which contains both SDGs lemma and law's lemma.
    :param path_law: string
        law's path
    :param sim_target: boolean
        True if the user wants to compute the similarity between the law and each target (only)
        False (DEFAULT) if he wants to compute the similarity between the law and each SDGs (SDG = Goal + list of Target)
    :return: DataFrame
        containing the concatenation between law's and SDGs lemma's df
    """
    from SDG_Preprocessing import get_lemma_targets
    from LawPreprocessing import get_df_laws_lemma
    from pandas import concat

    path_law = __get_path__(path_law)

    path_targets = __get_path__("LEMMAS\\lemma_targets.xlsx" if sim_target else "LEMMAS\\lemma_sdgs.xlsx")

    df_laws = get_df_laws_lemma(path_law)
    df_targets = get_lemma_targets(path_targets)

    union = concat([df_targets, df_laws])
    return union

#                     ----- SPACY LEMMATIZER -----

def get_lemma_SPACY(tokens):
    """
    Computes the tokens lemma
    Parameters
    ----------
    :parameter: tokens : token
        a sequence of tokens from which compute the lemma

    Returns
    -------
    :return: string
        tokens lemma

    """

    nlp = __nlp_SPACY__()
    doc = nlp(tokens)
    return ' '.join([token.lemma_ for token in doc])


# -------------------------------- VOCABULARY ----------------------------

def compute_vocabulary(lemma_path="LEMMAS\\lemma_sdgs.xlsx", n_gram=1, path_out="VOCAB\\ngram\\vocabulary_1.xlsx"):
    """
    Computes a vocabulary (list of strings) having in input a lemma (first argument).
    Each keyphrase contained into the vocabulary can be composed by 1, 2 or more tokens.
    By default the computation is setted to unigram (1 token for each keyphrase)
    but you can also change the parameter, e.g. to bigram (1 or 2 token for each keyphrase)
    by passing another value to the n_gram argument, for e.g.:
        -   n_gram = 2 (bigram), possible keyphrases are:
                -   "cibo scarso",
                -   "emancipazione femminile",
                -   "bambini",
                -   etc.
        -   n_gram = 1 (unigram, DEFAULT case), possible keyphrases are:
                -   "cibo",
                -   "scarso",
                -   "emancipazione",
                -   "femminile",
                -   "bambini",
            etc.
    :param lemma_path: string
        destination + name of the xlsx file containing the lemma.
    :param n_gram: integer
        it represents the number of words for each keyphrase.
    :param path_out: string
        output path of the xlsx file.
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
    lemma_path = __get_path__(lemma_path)
    df = pd.read_excel(lemma_path)
    vocab = list()
    list_of_descriptions = df["body"].tolist()

    for content in list_of_descriptions:
        txt = remove_new_lines(content)
        token = word_tokenize_NLTK(txt)
        # remove stopwords from token
        tokens_no_sw = [word for word in token if not word in stop_words_ita()]
        tokens_no_sw = list(ngrams(tokens_no_sw, n_gram))
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
    path_dir = __get_path__(path_out)
    makedirs(path.dirname(path_dir), exist_ok=True)
    df_vocab.to_excel(path_dir)
    return vocab, df_vocab


def get_list_vocabulary(dest, ngram=1):
    """
    Returns a list containing each keyphrase of the vocabulary
    :param dest: string
        destination of the vocabulary xlsx
    :param ngram: integer
        grammature of the vocabulary
    :return:
        list of strings
            ... containing each keyphrase of the vocabulary

    """
    from pandas import read_excel
    dest = __get_path__(dest)
    if not path.isfile(dest):
        if ngram == 2:
            dest = __get_path__("VOCAB\\vocabulary.xlsx")
        elif ngram == 1:
            dest = get_list_vocabulary(__get_path__("VOCAB\\ngram\\vocabulary_1.xlsx"))
        else:
            dest = "VOCAB\\ngram\\vocabulary_" + str(ngram) + ".xlsx"
            dest = __get_path__(dest)
        compute_vocabulary(path_out=dest, n_gram=ngram)
    df = read_excel(dest)
    vocabulary = df['keyphrase'].tolist()
    return vocabulary


# -------------------------------- TOKENIZER -----------------------------
def word_tokenize_NLTK(text):
    """
    Tokenizes a text (following the italian grammar rules) by means of NLTK.
    Parameters
    ----------
    :param: text : string
        text to tokenize

    :return:
    -------
    string, the tokenized text

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


# ---------------------------- TFIDF -------------------------------------

def tfidf(ngram=1, path_law="", sim_target = False):
    """
    Creates the TFIDF term document matrix between the law (specified in path_law)
    and all of the SDGs.
    :param ngram: integer
        specifies how many tokens a keyphrase will contain
    :param path_law: string
        destination + name of the file containing the law
    :param sim_target: boolean
        True if the user wants to compute the similarity between the law and each target (only)
        False if he wants to compute the similarity between the law and each SDGs (SDG = Goal + list of Target)
    :return: DataFrame
        the doc term matrix

    """
    from pandas import DataFrame
    from sklearn.feature_extraction.text import TfidfVectorizer
    # -------------------------------------VOCABULARY
    if ngram == 2:
        vocabulary = get_list_vocabulary(dest=__get_path__("VOCAB\\vocabulary.xlsx"), ngram=ngram)
    elif ngram == 1:
        vocabulary = get_list_vocabulary(dest=__get_path__("VOCAB\\ngram\\vocabulary_1.xlsx"), ngram=ngram)
    else:
        file_voc = "VOCAB\\ngram\\vocabulary_" + str(ngram) + ".xlsx"
        file_voc = __get_path__(file_voc)
        # if file doesn't exist
        if not path.isfile(file_voc) or stat(file_voc).st_size == 0:
            compute_vocabulary(n_gram=ngram, path_out=file_voc)
            vocabulary = get_list_vocabulary(dest=file_voc, ngram=ngram)
        else:
            vocabulary = get_list_vocabulary(dest=file_voc, ngram=ngram)

    # -------------------------------------SET TOKENIZER
    tokenizer = word_tokenize_NLTK

    # -------------------------------------LEMMA LAWS and SDGS
    path_law = __get_path__(path_law)
    lemma_targets_laws_df = get_lemma_targets_laws_df(path_law=path_law, sim_target=sim_target)
    index = lemma_targets_laws_df['name'].tolist()

    # ------------------------------------COMPUTE TFIDF
    vect = TfidfVectorizer(vocabulary=vocabulary, encoding="utf-8", stop_words=stop_words_ita(),
                           tokenizer=tokenizer, ngram_range=(1, ngram), use_idf=True, binary=False, lowercase=False)

    X = vect.fit_transform(lemma_targets_laws_df["body"].values.astype('U'))  # astype to convert into a string

    # dataframe containing the document terms matrix
    doc_term_matrix = DataFrame(X.toarray(), columns=vect.get_feature_names_out(), index=index)

    # only for test purposes
    # doc_term_matrix.to_excel("prova.xlsx")

    return doc_term_matrix


# ---------------------------- UTILS -------------------------------------
def __get_path__(relative_path):
    """
    Converts the relative path into an absolute path
    :param relative_path: relative path of the file
    :return: string
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


"""
# test
# remove triple prime to test the class

if __name__ == '__main__':
    print(tfidf(path_law="laws\\[2015-2020]LeggiRegionePuglia\\LR_10.2016.pdf"))
"""
