# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:34:13 2021

@author: ClaudiaLorusso
"""

from Preprocessing import remove_digits, get_lemma_SPACY
from SDGs_Extractor import SDGs_Extractor
import pandas as pd
import sys
from os import path

"""
Offers the method to preprocess all of the SDGs.
NB. By default was chosen to preprocess the SDGs_indicatori.json file
which contains each SDG in addition to the global indicators.
If you want to compute only the SDGs please change the path in the SDGs_Extractor class
to SDG_jason.json .

On both goals and targets description:
    -   removes all of the digits
    -   computes the LEMMA using SPACY
    -   lowercases the corresponding LEMMA
    -   removes all of the trailing spaces
At the end, you'll get a new folder with two xls:
    -   "LEMMAS\\lemma_sdgs.xlsx" : which contains the lemma of all of the SDGs
    -   "LEMMAS\\lemma_targets.xlsx": which contains the lemma of all of the targets (only)
"""

def preprocess_SDGs():
    """
    Preprocess all of the SDGs creating, respectively:
    -   one file xls containing sdgs (SDG = goal + target) lemma
    -   one file xls containing only targets lemma
    :return:
    """
    extractor = SDGs_Extractor()
    # processes each SDG inserting them into an SDGs object
    sdgs = extractor.get_SDGs()
    """
    #initializes the vocab to an empty set to ensure no duplicates #FIX ME
    sdgs_vocab = set()
    """
    #creates a DataFrame that will contain the lemma of the SDGs (goals+targets)
    # index = name, column = body
    df_sdgs = pd.DataFrame(columns=['name', 'body'])
    df_sdgs = pd.DataFrame(df_sdgs).set_index("name")

    # creates a DataFrame that will contain the lemma of the targets (only)
    # index = name, column = body
    df_targets = pd.DataFrame(columns=['name','body'])

    df_targets = pd.DataFrame(df_targets).set_index("name")

    for sdg in sdgs:
        txt_goal = __preprocess_goal__(sdg)
        txt_targets, df_tgs = __preprocess_targets__(sdg)
        txt_lemm = txt_goal + " " + txt_targets
        df_sdgs.loc[sdg.get_Goal_id()] = [txt_lemm]
        df_targets = pd.concat([df_targets, df_tgs])
        """
        # processo il vocabulary
        for tok in sdg.get_occurrences():
            sdgs_vocab.add(tok[0])
        """
    df_sdgs.index.name = "name"
    df_targets.index.name = "name"

    """
    df_vocab = pd.DataFrame(columns=['keyphrase'])

    i = 0
    for keyphrase in sdgs_vocab:
        df_vocab.loc[i] = [keyphrase]
        i += 1

    # df_vocab.to_excel("SDGs_utils/Unigram_vocab.xlsx") #FIXME
    # self.__set_inv_vocabulary__(sdgs, sdgs_vocab)
    """

    dest_sdg = __get_path__("LEMMAS\\lemma_sdgs.xlsx")


    dest_tgts = __get_path__("LEMMAS\\lemma_targets.xlsx")
    #print("I'm creating the first xls")
    df_sdgs.to_excel(dest_sdg)
    #print("I'm done creating the first xls")
    #print("I'm creating the first xls")
    df_targets.to_excel(dest_tgts)
    #print("I'm done creating the second xls")

    # FIXME
    #return sdgs

def __preprocess_goal__(sdg):
    """
    Preprocesses the Goal description, after getting it from the corresponding sdg (argument):
    -   removes all of the digits
    -   computes the LEMMA using SPACY
    -   lowercases the corresponding LEMMA
    -   removes all of the trailing spaces
    -   DEPRECATED computes all of the keyphrases using RAKE #FIXME
    -   DEPRECATED computes the occurence value for each keyphrase

    Parameters
    ----------
    sdg : SDG
        the sdg from which extract the description of the goal with the aim to process it

    Returns
    -------
    None.

    """

    goal = sdg.get_Goal()
    txt = goal.get_description()

    lemma = __preprocess_lemma__(txt)

    """
    # use this for test purposes
    print("\n\nLEMMA\n")
    print(txt)
    print("\n\n")
    """

    """
    # DEPRECATED
    # computes keyphrases using RAKE
    # setted to bigram for default.
    # To choose unigram change the value max_words from 2 to 1
    # in the get_keyphrase method
    tokens = txt_prs.get_keyphrase(txt)
    # following line for test purposes only
    # print(tokens)
    """



    """
    # NOT NEEDED ANYMORE
    # get occurrences of each keyphrase contained in the description
    for tok in tokens:
        keyphrase = tok[0]
        occurrence = txt_prs.find_pattern(keyphrase, txt)
        item = tuple([keyphrase, occurrence])
        sdg.add_occurrence(item) #FIXME controlla
    """

    """
    # use this for test purposes
    print("TF\n")
    print(sdg.get_occurrences())
    """

    return lemma


def __preprocess_targets__(sdg):
    """
    Uses the __preprocess_targets__ method on each target
    that belongs to sdg (argument) to preprocess their description.
    Computes the dataframe containing the lemma of the description of
    the targets (and not of the goal).
    Parameters
    ----------
    sdg : sdg to be preprocessed

    Returns
    -------
    lemma: a string containing the lemma of all of the targets
    df_tgs: dataframe of the corresponding targets' lemma
    """
    df_tgs = pd.DataFrame(columns=['name', 'body'])

    df_tgs = pd.DataFrame(df_tgs).set_index("name")

    lemma = ""
    for target in sdg.get_Target_list():
        txt_tg = __preprocess_target__(target)
        lemma += " " + txt_tg
        index = str(target.get_Goal_id()) + "." + str(target.get_id())
        df_tgs.loc[index] = [txt_tg]

        """
        # NOT NECESSARY ANYMORE
        # FIXME
        # update sdg occurrences
        occurrence_table = target.get_occurrences()
        for tup in occurrence_table:
            inside = False
            for t in sdg.get_occurrences():
                if tup[0] == t[0]:
                    inside = True
                    # print("\nI'm inside\n")
                    newTuple = tuple([tup[0], t[1] + tup[1]])
                    sdg.update_occurrence(t, newTuple)
                    break
            if not inside:
                sdg.add_occurrence(tup)
        """
    df_tgs.index.name = "name"
    return lemma, df_tgs

def __preprocess_target__(target):
    """
    Preprocess the description of a single target (argument):
    -   removes all of the digits
    -   computes the LEMMA using SPACY
    -   lowercases the corresponding LEMMA
    -   removes all of the trailing spaces
    -   DEPRECATED computes all of the keyphrases using RAKE #FIXME
    -   DEPRECATED computes the occurence value for each keyphrase

    Processa ogni singolo target corrispondente ad una sdg.

    Parameters
    ----------
    target : target da processare.

    Returns
    -------
    None.

    """


    txt = target.get_description()
    lemma = __preprocess_lemma__(txt)

    """
    # use this for test purposes
    print("\n" + txt + "\n")
    """

    """
    # NOT NEEDED ANYMORE
    # FIXME
    # computes the keyphrases with RAKE
    tokens = txt_prs.get_keyphrase(txt)
    """
    """
    # use this for test purposes
    # print("\n")
    # print(tokens)
    """

    """
    # NOT NEEDED ANYMORE
    # FIXME
    # ottengo le occorrenze delle keyphrase
    for tok in tokens:
        # print(tok[0])
        keyphrase = tok[0]  # txt_prs.trim((tok[0]))#.lower()
        occurrence = txt_prs.find_pattern(keyphrase, txt)

        item = tuple(
            [keyphrase, occurrence])
        target.add_occurrence(item)
    """
    """
    # use this for test purposes
    print(target.get_occurrences())
    print("\n\n\n")
    """
    return lemma

def __preprocess_lemma__(txt):
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

    """
    # NOT NECESSARY ANYMORE
    # already done while saving SDGs on .json
    from Preprocessing import replace symb
    txt = replace_symb("’", "'", target.get_description())
    txt = replace_symb("“", '"', txt)
    txt = replace_symb("”", '"', txt)
    """

    # removes digits
    txt = remove_digits(txt)
    # gets lemma applying SPACY and lower cases the output
    lemma = (get_lemma_SPACY(txt)).lower()

    #removes unnecessary spaces
    lemma = " ".join(lemma.split())
    return lemma

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






# FIXME not needed anymore
def __set_inv_vocabulary__(sdgs, sdgs_vocab):
    """
    Genera il vocabolario inverso degli SDGs

    Parameters
    ----------
    sdgs : oggetto della classe SDGs
    sdgs_vocab : set
        insieme di tutte le keyohrase contenute negli sdgs

    Returns
    -------
    restituisce la grandezza del vocabolario

    """
    # genero il vocabulary di tutti gli SDGS
    v = list(sdgs_vocab)
    sdgs.set_inv_vocabulary(dict([word, i] for i, word in enumerate(v)))


#test
#remove triple prime to test the class
"""
if __name__ == '__main__':
    preprocess_SDGs()

"""
