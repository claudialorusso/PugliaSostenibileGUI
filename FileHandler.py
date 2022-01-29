# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:36:52 2021

Contains methods to manage files with the following extensions:
    - .txt
    - .docx
    - .pdf

@author: Claudia Lorusso
"""

import sys
from os import path


def ask_path():
    """
    Asks the user for the path's file
    :return:
        destination: path of the file
    """
    exists = False
    destination = ""
    while not exists:
        destination, exists = __check_file__()
    return destination


def __check_file__():
    """
    Checks if the file actually exists.
    :return:
        destination: path of the file
        exists: control variable: it is True if the file actually exists; either it is False.
    """
    destination = input("Enter Filename:\t")
    exists = True
    if path.isfile(destination):
        if destination.endswith((".txt", ".pdf", ".docx")):
            pass
        else:
            print("Invalid file extension: '.TXT', '.PDF' and '.DOCX' only.")
            exists = False
    else:
        print("File doesn't exist OR missed extension. Please try again.")
        exists = False
    return destination, exists


def extract_content(destination):
    """
    Extracts the content of the specified file by destination.
    The file must either: ".txt", ".docx", ".pdf"
    The content is then saved into a string.
    Return an empty string in case the file is empty.
    :param destination: path of the doc
    :return: string
        content: a string that contains the content of the file
    :raises:
        ValueError: in case the specified file is protected by password
    """
    content = ""
    try:
        if destination.endswith(".txt"):
            content = __extract_txt__(destination)
        elif destination.endswith(".docx"):
            content = __extract_docx__(destination)
        elif destination.endswith(".pdf"):
            content = __extract_pdf__(destination)
    except Exception:

        raise ValueError(
            "ValueError: WARNING, The file you selected maybe protected by password.\nPlease select another file.")
    return content


def __extract_txt__(destination):
    """
    Extracts the content of a .txt file.
    :param destination: path of the .txt file
    :return: string
        content: string that contains the content of the file
    """
    content = ""
    with open(destination, 'r', encoding='utf-8', errors="ignore") as file:
        for line in file:
            content += line
    return content


def __extract_docx__(destination):
    """
    Extracts the content of a .docx file.
    :param destination: path of the .docx file
    :return: string
        content: string that contains the content of the file
    """
    import docx
    doc = docx.Document(destination)
    content = ""
    for paragraph in doc.paragraphs:
        txt = paragraph.text
        content += txt
    return content


def __extract_pdf__(destination):
    """
    Extracts the content of a .pdf file.
    :param destination: path of the .pdf file
    :return: string
        content: string that contains the content of the file
    """
    import PyPDF2
    # creating an object
    file = open(destination, 'rb')
    # creating a pdf reader object
    file_reader = PyPDF2.PdfFileReader(file, strict=False)
    content = ""
    for page in file_reader.pages:
        for line in page.extractText().splitlines():
            content += line
    file.close()
    return content


def __get_path__(relative_path):
    """
    Converts the relative path into an absolute path
    :param relative_path: relative path of the file
    :return: string
        absolute path: base path + relative path
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)


def get_content(destination = ""):
    """
    Returns the content of a specified path.
    If no argument is setted asks the path, then extracts the content.
    :param destination: string
        path of the file
    :return:
        cont:   string
            content of a specified text
        file_name: string
            file_name
    """

    if destination == "":
        destination = ask_path()
    else:
        destination = __get_path__(destination)
    cont = extract_content(destination)
    file_name = get_filename_no_extension(destination)

    return cont, file_name

def get_basename(destination):
    """
    Returns the basename of a file:
    E.g.
        argument = "C:\\something\\something_again\\IwantThis.some_extension"
        file_name = "IwantThis.some_extension"
    :param destination: string
        path of the file
    :return: string
        basename of the destination
    """
    file_name = path.basename(destination)
    return file_name

def get_filename_no_extension(file_name):
    """
    Returns the basename with no extension
    E.g.
        argument = "C:\\something\\something_again\\IwantThis.some_extension"
        file_name = "IwantThis"
    :param file_name: string
        destination of a file.
    :return: string
        filename with no extension
    """
    file_name = get_basename(file_name)
    path.splitext(file_name)
    return path.splitext(file_name)[0]


def filetypes():
    """
    Returns all of the filetypes allowed
    :return:
    tuple of all of the filetypes allowed
    """
    filetypes = (
        ("*.txt", "*.txt"),
        ("*.docx", "*.docx"),
        ("*.pdf", "*.pdf")
    )
    return filetypes

#test
#remove triple prime to test the class
"""
if __name__ == '__main__':
    try:
        cont = get_content()
        print(cont)
    except ValueError:
        print("ValueError: WARNING, The file you selected maybe protected by password.\nPlease select another file.")
"""
