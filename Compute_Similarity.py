# -*- coding: utf-8 -*-
"""
Created on Fr Jan 28 12:02:50 2022

Computes the n most relevant sdgs or targets based on the law the user inputted.
The computation is done by means of the cosine similarity.
@author: ClaudiaLorusso
"""
from Preprocessing import tfidf
from sklearn.metrics.pairwise import cosine_similarity
from pandas import DataFrame
import sys
from os import path

def get_cossim(ngram = 1, path_law = "", sim_target = False):
    """
    Computes a DataFrame containing the cossim matrix,
    starting from the TFIDF term document matrix,
    between the law and all of the sdgs (or targets, if sim_target = True).

    :param ngram: integer
        number of tokens into each keyphrase
    :param path_law: string
        directory + name of the file containing the law
    :param sim_target: boolean
        True if the user wants to compute the similarity between the law and each target (only)
        False if he wants to compute the similarity between the law and each SDGs (SDG = Goal + list of Target)
    :return: DataFrame
        containing the cossim matrix
    """
    path_law = __get_path__(path_law)
    df_doc_term_matrix = tfidf(ngram = ngram, path_law = path_law, sim_target = sim_target)
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

    if sim_target:
        targets_matrix = tf_idf_matrix[:169, 1:]  # [:17,1:] use this for sdgs
        #print("target matrix:\n", targets_matrix, "\n")
        laws_matrix = tf_idf_matrix[169:, 1:]  # [17:,1:] use this for sdgs
        #print("law matrix:\n", targets_matrix, "\n")
    else:
        targets_matrix = tf_idf_matrix[:17,1:]
        #print("target matrix:\n", targets_matrix, "\n")

        laws_matrix = tf_idf_matrix[17:,1:]
        #print("law matrix:\n", targets_matrix, "\n")

    cossim = cosine_similarity(laws_matrix, targets_matrix)

    cossim_df = DataFrame(cossim, columns=cols)
    cossim_df.index.name = "law name"
    cossim_df.rename(index={0: indx_law}, inplace=True)

    return cossim_df

def get_relevant(ngram = 1, path_law = "", sim_target = False):
    """
    Computes the first n (= 3) relevant targets
    detected by the cossim matrix.
    :param ngram: integer
        number of tokens contained into each keyphrase
    :param path_law: string
        directory + name of the file containing the law
    :param sim_target: boolean
        True if the user wants to compute the similarity between the law and each target (only)
        False if he wants to compute the similarity between the law and each SDGs (SDG = Goal + list of Target)
    :return: string
        containing the first n (= 3) relevant targets
    """

    path_law = __get_path__(path_law)
    cossim_df = get_cossim(ngram = ngram, path_law = path_law, sim_target = sim_target)

    # cossim_df.to_excel("file.xlsx") #TEST PURPOSES

    #to change the number of targets outputted
    #just switch the number 3 to whatever you want
    n = 3
    largest = cossim_df.stack().nlargest(n)
    largest = largest.multiply(100).round(2)
    largest = largest.unstack()

    columns = []
    for col in largest.columns:
        if sim_target:
            column = "Target\t"
        else:
            column = "SDG\t"
        column += str(col)
        columns.append(column)

    values = largest.iloc[0].tolist()
    relevant = ""
    for col, perc in zip(columns, values):
        relevant += col + ":\t"+ str(perc) + "%\n"
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
