# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:54:57 2022

@author: ClaudiaLorusso
"""
import pandas as pd

def count_occurences(law, pattern):
    """
    Counts the occurrences of a substring (second argument)
    into the main string (first argument)
    :param law: string
        law's content
    :param pattern: string
        substring
    :return: integer
        occurrences of the substring into the main string
    """
    law = " ".join(law.split())
    return law.count(pattern)


def preprocess_law(law):
    """
    Preprocesses the specified string containing the law's content (argument)
    returning it's lemma.
    :param law: string
        content of the law
    :return: string
        lemma of the law
    """
    from Preprocessing import clean_text, remove_new_lines, preprocess_lemma
    txt = clean_text(law)
    txt = remove_new_lines(txt)
    lemma = preprocess_lemma(txt)
    return lemma

def get_df_laws_lemma(path_law = ""):
    """
    Computes the DataFrame of the law's lemma.
    The dataframe is in the form:
        name        |body
        laws_name    law's lemma
    :param path_law: string
        path of the file containing the law
    :return: DataFrame
        dataframe containing the law's lemma
    """
    from FileHandler import get_content
    try:
        cont, file_name = get_content(path_law)
        lemma = preprocess_law(cont)
        df = pd.DataFrame(columns = ["name", "body"])
        df= pd.DataFrame(df).set_index("name")
        df.loc[file_name] = lemma
        df.index.name = "name"
        return df
    except ValueError:
        print("ValueError: WARNING, The file you selected maybe protected by password.\nPlease select another file.")

#test
#remove triple prime to test the class
"""
if __name__ == '__main__':
    df = get_df_laws_lemma("laws\\[2015-2020]LeggiRegionePuglia\\LR_10.2016.pdf")
    print(df)
"""