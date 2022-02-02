# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:39:51 2022

@author: ClaudiaLorusso
"""

from tkinter import *
from tkinter import ttk, scrolledtext, messagebox
from tkinter import filedialog as fd
import webbrowser

#from tkinter.filedialog import asksaveasfile
import sys
from os import path


class Installation:
    """
    Manages the installation GUI.
    If it is the first execution OR the user doesn't dispose of the needed libs
    asks him if he wants to download them, in which case the program proceeds
    with the installation. Else, he can easly close the window.
    """

    def __init__(self):

        # ------------------------------- Termination variable. Default = False; if True wont open App.
        self.__termination__ = False
        # ------------------------------- Installation root creation
        self.__installation_root__ = Tk()
        self.__installation_root__.title("Puglia Sostenibile: Installazione")
        # path logo
        logo = __get_path__("utils\\images\\PugliaSostenibile2200x2239.png")
        # -----------------logo
        self.__logo__ = PhotoImage(file=logo)
        # path logo
        logo_min = __get_path__("utils\\images\\COLORPugliaSostenibile175x161.png")
        # -----------------logo minimized
        self.__mini_logo__ = PhotoImage(file=logo_min)
        # path ico
        ico = __get_path__("utils\\images\\PugliaSostenibileICO.ico")
        # -----------------ico
        self.__ico__ = ico
        # set root icon
        self.__set_ico__()
        # set root title
        self.__title__ = "Program Installation"
        self.__set_title__(self.__title__)
        # ---------------------------------- Master installation frame creation
        self.__master_frame__ = Frame(self.__installation_root__)
        self.__master_frame__.grid(row=0, column=0)
        # ---------------------------------- Dialog Frame creation
        self.__up_dialog_frame__ = Frame(self.__master_frame__)
        self.__up_dialog_frame__.grid(row=0, sticky=W, padx=(5))
        # ---------------------------------- Image installation lbl
        self.__image_lbl__ = Label(self.__up_dialog_frame__, image=self.__mini_logo__, justify="center")
        self.__image_lbl__.grid(row=0, column=0, padx=(10), pady=10)
        # ---------------------------------- Welcome installation Frame creation
        self.__welcome_frame__ = Frame(self.__up_dialog_frame__)
        self.__welcome_frame__.grid(row=0, column=1, sticky=W, padx=(5))
        # ---------------------------------- Welcome installation lbl
        self.__welcome_lbl__ = Label(self.__welcome_frame__, text='Puglia Sostenibile: Installazione',
                                     font=("Bahnschrift SemiCondensed", 20, "bold"), justify="left")
        self.__welcome_lbl__.grid(row=0, column=1, sticky=N + W, pady=5)
        # ---------------------------------- Instruction installation lbl
        self.__instruction_lbl__ = Label(self.__welcome_frame__, justify="left",
                                         text='A quanto pare è la prima volta che esegui Puglia Sostenibile, BENVENUTO!\n\n'
                                              'Per utilizzare correttamente il programma è necessario installare alcune librerie.\n\n'
                                              'Per favore, assicurati di aver installato sulla tua macchina Python 3.9 o versioni\nprecedenti'
                                              ' e di essere connesso ad internet.',
                                         font=("Times New Roman", 12))
        self.__instruction_lbl__.grid(row=1, column=1, sticky=N + W, pady=10)
        # ---------------------------------------------------- TEXTBOX Frame
        self.__box_frame__ = LabelFrame(self.__master_frame__, text="Le seguenti librerie verranno installate:", padx=5,
                                        pady=5)
        self.__box_frame__.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E + W + N + S)

        self.__installation_root__.columnconfigure(0, weight=1)
        self.__installation_root__.rowconfigure(1, weight=1)

        self.__box_frame__.rowconfigure(0, weight=1)
        self.__box_frame__.columnconfigure(0, weight=1)

        # Create the textbox widget
        self.__txt_box__ = scrolledtext.ScrolledText(self.__box_frame__, width=40, height=10,
                                                     font=("Times New Roman", 12))
        self.__txt_box__.grid(row=0, column=0, sticky=E + W + N + S)
        self.__txt_box__.insert(INSERT, self.__get_packages__())
        self.__txt_box__.configure(state="disabled")

        # -----------------------------------------------Accept frame creation
        self.__accept_frame__ = Frame(self.__master_frame__)
        self.__accept_frame__.grid(row=2, padx=(10), pady=10, sticky=W)

        # accept installation boolean variable
        self.__accept_terms__ = BooleanVar()

        # check button
        self.__check_btn__ = Checkbutton(self.__accept_frame__,
                                         text="Acconsento il download e l'installazione delle librerie soprariportate. Clicca sul pulsante 'Avanti' per continuare",
                                         variable=self.__accept_terms__, onvalue=True, offvalue=False,
                                         command=self.__manage_next_btn__)
        self.__check_btn__.grid(row=0, sticky=W)

        # next button
        self.__next_btn__ = Button(self.__accept_frame__, text='Avanti', state=DISABLED, width=10, command=self.__bar__)
        self.__next_btn__.grid(row=2, sticky=E + S, pady=10)

        # termination program variable
        terminate = BooleanVar()

        # progress bar
        self.__progress__ = ttk.Progressbar(self.__accept_frame__, orient=HORIZONTAL, length=700, mode="determinate")
        self.__progress__.grid(row=1, sticky=W)

        # defines min and max root dimension
        self.__installation_root__.update()
        self.__installation_root__.minsize(self.__installation_root__.winfo_width(),
                                           self.__installation_root__.winfo_height())
        self.__installation_root__.maxsize(self.__installation_root__.winfo_width(),
                                           self.__installation_root__.winfo_height())
        # terminate installation, open app
        self.__installation_root__.mainloop()

    def get_terimantion(self):
        """
        Returns the termination variable
        :return:
            the termination variable = True if libs were correctly installed
        """
        return self.__termination__

    def __set_ico__(self):
        """
        Sets the icon of the installation root
        :return:
        """
        self.__installation_root__.iconbitmap(self.__ico__)
        self.__installation_root__.wm_iconphoto(True, self.__logo__)

    def __set_title__(self, title):
        """
        Sets installation root title
        :param title: string which contains installation root title
        :return:
        """
        self.__installation_root__.title(title)

    def __get_packages__(self):
        """
        Puts into a string all of the libraries required to correctly run Puglia Sostenibile.
        Libraries names and versions are taken from the requirements.txt file.
        The test is in the form:
        pack = "lib_1==#version_1\nlib_2==#version_2\n[...]\nlib_n==version_n\n"
        :return:
            A string containing all the Packages required for the installation of Puglia Sostenibile
        """
        pack = "\n"
        with open("requirements.txt", 'r') as f:
            for line in f:
                pack = pack + line + "\n"
        return pack

    def __manage_next_btn__(self):
        """
        Enables and Disables the next button in the installation root.
        If the checkbox value, accept_terms, is set to True the next button is activated.
        :return:
        """
        self.__next_btn__.configure(state="disabled" if not self.__accept_terms__.get() else "normal")

    def __install_libs__(self):
        """
        Download and installs required libraries from requirement.txt file
        :return:
        """
        from subprocess import run
        # implement pip as a subprocess:
        # I start with scikit-learn 'cause of dependencies
        run(["pip3", "install", "scikit-learn == 1.0.2"], shell=True, capture_output=True)
        run(["pip3", "install", "-r", "requirements.txt"], shell=True, capture_output=True)

    def __import_packs__(self):
        """
        Imports needed packages while managing the progress bar
        :return:
        """
        from re import sub
        self.__installation_root__.update_idletasks()
        self.__progress__["value"] = 47
        from tkPDFViewer import tkPDFViewer as pdf
        self.__progress__["value"] = 60
        self.__installation_root__.update_idletasks()
        from Compute_Similarity import get_relevant
        self.__progress__["value"] = 76
        self.__installation_root__.update_idletasks()
        from FileHandler import ask_path, extract_content
        self.__progress__["value"] = 87
        self.__installation_root__.update_idletasks()

    def __disable_widgets__(self):
        """
        Disables check_btn and next_btn.
        :return:
        """
        self.__check_btn__.configure(state=DISABLED)
        self.__next_btn__.configure(state=DISABLED)

    def __bar__(self):
        """
        Manages the progress bar while installing the required processes and importing
        required packages.
        Destroys installation root after installation.
        :return:
        """
        # disable checkbox and next buttons
        self.__disable_widgets__()
        # download and install packages
        self.__progress__["value"] = 5
        self.__installation_root__.update_idletasks()
        self.__install_libs__()
        self.__progress__["value"] = 55
        self.__import_packs__()
        self.__termination__ = True
        self.__progress__["value"] = 100
        self.__installation_root__.update_idletasks()
        # destroy the installation root
        self.__installation_root__.destroy()


class App:
    """
    Defines the Puglia Sostenibile GUI.
    Pressing the "Select File" button the user can simply choose the desired file that has one of the following extentions:
    - .pdf
    - .docx
    - .txt
    Pressing the "Start" button, the program will compute the reading time of the doc.
    The game is done.

    BASICALLY:
    The GUI is divided into two main vertical Frames, inserted into a __master_frame__:
        - __left_frame__ (0,0):
                contains the logo ( into __up_dialog_frame__ (0, 0)) and the
                buttons ( into __button_frame__ (1, 0)).
                Each button manages the selection of the desired Variable Frame.
        - __line_frame__ (0, 1): contains a vertical image with each SDG representation.
        - __right_frame__ (0, 2): contains:
                -   the __title_lbl__ (0, 0): "Puglia Sostenibile"
                -   the __mid_title_lbl__ (1, 0): changes based on the button
                    the user has pressed on:
                    -   0:  (Default) Home
                    -   1:  Informazioni
                    -   2:  Avanzate
                    -   3:  Agenda 2030
                    -   4:  Contatti
                - the __mid_descr_lbl__ (2, 0): changes based on the button
                    the user pressed on:
                    -   0:  (Default) Home description
                    -   1:  Informazioni description
                    -   2:  Avanzate description
                    -   3:  Agenda 2030 description
                    -   4:  Contatti description
                -   the variable Frames (each in the same spot: (3, 0))
                    -   __home_frame__ :
                            it's the core of the program.
                            it's divided into two main frames:
                            -   __home_up_frame__ (0, 0): it's the place in which the user can,
                                finally, use Puglia Sostenibile. He must select the Law,
                                Press on the Start Button and the result will appear in the output box
                            -   __home_down_frame__ (1, 0): if the user has already selected a law in this section
                                he can also search occurrences of some keyphrase in the text.
                                He must insert the keyphrase in the box and click on the "Cerca" button
                                (or press the "Enter" key on the keyboard).
                                The result will appear under the box.
                    -   __info_frame__ :    #TODO
                    -   __adv_frame__ :     Enables the user to change the Grammature from Unigram to Bigram and
                                            vice-versa.
                    -   __agenda_frame__ :  Permits the user to consult the pdf of the Agenda 2030.
                    -   __contact_frame__ : #TODO

    """

    def __init__(self):

        # ------------------------------- Installation root creation
        self.__root__ = Tk()

        # -----set root to full screen
        pad = 3
        self.__root__.geometry("{0}x{1}+0+0".format(
            self.__root__.winfo_screenwidth() - 3, self.__root__.winfo_screenheight() - 3))
        # -----set root to full screen

        self.__root__.configure(background="white")
        # self.__root__.attributes('-alpha', )#('-alpha', 1.0)#    "transparentcolor", '#ab23ff'
        # Make the root window always on top

        # set root title
        title = "Puglia Sostenibile"
        self.__set_title__(title)

        # path logo
        logo = __get_path__("utils\\images\\PugliaSostenibile2200x2239.png")
        # -----------------logo
        self.__logo__ = PhotoImage(file=logo)
        # path logo
        logo_min = __get_path__("utils\\images\\COLORPugliaSostenibile200x184.png")
        # -----------------logo minimized
        self.__mini_logo__ = PhotoImage(file=logo_min)
        # path ico
        ico = __get_path__("utils\\images\\PugliaSostenibileICO_black.ico")
        # -----------------ico
        self.__ico__ = ico
        # set root icon
        self.__set_ico__()


        #                            ---------------    MASTER FRAME    ---------------

        self.__master_frame__ = Frame(self.__root__)
        self.__master_frame__.pack(side=LEFT, anchor="ne", padx=(10), pady=10, ipadx=(10), ipady=10)
        self.__master_frame__.config(bg='white')


        #                            ---------------    TOP LEFT    ---------------

        # --------------------------------------------------------------- Left frame creation (where the magic happens)
        self.__left_frame__ = Frame(self.__master_frame__)  # , background = "#ab23ff")#, background= "#88cffa")#F6ECEC
        #self.__left_frame__.pack(side=LEFT, anchor="ne", padx=(10), pady=10, ipadx=(10), ipady=10)
        self.__left_frame__.grid(row = 0, column = 0, padx=(10), pady=10, ipadx=(10), ipady=10, sticky = "nw")
        self.__left_frame__.config(bg='white')

        # -------------------------------------------------------------------------------------- UP Dialog Frame creation
        self.__up_dialog_frame__ = Frame(self.__left_frame__, bg="white")
        self.__up_dialog_frame__.grid(row=0, column=0, padx=(10), pady=10, ipadx=(10), ipady=10, sticky = "n")
        # ---------------------------------- Image lbl
        self.__image_lbl__ = Label(self.__up_dialog_frame__, image=self.__mini_logo__, bg="white")
        self.__image_lbl__.grid(row=0, column=0, padx=(10), pady=10, sticky = "n")

        # ---------------------------------- UNIBA ft Regione Puglia label
        self.__ft_lbl__ = Label(self.__up_dialog_frame__, text="  Regione Puglia in collaborazione con UNIBA",
                                font=("Bahnschrift Light", 10), bg="white")
        self.__ft_lbl__.grid(row=1, column=0, sticky=N)

        # ------------------------------------------------------------------------------------------------- Buttons Frame
        self.__button_frame__ = Frame(self.__left_frame__, bg="white")
        self.__button_frame__.grid(row=1, column=0, padx=(10), pady=10, sticky = "n")



        # id btn selected
        self.__id_btn_selected__ = IntVar() #FIXME cancellami?
        self.__id_btn_selected__ = 0

        # color btn selected
        color_btn_selected = self.__get_color_btn__(self.__id_btn_selected__)
        color_btn_base = "white"

        # home button
        self.__home_btn__ = Button(self.__button_frame__, text=" "+u'\u2302' + "\tHome", font=("Bahnschrift Light", 12),
                                   height=2, width=40, borderwidth=0,
                                   background=color_btn_selected, cursor = "hand2", anchor = "w")

        # info button
        self.__info_btn__ = Button(self.__button_frame__, text="  "+u'\u2139' + "\tInformazioni",
                                   font=("Bahnschrift Light", 12), height=2, width=40,
                                   borderwidth=0, background=color_btn_base , cursor = "hand2", anchor = "w")

        # advanced button
        self.__advanced_btn__ = Button(self.__button_frame__, text=u'\u2699' + "\tAvanzate",
                                       font=("Bahnschrift Light", 12), height=2, width=40,
                                       borderwidth=0, background=color_btn_base , cursor = "hand2", anchor = "w")

        # agenda button
        self.__agenda_btn__ = Button(self.__button_frame__, text=u'\U0001F4D6' + "\tAgenda 2030",
                                     font=("Bahnschrift Light", 12), height=2, width=40,
                                     borderwidth=0, background=color_btn_base , cursor = "hand2", anchor = "w")

        # contact button
        self.__contact_btn__ = Button(self.__button_frame__, text=u'\U0001F465' + "\tContatti",
                                      font=("Bahnschrift Light", 12), height=2, width=40,
                                      borderwidth=0, background=color_btn_base , cursor = "hand2", anchor = "w")

        #set the command for each button #FIXME create function
        self.__home_btn__.configure(command=(lambda:self.__hide__(0)))
        self.__info_btn__.configure(command=(lambda:self.__hide__(1)))
        self.__advanced_btn__.configure(command=(lambda:self.__hide__(2)))
        self.__agenda_btn__.configure(command=(lambda:self.__hide__(3)))
        self.__contact_btn__.configure(command=(lambda:self.__hide__(4)))

        #positions each button #FIXME create function
        self.__home_btn__.grid(row=0, column=0, sticky=E + N)
        self.__info_btn__.grid(row=1, column=0, sticky=E + N)
        self.__advanced_btn__.grid(row=2, column=0, sticky=E + N)
        self.__agenda_btn__.grid(row=3, column=0, sticky=E + N)
        self.__contact_btn__.grid(row=4, column=0, sticky=E + N)

        #                                ---------------    Center Line Image    ---------------

        # vertical image
        self.__vertical_image__ = PhotoImage(file=__get_path__("utils\\images\\sdgline108x2000.png"))
        base_color = "white"

        # ----------------------------------------------------------------------------------- center line frame creation
        self.__line_frame__ = Frame(self.__master_frame__)
        self.__line_frame__.grid(column = 1, row = 0)
        self.__line_frame__.config(bg=base_color)
        self.__line_lbl__ = Label(self.__line_frame__, bg=base_color, image=self.__vertical_image__)
        self.__line_lbl__.grid()


        #                                ---------------    TOP RIGHT    ---------------

        id_color_right = "#FCFCFC"

        # ----------------------------------------------------------------------------------- Master right frame creation
        self.__right_frame__ = Frame(self.__master_frame__)  # , background = "#ab23ff")#, background= "#88cffa")#F6ECEC
        #self.__right_frame__.pack(expand=True, side=RIGHT, anchor="nw", padx=(10), pady=10, ipadx=(10), ipady=10)
        self.__right_frame__.grid(row = 0, column = 2, padx=(10), pady=10, ipadx=(10), ipady=10, sticky = "n")
        self.__right_frame__.config(bg=id_color_right)
        self.__right_frame__.rowconfigure(index=1, minsize=900, weight=1)

        # ------------------------------------------------------------------------------------- Principal Frame creation
        self.__principal_frame__ = Frame(self.__right_frame__, bg=id_color_right)
        self.__principal_frame__.grid(row=0, column=0, sticky=W, padx=(10), pady=5)

        # title label
        title = "Puglia Sostenibile"
        self.__title_lbl__ = Label(self.__principal_frame__, justify="left", text=title,
                                   font=("Bahnschrift SemiCondensed", 40, "bold"), bg=id_color_right)
        self.__title_lbl__.grid(row=0, column=0, sticky=W, padx=(10), pady=5)

        # mid title: Home, Info, Advanced, Contacts, etc. -------------------------------------------------------------- Mid Title

        self.__mid_title_lbl__ = Label(self.__principal_frame__, justify="left", text=self.__get_title_name__(0),
                                       font=("Bahnschrift SemiCondensed", 20, "bold"), bg=id_color_right)
        self.__mid_title_lbl__.grid(row=1, column=0, sticky=W, padx=(10), pady=5)

        # mid description: Description for Home, Info, Advanced, Contacts, etc.----------------------------------------- Mid Description
        self.__mid_descr_lbl__ = Label(self.__principal_frame__, justify="left", text=self.__get_description_frame__(0),
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__mid_descr_lbl__.grid(row=2, column=0, sticky=W, padx=(10), pady=5)


        # NOME DEL FILE!!!
        self.__file_name__ = StringVar()
        # GRAMMATURA!!!
        self.__ngram__ = IntVar()
        self.__ngram__ = 1
        # Computa Similarita' tra targets o sdgs!!!
        self.__sim_target__ = BooleanVar()
        self.__sim_target__ = False

        # ------------------------------------------- VARIABLE FRAMES -------------------------------------------------- VARIABLE FRAMES:

        #                                        ---------  HOME --------                                                               0.   HOME

        # ------------------------------------------------------------------------------------------ HOME Frame creation
        self.__home_frame__ = Frame(self.__principal_frame__, bg=id_color_right)


        # --------------------------------------------------------------------------------------- UP HOME Frame creation
        self.__home_up_frame__ = Frame(self.__home_frame__, bg=id_color_right)
        self.__home_up_frame__.grid(row=0, column=0)
        # ----------------------------------------------------------------------------------------- title Frame creation
        self.__title_frame__ = Frame(self.__home_up_frame__, bg = id_color_right)
        self.__title_frame__.grid(row=0, column=0, sticky=W)

        res_targ_text = "Ricerca Target" if self.__sim_target__ else "Ricerca SDGs"
        self.__ric_targets_lbl__ = Label(self.__title_frame__, justify="left", text=res_targ_text,
                                       font=("Bahnschrift SemiCondensed", 14, "bold"), bg=id_color_right)
        self.__ric_targets_lbl__.grid(row=0, column=0, sticky=W, padx = 5, pady=5)

        spec_sel_law_text = "Seleziona la legge e premi su 'Start'.\n\n" \
                            "Per consultare la lista di SDG e Target fai click sulla rotella."
        self.__sel_law_lbl__ = Label(self.__title_frame__, justify="left", text=spec_sel_law_text,
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__sel_law_lbl__.grid(row=1, column=1, sticky=N, padx = 5, pady=5)

        # SFOGLIAMI BTN

        sfogliami_img = PhotoImage(file=__get_path__("utils\\images\\button\\empty_square_70x72.png"))

        self.__sfogliami_btn__ = Button(self.__title_frame__, image = sfogliami_img,
                                   font=("Bahnschrift Light", 12), command=self.__consult_sdgs__,
                                   borderwidth=0.4, background=id_color_right , cursor = "hand2")
        self.__sfogliami_btn__.grid(row=1, column=0, sticky=N, padx = 5, pady=5)






        # label file name

        self.__adv_sel_lbl__ = Label(self.__home_up_frame__, justify="left", text="",
                                       font=("Bahnschrift Light", 10, "bold"), bg=id_color_right)
        self.__adv_sel_lbl__.grid(row=1, column=0, sticky=W, padx = 5, pady=5)

        # ------------------------------------------------------------------------------------COMPUTATION FRAME creation
        self.__computation_frame__ = Frame(self.__home_up_frame__, bg=id_color_right)
        self.__computation_frame__.grid(row=2, column=0, sticky=W)


        # ---------------------------------------------------------------------------- HOME BTN selection Frame creation
        self.__btn_select_frame__ = Frame(self.__computation_frame__, bg=id_color_right)
        self.__btn_select_frame__.grid(row=0, column=0, sticky=W, padx=(10), pady=10)


        # HOME BTN select file
        self.__select_btn__ = Button(self.__btn_select_frame__, text="Seleziona Legge",
                                   font=("Bahnschrift Light", 12), height=2, width=20, command=self.__select_file__,
                                   borderwidth=0.5, background="#F0F0F0" , cursor = "hand2")
        self.__select_btn__.grid(row=0, column=0, sticky=N, pady=5)

        # label file name

        self.__instr_sel_file__ = StringVar()
        self.__instr_sel_file__ = ""
        self.__sel_lbl__ = Label(self.__btn_select_frame__, justify="left", text=self.__instr_sel_file__,
                                       font=("Bahnschrift Light", 10), bg=id_color_right)
        self.__sel_lbl__.grid(row=1, column=0, sticky=N, pady=5)

        # start btn
        self.__start_btn__ = Button(self.__btn_select_frame__, text="Start",
                                       font=("Bahnschrift Light", 12), height=2, width=20, command=self.__start__,
                                       borderwidth=0.5, background="#F0F0F0", state = DISABLED)  # FIXME
        self.__start_btn__.grid(row=2, column=0, sticky=N, pady=5)

        # ----------------------------------------------------------------------------------- HOME Output Frame creation

        self.__output__ = StringVar()

        self.__output_frame__ = LabelFrame(self.__computation_frame__, width=100, height=10,padx=5,
                                           pady=5,font=("Bahnschrift Light",10),bg=id_color_right,text = " Output ")
        self.__output_frame__.grid(row=0, column = 1, padx = 10, pady=10)

        self.__root__.columnconfigure(0, weight=1)
        self.__root__.rowconfigure(1, weight=1)

        self.__output_frame__.rowconfigure(0, weight=1)
        self.__output_frame__.columnconfigure(0, weight=1)

        # Create the textbox widget
        self.__txt_box__ = Text(self.__output_frame__, width=100, height=10,
                                font=("Bahnschrift Light", 12), state = DISABLED, bg=id_color_right, cursor = "arrow")
        self.__txt_box__.grid(row=0, column=0, sticky=E + W + N + S)




        # ------------------------------------------------------------------------------------- DOWN HOME Frame creation
        self.__home_down_frame__ = Frame(self.__home_frame__, bg=id_color_right)
        self.__home_down_frame__.grid(row=1, column=0, sticky = W)


        # ------------------------------------------------------------------------------- Occurrences box frame creation
        occ_text = "Ricerca Occorrenze"
        self.__occ_text_lbl__ = Label(self.__home_down_frame__, justify="left", text=occ_text,
                                       font=("Bahnschrift SemiCondensed", 14, "bold"), bg=id_color_right)
        self.__occ_text_lbl__.grid(row=0, column=0, sticky=W, padx = 5, pady=5)

        expl_occ_text = "Inserisci una parola chiave e premi sul pulsante 'Cerca' per sapere quante volte compare nella Legge:"
        self.__expl_occ_lbl__ = Label(self.__home_down_frame__, justify="left", text=expl_occ_text,
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__expl_occ_lbl__.grid(row=1, column=0, sticky=W, padx = 5, pady=5)

        self.__keycatch_frame__ = LabelFrame(self.__home_down_frame__, width=28, height=2,padx=5, pady=5,
                                             font=("Bahnschrift Light",10),
                                             bg=id_color_right,text = " Inserisci la parola chiave ")
        self.__keycatch_frame__.grid(row=2, column = 0, padx = 10, pady=10, sticky = W)

        self.__root__.columnconfigure(0, weight=1)
        self.__root__.rowconfigure(1, weight=1)

        self.__keycatch_frame__.rowconfigure(0, weight=1)
        self.__keycatch_frame__.columnconfigure(0, weight=1)

        # Create the textbox widget
        self.__insert_key__ = Text(self.__keycatch_frame__, width=28, height=1,
                                   font=("Bahnschrift Light", 10), bg="white",
                                   state = DISABLED
                                   )
        self.__insert_key__.grid(row=0, column=0, sticky=W)

        self.__insert_key__.bind('<Return>', lambda _: self.__cerca_occorrenze__())

        # cerca btn
        self.__cerca_btn__ = Button(self.__keycatch_frame__, text="Cerca",
                                       font=("Bahnschrift Light", 12), height=1, width=10, command=self.__cerca_occorrenze__,
                                       borderwidth=0.5, background="#F0F0F0", state = DISABLED)
        self.__cerca_btn__.grid(row=0, column=1, sticky=N, pady=10, padx=10)

        self.__key_occ__ = StringVar()
        self.__key_occ__ = ""

        self.__ky_occ_res_label__ = Label(self.__home_down_frame__, justify="left", text=self.__key_occ__,
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__ky_occ_res_label__.grid(row=3, column=0, sticky=W, padx = 5, pady=5)

        #                                        ---------  Informazioni --------                                                       1.   Informazioni

        # ---------------------------------------------------------------------------------- INFORMAZIONI Frame creation
        self.__info_frame__ = Frame(self.__principal_frame__, bg=id_color_right)


        #                                        ---------  AVANZATE --------                                                           2.   Avanzate

        # -------------------------------------------------------------------------------------- AVANZATE Frame creation
        self.__adv_frame__ = Frame(self.__principal_frame__, bg=id_color_right)

        self.__grammatura_lbl__ = Label(self.__adv_frame__,justify="left", text="Grammatura",
                                       font=("Bahnschrift SemiCondensed", 14, "bold"), bg=id_color_right)
        self.__grammatura_lbl__.grid(row=0, column=0, sticky=W, padx = 5, pady=5)

        self.__grammatura_expl_lbl__ = Label(self.__adv_frame__, justify="left", text="Clicca sulla Grammatura che preferisci:",
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__grammatura_expl_lbl__.grid(row=1, column=0, sticky=W, padx = 5, pady=5)

        Radiobutton(self.__adv_frame__,
                       text="Bigram",
                       padx=20,
                       variable=self.__ngram__, font=("Bahnschrift Light", 12),
                       value=2, bg=id_color_right,
                    command=(lambda:self.__set_ngram_value__(2))
                    ).grid(row=2, column=1, sticky=E)

        Radiobutton(self.__adv_frame__,
                       text="Unigram",
                       padx=20,
                       variable=self.__ngram__, font=("Bahnschrift Light", 12),
                       value=1, bg=id_color_right,
                    command=(lambda:self.__set_ngram_value__(1))
                    ).grid(row=2, column=0, sticky=W)


        self.__choose_t_sdg_lbl__ = Label(self.__adv_frame__,justify="left", text="Rileva SDG o Target",
                                       font=("Bahnschrift SemiCondensed", 14, "bold"), bg=id_color_right)
        self.__choose_t_sdg_lbl__.grid(row=3, column=0, sticky=W, padx = 5, pady=5)

        self.__choose_t_sdg_expl_lbl__ = Label(self.__adv_frame__, justify="left", text="Scegli tra SDG e Target:",
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__choose_t_sdg_expl_lbl__.grid(row=4, column=0, sticky=W, padx = 5, pady=5)

        Radiobutton(self.__adv_frame__,
                       text="Target",
                       padx=20,
                       variable=self.__sim_target__, font=("Bahnschrift Light", 12),
                       value=True, bg=id_color_right,
                    command=(lambda:self.__set_sel_t_sdg_value__(True))
                    ).grid(row=5, column=1, sticky=E)

        Radiobutton(self.__adv_frame__,
                       text="SDG",
                       padx=20,
                       variable=self.__sim_target__, font=("Bahnschrift Light", 12),
                       value=False, bg=id_color_right,
                    command=(lambda:self.__set_sel_t_sdg_value__(False))
                    ).grid(row=5, column=0, sticky=W)




        #                                        ---------  AGENDA 2030 --------                                                        3.   Agenda 2030

        # ----------------------------------------------------------------------------------- AGENDA 2030 Frame creation
        self.__agenda_frame__ = Frame(self.__principal_frame__, bg=id_color_right)

        # creating object of ShowPdf from tkPDFViewer.
        pdf_viewer= pdf.ShowPdf()

        agenda_directory = __get_path__("Agenda2030\\Agenda-2030-Onu-italia.pdf")


        #Clear the image list to ignore deprecation warning
        pdf_viewer.img_object_li.clear()

        # Adding pdf location and width and height.
        self.__show_agenda__ = pdf_viewer.pdf_view(self.__agenda_frame__,
                         pdf_location=agenda_directory,
                         width=80, height=43)

        # Placing Pdf in my gui.
        self.__show_agenda__.pack()


        #                                        ---------  CONTATTI --------                                                           4.   CONTATTI

        # -------------------------------------------------------------------------------------- CONTATTI Frame creation
        self.__contact_frame__ = Frame(self.__principal_frame__, bg=id_color_right)








        #grid the home_fram ONLY. The other Variable Frame will be gridded when needed
        self.__home_frame__.grid(row=3, column=0, sticky=W, padx=(10), pady=10)
        # defines min and max root dimension
        self.__root__.update()
        self.__root__.minsize(self.__root__.winfo_width(), self.__root__.winfo_height())

        self.__root__.mainloop()

    def __grid_variable_frames__(self):
        """
        Places each variable frame into the right master frame
        :return:
        """

        for frame in self.__get_variable_frame_list__():
            frame.grid(row=3, column=0, sticky=W, padx=(10), pady=10)

    def __forget_grid_variable_frames__(self):
        """
        Removes each variable frame from the right master frame
        :return:
        """

        for frame in self.__get_variable_frame_list__():
            frame.grid_forget()


    def __set_ngram_value__(self, value):
        """
        Changes the ngram based on the user choice
        :return:
        """

        self.__ngram__ = value


    def __set_sel_t_sdg_value__(self, value):
        """
        Changes the sdg or target choice based on the user choice
        :return:
        """
        self.__sim_target__ = value
        self.__ric_targets_lbl__.configure(text = "Ricerca Target" if self.__sim_target__ else "Ricerca SDGs")

    def __select_file__(self):
        """
        Let the user select a file. The file type must be one of the allowed ones (see self.__filetypes__ function).
        Enables and disables start button.
        :return:
        """

        self.__file_name__ = fd.askopenfilename(
            title="Select File",
            initialdir="\\",
            filetypes=self.__filetypes__()
        )

        # Enables and disables start button
        self.__start_btn__.configure(state=NORMAL if not self.__file_name__ == "" else DISABLED)
        file_name = path.basename(self.__file_name__)
        # specify doc selected
        doc_select_rd_txt = "Premi 'Start' per continuare"
        self.__sel_lbl__.config(text=doc_select_rd_txt if not file_name == "" else "Premi su 'Seleziona Legge'")
        self.__start_btn__.config(cursor="hand2" if not file_name == "" else "arrow")
        self.__adv_sel_lbl__.config(text="É stato selezionato il file '"+file_name+"'." if not file_name == '' else "")
        self.__insert_key__.delete("1.0", END)
        self.__insert_key__.configure(state="disabled")
        self.__cerca_btn__.configure(state="disabled")
        self.__cerca_btn__.configure(cursor="arrow")
        self.__key_occ__ = ""
        self.__ky_occ_res_label__.configure(text=self.__key_occ__)

    def __popup_sdgs__(self):
        """
        Lets pop up a new window with the SDGs list
        :return:
        """
        dest_sdgs = __get_path__("SDGs\\SDGs.txt")
        with open(dest_sdgs,"r",encoding='utf-8', errors='ignore') as f:
            contents = f.readlines()
        content=""
        for l in contents:
            content += l + "\n"

        pad = 3
        id_color_right = "#FCFCFC"
        popupwindow = Tk()
        popupwindow.configure(bg=id_color_right)
        popupwindow.wm_title("Obiettivi di Sviluppo Sostenibile: SDGs")
        master_frame = Frame(popupwindow, bg=id_color_right)
        master_frame.grid(row=0, column = 0, padx = 10, pady=10)

        # title label
        title = "Obiettivi di Sviluppo Sostenibile:"
        title_lbl__ = Label(master_frame, justify="left", text=title,
                                   font=("Bahnschrift SemiCondensed", 40, "bold"), bg=id_color_right)
        title_lbl__.grid(row=0, column=0, sticky=W, padx=(10), pady=10)

        # ---------------------------------------------------- TEXTBOX Frame
        box_frame = LabelFrame(master_frame, text=" Lista di SDGs: ", padx=5, pady=5,bg=id_color_right, width=popupwindow.winfo_width()-pad)
        box_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E + W + N + S)

        popupwindow.columnconfigure(0, weight=1)
        popupwindow.rowconfigure(1, weight=1)

        box_frame.rowconfigure(0, weight=1)
        box_frame.columnconfigure(0, weight=1)

        # Create the textbox widget
        txt_box = scrolledtext.ScrolledText(box_frame, bg=id_color_right, width=popupwindow.winfo_width()-pad)
        txt_box.grid(row=0, column=0, sticky=E + W + N + S)

        txt_box.insert(INSERT, content)
        txt_box.configure(state="disabled")

        close_btn = ttk.Button(master_frame, text="Close", command=popupwindow.destroy)

        close_btn.grid(row=2, sticky=E, padx=(10), pady=10)

        popupwindow.update()
        popupwindow.minsize(popupwindow.winfo_width(), popupwindow.winfo_height())

        popupwindow.maxsize(popupwindow.winfo_width(), popupwindow.winfo_height())

    def __consult_sdgs__(self):
        """
        If the sfogliami_btn is pressed it will pop up a page with the SDG list.
        :return:
        """
        self.__popup_sdgs__()



    def __start__(self):
        """
        Enables and disables the occurrences box and computes the output.
        :return:
        """
        self.__txt_box__.configure(state=NORMAL)
        self.__txt_box__.delete("1.0", END)
        self.__txt_box__.configure(state="disabled")
        self.__key_occ__ = ""
        if not self.__file_name__ == "":
            dest = self.__file_name__
            warning = False
            try:
                output = get_relevant(path_law=self.__file_name__, ngram=self.__ngram__, sim_target=self.__sim_target__)
            except ValueError:
                messagebox.showwarning("Warning", "Il file selezionato potrebbe essere protetto da password.\nPer favore, seleziona un altro file.")
                warning = True
            except OSError:
                messagebox.showwarning("Warning", "Il file risulta essere vuoto\noppure è composto da sole immagini.\nPer favore, seleziona un altro file.")
                warning = True
            except IOError:
                messagebox.showwarning("Warning", "Impossibile processare il file per uno dei seguenti motivi:"
                                                    "\n-\til file è vuoto;"
                                                    "\n-\til file contiene solo immagini;"
                                                    "\n-\til file è corrotto."
                                                  "\n\nPer favore, seleziona un altro file.")
                warning = True
            # get file name from path
            file_name = path.basename(dest)
            if warning:
                pass
            else:
                # get string containing the output
                self.__output__ = "I primi tre"
                self.__output__ += (" SDG " if not self.__sim_target__ else " Target ")
                self.__output__ += "più similari alla legge " + file_name + " sono:\n\n" + output + " \n\nPer favore seleziona un'altra Legge per una nuova computazione."
                self.__txt_box__.configure(state=NORMAL)
                self.__txt_box__.insert(INSERT, self.__output__)
                self.__txt_box__.configure(state="disabled")
                self.__insert_key__.configure(state="normal")
                self.__cerca_btn__.configure(state="normal")
                self.__cerca_btn__.configure(cursor="hand2")

        self.__start_btn__.configure(state="disabled")

    def __cerca_occorrenze__(self):
        """
        Returns the number of times a certain pattern appears in the law
        """
        #I extract the content of the law
        law = extract_content(self.__file_name__)
        #I remove symbols
        law = sub(r'[^\w]', ' ', law)
        #I remove unnecessary new line symbs
        law = sub(r"(?<!\\)\\n|\n", " ", law)
        #I lowercase the content
        law = law.lower()
        # I remove trailing spaces
        law = " ".join(law.split())
        pattern = str(self.__insert_key__.get("1.0", "end-1c")).lower()
        pattern = sub(r"(?<!\\)\\n|\n", " ", pattern)
        pattern = " ".join(pattern.split())
        #I count occurrences
        occ = law.count(pattern)
        self.__key_occ__ = "La parola chiave '" + pattern + "' appare " + str(occ) + " volte in " + path.basename(self.__file_name__)
        self.__ky_occ_res_label__.configure(text=self.__key_occ__)
        self.__insert_key__.delete("1.0", END)

    def __get_variable_frame_list__(self):
        """
        Returns the list of the variables Frames
            0 = home
            1 = info
            2 = advanced
            3 = agenda 2030
            4 = contact
        :return: list of Frame
            list of the variable Frames
        """
        return [self.__home_frame__, self.__info_frame__,
                self.__adv_frame__, self.__agenda_frame__,
                self.__contact_frame__]


    def __get_color_btn__(self, id):
        """
        Returns the color of the selected btn
        :param id: integer
            id of the btn:
                0 = home: green
                1 = info: yellow
                2 = advanced: red
                3 = agenda 2030: lilla
                4 = contact: blu
        :return: string
            the color of the selected btn
        """
        colors = {
            0: "#DAF7A6",
            1: "#F6F7A6",
            2: "#F7A6A6",
            3: "#E0A6F7",
            4: "#A6C7F7"
        }
        color = colors[id]
        return color

    def __get_title_name__(self, id):
        """
        Returns the name of the selected frame
        :param id: integer
            id of the btn:
                0 = Home
                1 = Informazioni
                2 = Avanzate
                3 = Agenda 2030
                4 = Contatti
        :return: string
            the name of the selected frame
        """
        names = {
            0: "Home",
            1: "Informazioni",
            2: "Avanzate",
            3: "Agenda 2030",
            4: "Contatti"
        }
        name = names[id]
        return name

    def __get_description_frame__(self, id):
        """
        Returns the description of the selected frame
        :param id: integer
            id of the btn:
                0 = Home
                1 = Informazioni
                2 = Avanzate
                3 = Agenda 2030
                4 = Contatti
        :return: string
            the description of the selected frame
        """
        frame_description = {
            0: "Questa sezione è dedicata all'utilizzo di Puglia Sostenibile.\n"
                "Il software ti permette di scoprire in modo "
                "semplice ed intuitivo quali tra i vari target e goal, appartenenti all'Agenda 2030,"
                " siano i più rilevanti per la legge da te selezionata. \nPuglia Sostenibile ti restituirà"
                " i tre target/goal che più verosimilmente trattano quest'ultima. "
                "\nUtilizzare Puglia Sostenibile è molto semplice!\n"
                "Ti basta selezionare il file contenente la legge che vorresti analizzare per poi spingere sul pulsante"
                " 'Start'. Mi raccomando, il file deve necessariamente essere uno tra \ni seguenti formati: '.pdf', '.docx' o '.txt'.\n"
                "Puoi anche effettuare una ricerca manuale per capire se una parola chiave sia inclusa, o meno, all'interno del"
                " contenuto della legge. \nDevi soltanto digitare la keyword nell'apposita box ed il programma ti restituirà, dopo"
                " aver premuto il pulsante 'Cerca', il numero di volte che compare nel testo.\n\n"
                "Come vedi, niente di più semplice!",
            1: "Questa sezione è dedicata alla storia dell'Agenda 2030 e di Puglia Sostenibile.\n"
               "Se sei curioso di conoscere com'è nato questo progetto, prosegui nella lettura.",
            2: "In questa sezione potrai mettere mano alle impostazioni avanzate di Puglia Sostenibile, cambiando le"
               " seguenti proprietà:"
               "\n-\tGrammatura;"
               "\n-\tRileva SDG o Target.\n\n"
               "Prima di andare avanti, è bene forniti delle informazioni preliminari.\n"
               "Devi sapere che Puglia Sostenibile, per il momento, effettua la computazione di similarità"
               " tra il documento da te caricato (la Legge) ed \ni vari Obiettivi di Sviluppo Sostenibile (SDGs),"
               " dell'Agenda 2030, per mezzo della Similarità del Coseno.\n"
               "La matrice TFIDF, propedeutica a questo calcolo, suddivide ogni documento"
               " in una serie di parole chiave (keyphrase).\n\nUn esempio di keyphrase è 'Emancipazione' oppure 'Femminile'.\n\n"
               "Si è dato modo all'utente di cambiare la Grammatura, ossia il numero di parole da cui è composta ogni parola chiave, "
               "facendoti scegliere \ntra una computazione Unigram ed una computazione Bigram.\n"
               "\nNella computazione Unigram ogni keyphrase è composta da una singola parola (DEFAULT).\n"
               "\nNella computazione Bigram ogni keyphrase è composta da una o due parole:\n"
               "esempi di keyphrase Bigram sono 'Emancipazione Femminile', 'Paternariato', 'Povertà assoulta', etc.\n\n"
               "Come già specificato, di Default il sofware effettua computazioni Unigram, ma tu hai la possibilità di "
               "cambiare questa proprietà.\nFai attenzione, però, nel caso di grammatura Bigram la computazione risulterà più"
               " precisa ma allo stesso tempo più selettiva.\n\nPuoi, inoltre, selezionare il tipo di output da computare "
               "decidendo tra il visualizzare gli SDGs più similari alla legge (es. SDG 5, SDG 3, SDG 15, etc.)\n"
               "ed il visualizzare, nello specifico, i Target più rilevanti (es. Target 5.5, Target 3.1, Target 15.c, etc.).\nPer farlo, ti basta modificare "
               "l'apposita impostazione.\n\nOra tocca a te!",
            3: "In questa sezione puoi consultare l'Agenda 2030.\n\n"
               "Per maggiori informazioni, consultare il sito https://unric.org/it/agenda-2030/ .",
            4: "In questa sezione trovi tutti i contatti necessari per inviare feedback, chiedere informazioni e"
               " comunicare qualsiasi tipo di problema dovessi riscontrare con il programma."
        }
        description = frame_description[id]
        return description

    def __filetypes__(self):
        """
        Returns all of the filetypes allowed
        :return:
        tuple of all of the filetypes allowed
        """
        filetypes = (
            ("*.pdf", "*.pdf"),
            ("*.txt", "*.txt"),
            ("*.docx", "*.docx")
        )
        return filetypes

    def __set_ico__(self):
        """
        Sets the icon of the installation root
        :return:
        """
        self.__root__.iconbitmap(self.__ico__)
        self.__root__.wm_iconphoto(True, self.__logo__)

    def __set_title__(self, title):
        """
        Sets installation root title
        :param title: string which contains installation root title
        :return:
        """
        self.__root__.title(title)

    def __get_btns__(self):
        """
        returns a list containing each of the following buttons:
        -home
        -info
        -advanced
        -agenda
        -contact

        :return: list of buttons
        """

        return [self.__home_btn__, self.__info_btn__, self.__advanced_btn__, self.__agenda_btn__, self.__contact_btn__]

    def __hide__(self, id):
        """
        Shows the variable frame selected (id-th Frame) and hides the others.
        Manages the buttons color based on the selection.
        Changes Title and Description.

        :param id: integer
            id of the pressed button
        :return:
        """
        self.__id_btn_selected__ = id

        #show the desired frame while hiding the others
        frame_list = self.__get_variable_frame_list__()

        self.__forget_grid_variable_frames__()
        frame_list[id].grid(row=3, column=0, sticky=W, padx=(10), pady=10)


        #change buttons color
        btn_list = self.__get_btns__()
        #     puts each button white
        for btn in btn_list:
            btn.configure(background="white")
        #     gives the selected button the right color
        btn_list[id].configure(background=self.__get_color_btn__(id))

        # set the Mid Title Name
        self.__mid_title_lbl__.configure(text= self.__get_title_name__(id))

        #set the Mid Description
        self.__mid_descr_lbl__.configure(text = self.__get_description_frame__(id))






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


if __name__ == '__main__':
    termination = False
    try:
        from Compute_Similarity import get_relevant
        from FileHandler import ask_path, extract_content
        from tkPDFViewer import tkPDFViewer as pdf
        from re import sub
        termination = True
    except ModuleNotFoundError:
        install = Installation()
        termination = install.get_terimantion()

    if termination:
        app = App()
