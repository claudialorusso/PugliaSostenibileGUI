# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:54:57 2022

@author: ClaudiaLorusso
"""
from Preprocessing import clean_text, remove_new_lines, preprocess_lemma

def preprocess_law(law):
    """
    Preprocesses the specified string containing the law's content (argument)
    returning it's lemma.
    :param law: string
        content of the law
    :return: string
        lemma of the law
    """
    txt = clean_text(law)
    txt = remove_new_lines(txt)
    lemma = preprocess_lemma(txt)
    return lemma

#test
#remove triple prime to test the class
"""
if __name__ == '__main__':
    from FileHandler import get_content
    try:
        cont = get_content()
        lemma = preprocess_law(cont)
        print(lemma)
    except ValueError:
        print("ValueError: WARNING, The file you selected maybe protected by password.\nPlease select another file.")
"""