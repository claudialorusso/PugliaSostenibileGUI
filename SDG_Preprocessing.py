# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:34:13 2021

@author: ClaudiaLorusso
"""

from Preprocessing import preprocess_lemma, compute_vocabulary
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
    -   computes the vocabulary.
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

    # creates a DataFrame that will contain the lemma of the SDGs (goals+targets)
    df_sdgs = pd.DataFrame(columns=['name', 'body'])
    df_sdgs = pd.DataFrame(df_sdgs).set_index("name")

    # creates a DataFrame that will contain the lemma of the targets (only)
    df_targets = pd.DataFrame(columns=['name', 'body'])

    df_targets = pd.DataFrame(df_targets).set_index("name")

    for sdg in sdgs:
        txt_goal = __preprocess_goal__(sdg)
        txt_targets, df_tgs = __preprocess_targets__(sdg)
        txt_lemm = txt_goal + " " + txt_targets
        df_sdgs.loc[sdg.get_Goal_id()] = [txt_lemm]
        df_targets = pd.concat([df_targets, df_tgs])

    df_sdgs.index.name = "name"
    df_targets.index.name = "name"

    dest_sdg = __get_path__("LEMMAS\\lemma_sdgs.xlsx")

    dest_tgts = __get_path__("LEMMAS\\lemma_targets.xlsx")
    df_sdgs.to_excel(dest_sdg)
    df_targets.to_excel(dest_tgts)


def __preprocess_goal__(sdg):
    """
    Preprocesses the Goal description, after getting it from the corresponding sdg (argument):
    -   removes all of the digits
    -   computes the LEMMA using SPACY
    -   lowercases the corresponding LEMMA
    -   removes all of the trailing spaces

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

    lemma = preprocess_lemma(txt)

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

    df_tgs.index.name = "name"
    return lemma, df_tgs


def __preprocess_target__(target):
    """
    Preprocess the description of a single target (argument):
    -   removes all of the digits
    -   computes the LEMMA using SPACY
    -   lowercases the corresponding LEMMA
    -   removes all of the trailing spaces

    Parameters
    ----------
    target : target da processare.

    Returns
    -------
    None.

    """

    txt = target.get_description()
    lemma = preprocess_lemma(txt)

    return lemma


def __get_path__(relative_path):
    """
    Converts the relative path into an absolute path
    :param relative_path: string
        relative path of the file
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


def get_vocabulary(path_lemma_sdgs):
    """
    Computed the vocabulary of the SDGs.
    :param path_lemma_sdgs: string
        path + name of the xlsx containing sdgs lemma
    :return: list of strings
        sdg's vocabulary
    """
    voc = compute_vocabulary(path_lemma_sdgs, 2)
    return voc


# test
# remove triple prime to test the class
"""
if __name__ == '__main__':
    preprocess_SDGs()
    get_vocabulary("LEMMAS\\lemma_sdgs.xlsx")
"""
