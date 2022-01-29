# -*- coding: utf-8 -*-
"""
Created on Fr Jan 28 12:02:50 2022

@author: ClaudiaLorusso
"""
from Preprocessing import tfidf
from sklearn.metrics.pairwise import cosine_similarity
from pandas import DataFrame
import sys
from os import path

def get_cossim(ngram = 1, path_law = ""):
    """
    Computes a DataFrame containing the cossim matrix,
    starting from the TFIDF term document matrix,
    between the law and all of the targets.

    :param ngram: integer
        number of tokens into each keyphrase
    :param path_law: string
        directory + name of the file containing the law
    :return: DataFrame
        containing the cossim matrix
    """
    path_law = __get_path__(path_law)
    df_doc_term_matrix = tfidf(ngram, path_law)
    # get indexes with
    indx_targtes = df_doc_term_matrix.index[0:-1]
    #get law name
    indx_law = df_doc_term_matrix.index[-1]

    #get matrix
    tf_idf_matrix = df_doc_term_matrix.to_numpy()

    cols = []
    for t in indx_targtes.tolist():
        cols.append(t)
    #print("colonne:\n", cols, "\n")

    #TODO
    targets_matrix = tf_idf_matrix[:169, 1:]  # [:17,1:] use this for sdgs
    #print("target matrix:\n", targets_matrix, "\n")
    #TODO
    laws_matrix = tf_idf_matrix[169:, 1:]  # [17:,1:] use this for sdgs
    #print("law matrix:\n", targets_matrix, "\n")

    cossim = cosine_similarity(laws_matrix, targets_matrix)

    cossim_df = DataFrame(cossim, columns=cols)
    cossim_df.index.name = "law name"
    cossim_df.rename(index={0: indx_law}, inplace=True)

    return cossim_df

def get_relevant(ngram = 1, path_law = ""):
    """
    Computes the first three relevant targets
    detected by the cossim matrix.
    :param ngram: integer
        number of tokens contained into each keyphrase
    :param path_law: string
        directory + name of the file containing the law
    :return: string
        containing the first three relevant targets
    """
    path_law = __get_path__(path_law)
    cossim_df = get_cossim(ngram, path_law)
    #to change the number of targets outputted
    #just switch the number 3 to whatever you want
    largest = cossim_df.stack().nlargest(3)
    largest = largest.multiply(100)

    rel= largest.to_string()
    relevant = "\t\t\tTarget\t%\n"+rel

    return relevant

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
    print(get_relevant(path_law="laws\\[2015-2020]LeggiRegionePuglia\\LR_10.2016.pdf"))
"""
