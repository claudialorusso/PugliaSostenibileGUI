# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:36:52 2021
@author: Claudia Lorusso
"""


class File_Handler:
    """
    Questa classe permette di estrarre
    del testo da file.
    Le tipologie di file supportati per l'estrazione
    sono:
        - txt
        - docx
        - pdf
    """

    # TODO: aggiungere altri formati, in caso, modificare descrizione

    # def __init__(self)

    # def get_file_name(self, name):

    def extract_txt(self, destination):
        """
        Estrae il testo dal documento di testo
        '.txt', sottoforma di liste di stringhe
        Parameters
        ----------
        destination : destinazione del file di testo da estrarre
        Returns
        -------
        lista di stringhe corrispondenti al testo
        """
        file = open(destination, "r", encoding="utf-8")
        text = file.readlines()
        file.close()
        return text

    def extract_pdf(self, destination):
        """
        Estrae il testo dal documento di testo
        '.pdf', sottoforma di liste di stringhe
        Parameters
        ----------
        destination : destinazione dei file pdf da estrarre
        Returns
        -------
        lista di stringhe corrispondenti ai testi
        contenute all'interno delle leggi (la i-esima cella della lista
        conterrà tutto il contenuto in formato stringa della i-esima legge estrapolata).
        Lista contenente tutti i nomi dei file pdf da cui sono state estratte le informazioni.
        """
        import fitz
        from os import listdir
        namesPDF = []
        doc = []
        for file in listdir(destination):
            text = ""
            namesPDF.append(file)
            pdf = fitz.open(destination + "/" + file)
            for i in range(pdf.page_count):
                page = pdf.load_page(i)
                text = text + " " + page.get_text("text")
            pdf.close()
            text = text.strip(" ")
            text = " ".join(text.split())
            doc.append(text)

        return doc, namesPDF