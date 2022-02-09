# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:39:51 2022
Manages the GUI of the program.
@author: ClaudiaLorusso
"""

from tkinter import *
from tkinter import ttk, scrolledtext, messagebox
from tkinter import filedialog as fd
import sys
from os import path


class Installation:
    """
    Manages the installation GUI.
    If it is the first execution OR the user doesn't dispose of the needed libs
    the program asks him if he wants to download them, in which case the software proceeds
    with the installation. Else, he can easily close the window.
    """

    def __init__(self):

        # ------------------------------- Termination variable. Default = False; if True, wont open App.
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

    def get_termination(self):
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
        from tkPDFViewer import tkPDFViewer
        self.__progress__["value"] = 60
        self.__installation_root__.update_idletasks()
        from Compute_Similarity import get_relevant
        self.__progress__["value"] = 76
        self.__installation_root__.update_idletasks()
        from FileHandler import ask_path, extract_content
        self.__progress__["value"] = 87
        self.__installation_root__.update_idletasks()
        import json
        self.__progress__["value"] = 90
        self.__installation_root__.update_idletasks()
        from glob import glob
        self.__progress__["value"] = 98
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
        self.__progress__["value"] = 100
        self.__installation_root__.update_idletasks()
        self.__termination__ = True
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
    The GUI is divided into three main vertical Frames, inserted into a __master_frame__:
        - __left_frame__ (0,0):
                contains the logo ( into __up_dialog_frame__ (0, 0)) and the
                buttons ( into __button_frame__ (1, 0)).
                Each button manages the selection of the desired Variable Frame.
                There's also another button which is separated from the others: sfoglia_btn.
                It will open a window in which the user can easily browse all of the SDGs (in Italian).
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
                    -   __info_frame__ :    Shows the user some information about the Agenda, the program and the logo.
                    -   __adv_frame__ :     Enables the user to change the Grammature from Unigram to Bigram and
                                            vice-versa.
                    -   __agenda_frame__ :  Permits the user to consult the pdf of the Agenda 2030.
                    -   __contact_frame__ : Shows the user the technical contacts.

    """

    def __init__(self):
        from tkPDFViewer import tkPDFViewer

        # ------- display adaptation

        """
        import ctypes

        # Query DPI Awareness (Windows 10 and 8)
        awareness = ctypes.c_int()
        errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        print(awareness.value)

        # Set DPI Awareness  (Windows 10 and 8)
        errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        # the argument is the awareness level, which can be 0, 1 or 2:
        # for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)

        # Set DPI Awareness  (Windows 7 and Vista)
        success = ctypes.windll.user32.SetProcessDPIAware()
        # behaviour on later OSes is undefined, although when I run it on my Windows 10 machine, it seems to work with effects identical to SetProcessDpiAwareness(1)
        """

        """     
        import ctypes
        try:  # Windows 8.1 and later
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception as e:
            pass
        try:  # Before Windows 8.1
            ctypes.windll.user32.SetProcessDPIAware()
        except:  # Windows 8 or before
            pass
        """
        import ctypes

        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        # ------------------------------- Installation root creation
        self.__root__ = Tk()

        self.__root__.update()

        width = self.__root__.winfo_screenwidth()

        if width<1680:
            self.__root__.tk.call("tk", "scaling", 1)
        if width>2000:
            self.__root__.tk.call("tk", "scaling", 1.5)
        self.__root__.update()

        # Maximises screen but not full
        pad = 3
        self.__root__.geometry("{0}x{1}+0+0".format(
            self.__root__.winfo_screenwidth() - pad, self.__root__.winfo_screenheight() - pad))

        # -----set root to full screen

        self.__root__.state("zoomed")
        self.__root__.update()
        """
        #WIDE FULL SCREEN: erases tool and top bar BUT if you press on the escape
        #button it will show everything
        self.__root__.attributes("-fullscreen", True)
        self.fullScreenState = False
        self.__root__.bind("<F11>", self.__toggleFullScreen__)
        self.__root__.bind("<Escape>", self.__quitFullScreen__)
        """

        self.__root__.configure(background="white")

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
        self.__master_frame__.pack(side=LEFT, anchor="ne", padx=(10), pady=10)
        self.__master_frame__.config(bg='white')


        #                            ---------------    TOP LEFT    ---------------

        # --------------------------------------------------------------- Left frame creation (where the magic happens)
        self.__left_frame__ = Frame(self.__master_frame__)
        self.__left_frame__.grid(row = 0, column = 0, padx=(10), pady=10, sticky = "nw")
        self.__left_frame__.config(bg='white')

        # -------------------------------------------------------------------------------------- UP Dialog Frame creation
        self.__up_dialog_frame__ = Frame(self.__left_frame__, bg="white")
        self.__up_dialog_frame__.grid(row=0, column=0, padx=(10), pady=10, sticky = "n")
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

        color_btn_base = "white"

        # home button
        self.__home_btn__ = Button(self.__button_frame__, text=" "+u'\u2302' + "\tHome", font=("Bahnschrift Light", 12),
                                   height=2, width=40, borderwidth=0,
                                   background=color_btn_base, cursor = "hand2", anchor = "w")

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

        #set the command for each button
        self.__home_btn__.configure(command=(lambda:self.__hide__(0)))
        self.__info_btn__.configure(command=(lambda:self.__hide__(1)))
        self.__advanced_btn__.configure(command=(lambda:self.__hide__(2)))
        self.__agenda_btn__.configure(command=(lambda:self.__hide__(3)))
        self.__contact_btn__.configure(command=(lambda:self.__hide__(4)))

        #positions each button
        self.__home_btn__.grid(row=0, column=0, sticky=W + N)
        self.__info_btn__.grid(row=1, column=0, sticky=W + N)
        self.__advanced_btn__.grid(row=2, column=0, sticky=W + N)
        self.__agenda_btn__.grid(row=3, column=0, sticky=W + N)
        self.__contact_btn__.grid(row=4, column=0, sticky=W + N)


        # --------------------------------------------------------------------------------------------------------------SFOGLIAMI BTN
        """
        self.__sfoglia_frame__ = Frame(self.__button_frame__)
        self.__sfoglia_frame__.grid(row=5, sticky=S + E)
        """

        self.__sfogliami_btn__ = Button(self.__button_frame__, text = "Sfoglia gli SDGs", justify="center",
                                   font=("Bahnschrift SemiCondensed", 14, "bold"), command=self.__consult_sdgs__, height=2, width=40,
                                      borderwidth=0, background="#F0F0F0" , cursor = "hand2")
        self.__sfogliami_btn__.grid(row=5,column=0, sticky=W + N)#pack(anchor="s")





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

        #------------------------------------------------------------------------------------- Welcome Frame (only once)
        id_color_right = "#FCFCFC"

        self.__welcome_frame__ = Frame(self.__master_frame__)
        self.__welcome_frame__.grid(row = 0, column = 2, sticky = "ne")
        self.__welcome_frame__.config(bg=id_color_right)
        welcome_image = PhotoImage(file = __get_path__("utils\\images\\welcome_new.png" if self.__root__.winfo_screenwidth()>=1680 else "utils\\images\\welcome_new_min.png"))
        self.__welcome_lbl__ = Label(self.__welcome_frame__, bg = id_color_right, image = welcome_image)



        self.__welcome_lbl__.pack()


        # ----------------------------------------------------------------------------------- Master right frame creation
        self.__right_frame__ = Frame(self.__master_frame__)
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
        self.__ngram__.set(1)
        # Computa Similarita' tra targets o sdgs!!!
        self.__sim_target__ = BooleanVar()
        self.__sim_target__.set(False)

        # ------------------------------------------- VARIABLE FRAMES -------------------------------------------------- VARIABLE FRAMES:

        #                                        ---------  HOME --------                                                               0.   HOME

        # ------------------------------------------------------------------------------------------ HOME Frame creation
        self.__home_frame__ = Frame(self.__principal_frame__, bg=id_color_right, width = self.__root__.winfo_screenwidth())

        height = self.__root__.winfo_screenheight()
        if height<=720:
            self.__home_scroll_frame__ = ScrollableFrame(self.__home_frame__, bg=id_color_right, width = self.__root__.winfo_screenwidth())
            fr_home = self.__home_scroll_frame__.scrollable_frame
        else:
            self.__home_scroll_frame__ = Frame(self.__home_frame__, bg=id_color_right,
                                                         width=self.__root__.winfo_screenheight() - 100)
            fr_home = self.__home_scroll_frame__
        # --------------------------------------------------------------------------------------- UP HOME Frame creation
        self.__home_up_frame__ = Frame(fr_home, bg=id_color_right)
        self.__home_up_frame__.grid(row=0, column=0)
        # ----------------------------------------------------------------------------------------- title Frame creation
        self.__title_frame__ = Frame(self.__home_up_frame__, bg = id_color_right)
        self.__title_frame__.grid(row=0, column=0, sticky=W)

        res_targ_text = "Ricerca Target" if self.__sim_target__.get() else "Ricerca SDGs"
        self.__ric_targets_lbl__ = Label(self.__title_frame__, justify="left", text=res_targ_text,
                                       font=("Bahnschrift SemiCondensed", 14, "bold"), bg=id_color_right)
        self.__ric_targets_lbl__.grid(row=0, column=0, sticky=W, padx = 5)

        spec_sel_law_text = "Seleziona la legge e premi su 'Start'."
        self.__sel_law_lbl__ = Label(self.__title_frame__, justify="left", text=spec_sel_law_text,
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__sel_law_lbl__.grid(row=1, column=0, sticky=N, padx = 5)



        # label file name

        self.__adv_sel_lbl__ = Label(self.__home_up_frame__, justify="left", text="",
                                       font=("Bahnschrift Light", 10, "bold"), bg=id_color_right)
        self.__adv_sel_lbl__.grid(row=1, column=0, sticky=W, padx = 5)

        # ------------------------------------------------------------------------------------COMPUTATION FRAME creation
        computation_color = id_color_right

        self.__computation_frame__ = Frame(self.__home_up_frame__, bg=computation_color)
        self.__computation_frame__.grid(row=2, column=0, sticky=W)


        # ---------------------------------------------------------------------------- HOME BTN selection Frame creation
        self.__btn_select_frame__ = Frame(self.__computation_frame__, bg=computation_color)
        self.__btn_select_frame__.grid(row=0, column=0, sticky=W)


        # HOME BTN select file
        self.__select_btn__ = Button(self.__btn_select_frame__, text="Seleziona Legge",
                                   font=("Bahnschrift SemiCondensed", 12, "bold"), height=2, width=20, command=self.__select_file__,
                                   borderwidth=0.0, background="#F0F0F0" , cursor = "hand2")
        self.__select_btn__.grid(row=0, column=0, sticky=N, pady=5)

        # label file name

        self.__instr_sel_file__ = StringVar()
        self.__instr_sel_file__ = ""
        self.__sel_lbl__ = Label(self.__btn_select_frame__, justify="left", text=self.__instr_sel_file__,
                                       font=("Bahnschrift Light", 10), bg=computation_color)
        self.__sel_lbl__.grid(row=1, column=0, sticky=N, pady=5)

        # start btn
        self.__start_btn__ = Button(self.__btn_select_frame__, text="Start",
                                       font=("Bahnschrift SemiCondensed", 12, "bold"), height=2, width=20, command=self.__start__,
                                       borderwidth=0.0, background="#F0F0F0", state = DISABLED)
        self.__start_btn__.grid(row=2, column=0, sticky=N, pady=5)

        # ----------------------------------------------------------------------------------- HOME Output Frame creation

        self.__output__ = StringVar()

        self.__output_frame__ = LabelFrame(self.__computation_frame__, width=100, height=10,padx=5, borderwidth=0.4,
                                           pady=5,font=("Bahnschrift SemiCondensed",10), bg=computation_color,text = "  Output ")
        self.__output_frame__.grid(row=0, column = 1, padx = 10)

        self.__root__.columnconfigure(0, weight=1)
        self.__root__.rowconfigure(1, weight=1)

        self.__output_frame__.rowconfigure(0, weight=1)
        self.__output_frame__.columnconfigure(0, weight=1)

        # Create the textbox widget
        self.__txt_box__ = Text(self.__output_frame__, width=80, height=9,
                                font=("Bahnschrift Light", 12), state = DISABLED, bg="white", cursor = "arrow")
        self.__txt_box__.grid(row=0, column=0, sticky=E + W + N + S)




        # ------------------------------------------------------------------------------------- DOWN HOME Frame creation
        self.__home_down_frame__ = Frame(fr_home, bg=id_color_right)
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

        self.__keycatch_frame__ = LabelFrame(self.__home_down_frame__, width=28, height=2,
                                             padx=5, pady=5, borderwidth = 0.4,
                                             font = ("Bahnschrift SemiCondensed", 10),
                                             bg=id_color_right)
        self.__keycatch_frame__.grid(row=2, column = 0, padx = 10 if self.__root__.winfo_screenheight()>768 else 2, pady=10 if self.__root__.winfo_screenheight()>768 else 2, sticky = W)

        self.__root__.columnconfigure(0, weight=1)
        self.__root__.rowconfigure(1, weight=1)

        self.__keycatch_frame__.rowconfigure(0, weight=1)
        self.__keycatch_frame__.columnconfigure(0, weight=1)



        # Create the textbox widget
        self.__insert_key__ = Text(self.__keycatch_frame__, width=28, height=1,
                                   font=("Bahnschrift Light", 10), bg="white",
                                   state = DISABLED, cursor = "arrow"
                                   )
        self.__insert_key__.grid(row=0, column=0, sticky=W)

        self.__insert_key__.bind('<Return>', lambda _: self.__cerca_occorrenze__())
        self.__keycatch_frame__.configure(text = "  Inserisci la parola chiave " if (str(self.__insert_key__["state"])== "normal") else "  Seleziona una nuova Legge ed inserisci la parola chiave ")

        # cerca btn
        self.__cerca_btn__ = Button(self.__keycatch_frame__, text="Cerca",
                                       font=("Bahnschrift SemiCondensed", 12), height=1, width=10, command=self.__cerca_occorrenze__,
                                       borderwidth=0.0, background="#F0F0F0", state = DISABLED)
        self.__cerca_btn__.grid(row=0, column=1, sticky=N, pady= 0 if self.__root__.winfo_screenheight()<=768 else 10, padx=10 if self.__root__.winfo_screenheight()<=768 else 10)

        self.__key_occ__ = StringVar()
        self.__key_occ__ = ""

        self.__ky_occ_res_label__ = Label(self.__home_down_frame__, justify="left", text=self.__key_occ__,
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__ky_occ_res_label__.grid(row=3, column=0, sticky=W, padx = 0 if self.__root__.winfo_screenheight()<=768 else 5, pady=0 if self.__root__.winfo_screenheight()<=768 else 5)

        self.__root__.update()
        width = self.__root__.winfo_screenwidth()
        if width<1920:
            Label(self.__home_down_frame__, justify="left", text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
                                              font=("Bahnschrift Light", 12), bg=id_color_right).grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.__home_scroll_frame__.pack()

        #                                        ---------  Informazioni --------                                                       1.   Informazioni

        # ---------------------------------------------------------------------------------- INFORMAZIONI Frame creation
        self.__info_frame__ = Frame(self.__principal_frame__, bg=id_color_right, width=1200 if self.__root__.winfo_screenwidth()>=2000 else 810 if self.__root__.winfo_screenwidth()>=1600 else 600, height=800)

        self.__scrollableframe__ = ScrollableFrame(self.__info_frame__, bg=id_color_right, width=1200 if self.__root__.winfo_screenwidth()>=2000 else 810 if self.__root__.winfo_screenwidth()>=1600 else 600, height=800)

        # new line label \n
        Label(self.__scrollableframe__.scrollable_frame, bg=id_color_right, justify= "center", text = "\n"
                                                      ).grid(row=0, column = 0, sticky = "n")

        image_puglia_sostenibile = PhotoImage(file=__get_path__("utils\\images\\COLORPugliaSostenibile450x415.png" if self.__root__.winfo_screenwidth()>=1600 else "utils\\images\\COLORPugliaSostenibile450x415.png"))
        self.__lbl_image_puglia_sostenibile__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      image = image_puglia_sostenibile,
                                                      bg=id_color_right, justify= "center"
                                                      ).grid(row=1, column = 0, sticky = "n")

        citazione_1 = "\n''Siamo determinati a fare passi audaci e trasformativi urgentemente necessari \nper portare il mondo " \
                    "sulla strada della sostenibilità e della resilienza.\n\n" \
                    "Nell’intraprendere questo grande viaggio collettivo, \npromettiamo che nessuno verrà lasciato indietro.''\n" \
                    "\n(Onu, Agenda 2030)\n"

        self.__citazione_1_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = citazione_1,
                                                      bg=id_color_right, justify= "center" if self.__root__.winfo_screenwidth()>=1600 else "left",
                                         font=("Bahnschrift Light", 12, "italic")
                                                      ).grid(row=2, column = 0, sticky = N if self.__root__.winfo_screenwidth()>=1600 else W)

        self.__titolo_1_info_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = "Avvento dell’Agenda 2030\n",
                                                      bg=id_color_right, justify= "left",
                                         font=("Bahnschrift SemiCondensed", 14, "bold")
                                                      ).grid(row=3, column = 0, sticky = W)

        par_1 = "Negli ultimi anni organismi internazionali e locali, sensibilizzati " \
                "da vari accadimenti, \ntra cui quelli naturali, con lo sguardo rivolto " \
                "alle future generazioni, hanno sentito \nla necessità di intervenire in " \
                "modo deciso a sostegno dello Sviluppo Sostenibile.\n\n" \
                "In sintesi, tale tematica si concentra su di un progresso che non risulta essere \ncircostanziato " \
                "al mero soddisfacimento dei bisogni attuali bensì si pone il problema \ndi agire " \
                "positivamente in vista di esigenze future, per il bene delle prossime generazioni.\n\n" \
                "Conseguentemente, nel settembre 2015, tutti i 193 Paesi delle Nazioni Unite, " \
                "tra cui l’Italia, \nhanno concepito un piano d’azione per contribuire allo sviluppo " \
                "globale, promuovere il \nbenessere umano e proteggere l’ambiente.\n\n" \
                "Il bisogno di garantire un presente ed un futuro migliore al nostro " \
                "Pianeta e alle persone \nche lo abitano è sfociato nella definizione " \
                "di Obiettivi di Sviluppo Sostenibile (Sustainable \nDevelopment Goals" \
                " – il cui acronimo inglese è SDGs) da raggiungere entro il 2030:\n" \
                "è nata, così l’Agenda 2030 che si propone di agire in modo sostenibile " \
                "e che consta di 17 \nobiettivi, o goal, declinati in 169 traguardi, " \
                "anche detti target, in relazione ai vari domini \ndello sviluppo sociale ed economico.\n\n"

        self.__parag_1_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = par_1,
                                                      bg=id_color_right, justify= "left",
                                     font=("Bahnschrift Light", 12)).grid(row=4, column = 0, sticky = W)

        image_obiettivi = PhotoImage(file=__get_path__("utils\\images\\SDG\\SDG_Poster_#nonUN-IT500x290.png"))
        self.__lbl_image_obiettivi__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      image = image_obiettivi,
                                                      bg=id_color_right, justify= "center" if self.__root__.winfo_screenwidth()>=1600 else "left"
                                                      ).grid(row=5, column = 0, sticky = "n" if self.__root__.winfo_screenwidth()>=1600 else "w")
        self.__titolo_2_info_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = "\nPuglia Sostenibile\n",
                                                      bg=id_color_right, justify= "left",
                                         font=("Bahnschrift SemiCondensed", 14, "bold")
                                                      ).grid(row=6, column = 0, sticky = W)

        citazione_2="''Ho imparato che la Computer Science non si ferma solo\nalla sintassi ed allo scrivere del codice.\n\n" \
        "Possiamo fare la differenza nella vita delle persone\nattraverso lo sviluppo di applicazioni.''\n" \
        "\n(Kyle Rector)\n"


        self.__citazione_2_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = citazione_2,
                                                      bg=id_color_right, justify= "center" if self.__root__.winfo_screenwidth()>=1600 else "left",
                                         font=("Bahnschrift Light", 12, "italic")
                                                      ).grid(row=7, column = 0, sticky = N if self.__root__.winfo_screenwidth()>=1600 else W)

        par_2 = "Similarmente a quanto sviluppato dalla Commissione Europea con la loro" \
                " \npiattaforma KnowSDGs per valutare la correlazione tra i vari SDGs e le " \
                "normative Europee, \nscritte in lingua inglese, è stato ideato 'Puglia Sostenibile':\n" \
                "un software in grado di monitorare la presenza degli SDGs " \
                "all’interno delle Leggi Regionali \nPugliesi, in lingua italiana.\n\n" \
                "Questo lavoro nasce dal progetto, conseguente ad accordi stipulati tra " \
                "l’Università degli \nStudi di Bari e la Regione Puglia ed oggetto del tirocinio interno, presso la " \
                "sede del Laboratorio \ndi Sistemi Intelligenti della locale facoltà di " \
                "Informatica, presieduto dal Prof. Giuseppe Pirlo \ne svolto da Claudia Lorusso" \
                " in coordinamento con Alessandro Dattoli, \nil tutto sotto la supervisione del dott. " \
                "Michele Chieco e della D.ssa Gabriella Calvano.\n\n" \
                "La finalità del software è quella di capire quali tra gli obiettivi e traguardi " \
                "dell’Agenda 2030 \nsono stati effettivamente affrontati dai documenti " \
                "legislativi della Regione Puglia in modo da poter, \ntra l’altro, individuare e " \
                "correggere eventuali lacune e determinare l’effettivo progresso \nverso il " \
                "sostenibile.\n\n" \
                "L’utilizzo del software è, ovviamente, estendibile anche ad altre tipologie normative.\n\n" \
                "Il linguaggio utilizzato per lo sviluppo di Puglia Sostenibile è il python.\n\n"

        self.__parag_2_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = par_2,
                                                      bg=id_color_right, justify= "left",
                                     font=("Bahnschrift Light", 12)).grid(row=8, column = 0, sticky = W)
        image_collab = PhotoImage(file=__get_path__("utils\\images\\collab\\trio_collab500x162.png" if self.__root__.winfo_screenwidth()>=1600 else "utils\\images\\collab\\trio_collab400x97.png"))
        self.__lbl_image_collab__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      image = image_collab,
                                                      bg=id_color_right, justify= "center"
                                                      ).grid(row=9, column = 0, sticky = "n")


        self.__titolo_3_info_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = "\nIl Logo\n",
                                                      bg=id_color_right, justify= "left",
                                         font=("Bahnschrift SemiCondensed", 14, "bold")
                                                      ).grid(row=10, column = 0, sticky = W)
        image_logo = PhotoImage(file=__get_path__("utils\\images\\COLORPugliaSostenibile300x276.png"))
        self.__lbl_logo__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      image = image_logo,
                                                      bg=id_color_right, justify= "center"
                                                      ).grid(row=11, column = 0, sticky = "n")
        citazione_2 = "\n''Credo che abbiamo il dovere di lottare per la vita sulla Terra \ne non solo a nostro beneficio, ma di" \
                      " tutti quelli, umani o meno, \nche ci hanno preceduto ed ai quali siamo legati, \ncosì come coloro che, " \
                      "se siamo abbastanza saggi, \narriveranno più tardi. \nNon c'è una causa più urgente, né più giusta, del " \
                      "proteggere il futuro della nostra specie.''\n" \
                    "\n(Carl Sagan)\n"

        self.__citazione_2_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = citazione_2,
                                                      bg=id_color_right, justify= "center" if self.__root__.winfo_screenwidth()>=1600 else "left",
                                         font=("Bahnschrift Light", 12, "italic")
                                                      ).grid(row=12 ,column = 0, sticky = N if self.__root__.winfo_screenwidth()>=1600 else W)

        par_3 = "È doveroso spendere alcune parole per il logo ideato per il software di cui si sta trattando.\n\n" \
                      "In primo piano si nota la figura di un albero che riconduce alla mente l’idea della Natura, " \
                      "\na quel meccanismo tanto complesso che trasforma ogni singola azione in vita.\n\n" \
                      "Ma la sostenibilità non è l’agire positivamente solo ed esclusivamente per il bene dell’ambiente.\n\n" \
                      "Di fatto, dal tronco dell’albero fuoriescono dei rami le cui estremità si plasmano in frecce; \nogni freccia " \
                      "punta verso direzioni differenti che rappresentano le varie branche della sostenibilità \ne che, seppur " \
                      "divergenti, nascono tutte quante da uno stesso principio: \nil bene della comunità raggiungibile tramite " \
                      "un’azione comune.\n\n" \
                      "Ed è appunto per questo che, alle spalle dell’albero, si intravede la Terra che ha significato ambivalente: \n" \
                      "sprona ad agire per il suo bene ed allo stesso tempo stimola un’azione comune per l’ottenimento di quel \n" \
                      "tanto agognato cambiamento.\n\n" \
                      "Il logo è stato realizzato dall’esperto di grafica Nicola Surgo.\n\n\n\n\n\n\n\n\n\n\n\n\n\n" \
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

        self.__parag_3_lbl__ = Label(self.__scrollableframe__.scrollable_frame,
                                                      text = par_3,
                                                      bg=id_color_right, justify= "left",
                                     font=("Bahnschrift Light", 12)
                                     ).grid(row=13, column = 0, sticky = W)

        self.__scrollableframe__.pack()



        #                                        ---------  AVANZATE --------                                                           2.   Avanzate

        # -------------------------------------------------------------------------------------- AVANZATE Frame creation
        self.__adv_frame__ = Frame(self.__principal_frame__, bg=id_color_right, width = self.__root__.winfo_screenwidth())


        self.__grammatura_lbl__ = Label(self.__adv_frame__,justify="left", text="Grammatura (Utente esperto)",
                                       font=("Bahnschrift SemiCondensed", 14, "bold"), bg=id_color_right)
        self.__grammatura_lbl__.grid(row=0, column=0, sticky=W, padx = 0 if self.__root__.winfo_screenheight()<=768 else 5, pady=0 if self.__root__.winfo_screenheight()<=768 else 5)

        self.__grammatura_expl_lbl__ = Label(self.__adv_frame__, justify="left", text="Clicca sulla Grammatura che preferisci:",
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__grammatura_expl_lbl__.grid(row=1, column=0, sticky=W, padx = 0 if self.__root__.winfo_screenheight()<=768 else 5, pady=0 if self.__root__.winfo_screenheight()<=768 else 5)

        r1 = Radiobutton(self.__adv_frame__,
                       text="Bigram",
                       padx=20,
                       variable=self.__ngram__, font=("Bahnschrift Light", 12),
                       value=2, bg=id_color_right
                    )
        r1.grid(row=2, column=1, sticky=E)

        r2 = Radiobutton(self.__adv_frame__,
                       text="Unigram",
                       padx=20,
                       variable=self.__ngram__, font=("Bahnschrift Light", 12),
                       value=1, bg=id_color_right
                    )
        r2.grid(row=2, column=0, sticky=W)

        r1.bind("<Leave>", lambda e: "break")

        self.__choose_t_sdg_lbl__ = Label(self.__adv_frame__,justify="left", text="Rileva SDG o Target",
                                       font=("Bahnschrift SemiCondensed", 14, "bold"), bg=id_color_right)
        self.__choose_t_sdg_lbl__.grid(row=3, column=0, sticky=W, padx = 0 if self.__root__.winfo_screenheight()<=768 else 5, pady=0 if self.__root__.winfo_screenheight()<=768 else 5)

        self.__choose_t_sdg_expl_lbl__ = Label(self.__adv_frame__, justify="left", text="Scegli tra SDG e Target:",
                                       font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__choose_t_sdg_expl_lbl__.grid(row=4, column=0, sticky=W, padx = 0 if self.__root__.winfo_screenheight()<=768 else 5, pady=0 if self.__root__.winfo_screenheight()<=768 else 5)

        r3 = Radiobutton(self.__adv_frame__,
                       text="Target",
                       padx=20,
                       variable=self.__sim_target__, font=("Bahnschrift Light", 12),
                       value=True, bg=id_color_right, command = self.__change_sim_target_title__
                    )
        r3.grid(row=5, column=1, sticky=E)

        r4 = Radiobutton(self.__adv_frame__,
                       text="SDG",
                       padx=20,
                       variable=self.__sim_target__, font=("Bahnschrift Light", 12),
                       value=False, bg=id_color_right, command = self.__change_sim_target_title__
                    )
        r4.grid(row=5, column=0, sticky=W)

        r3.bind("<Leave>", lambda e: "break")

        Label(self.__adv_frame__, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n", bg=id_color_right, justify= "left",
                                     font=("Bahnschrift Light", 12)
                                     ).grid(row=6, column = 0, sticky = W)

        #                                        ---------  AGENDA 2030 --------                                                        3.   Agenda 2030

        # ----------------------------------------------------------------------------------- AGENDA 2030 Frame creation
        self.__agenda_frame__ = Frame(self.__principal_frame__, bg=id_color_right)

        agenda_directory = __get_path__("Agenda2030\\Agenda-2030-Onu-italia.pdf")

        # -----------------------------------------------------------------
        # Tkinter code
        # -----------------------------------------------------------------

        # creating object of ShowPdf from tkPDFViewer.
        pdf_viewer= tkPDFViewer.ShowPdf()

        # Adding pdf location and width and height.
        self.__show_agenda__ = pdf_viewer.pdf_view(self.__agenda_frame__,
                         pdf_location=agenda_directory,
                         width=(self.__root__.winfo_screenwidth()//25) +10 if self.__root__.winfo_screenwidth()>=1680 else self.__root__.winfo_screenwidth()//14,
                                                   height=43 if self.__root__.winfo_screenheight()>=1050 else (48 if self.__root__.winfo_screenheight()>=768 else 35))

        # Placing Pdf in my gui.
        self.__show_agenda__.pack()


        #                                        ---------  CONTATTI --------                                                           4.   CONTATTI

        # -------------------------------------------------------------------------------------- CONTATTI Frame creation
        self.__contact_frame__ = Frame(self.__principal_frame__, bg=id_color_right)

        # label name
        supervisors_author = "\nSupervisore:\tChiar.mo Prof. Pirlo Giuseppe, presso l'Università degli Studi di Bari"
        gui_author = "GUI e back-end:\tLorusso Claudia,\t\tlorussoclaudia95@libero.it"
        logo_author = "Logo:\t\tSurgo Nicola,\t\tsurgo.nicola20@gmail.com"

        cont_authors = "---------------------------------------------------------------------------" \
                       "-----\n\n"+supervisors_author + \
                       "\n\n\n------------------------------------------" \
                       "--------------------------------------\n\nContatti Tecnici:\n\n" \
                       + gui_author + "\n\n" + logo_author
        self.__contact_lbl__ = Label(self.__contact_frame__, justify="left", text=cont_authors,
                                   font=("Bahnschrift Light", 12), bg=id_color_right)
        self.__contact_lbl__.grid(row=0, column=0, sticky=W, padx=(10), pady=10)

        #grid the home_fram ONLY. The other Variable Frame will be gridded when needed
        self.__home_frame__.grid(row=3, column=0, sticky=W, padx=(10), pady=10)
        # defines min and max root dimension
        self.__root__.update()
        self.__root__.minsize(self.__root__.winfo_width(), self.__root__.winfo_height())

        self.__root__.mainloop()

    def __toggleFullScreen__(self, event):
        self.fullScreenState = not self.fullScreenState
        self.__root__.attributes("-fullscreen", self.fullScreenState)

    def __quitFullScreen__(self, event):
        self.fullScreenState = False
        self.__root__.attributes("-fullscreen", self.fullScreenState)

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

    def __change_sim_target_title__(self):
        """
        Changes the sdg or target Title and unbinds the radiobutton

        """
        self.__ric_targets_lbl__.configure(text = "Ricerca Target" if self.__sim_target__.get() else "Ricerca SDGs")


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
        self.__keycatch_frame__.configure(text="  Seleziona una nuova Legge ed inserisci la parola chiave ")
        self.__insert_key__.configure(state="disabled", cursor = "arrow")
        self.__cerca_btn__.configure(state="disabled")
        self.__cerca_btn__.configure(cursor="arrow")
        self.__key_occ__ = ""
        self.__ky_occ_res_label__.configure(text=self.__key_occ__)

    def __show_targets__(self, back_btn, btn_frame, variable_frame, sdgs, i):

        back_btn.grid(row=2, sticky=W, padx=(5), pady=5)
        back_btn.config(state=NORMAL)

        agenda = sdgs["Agenda"]
        sdg = agenda[i]

        scrollable_frame = ScrollableFrame(variable_frame, bg="white", width=800, height=500, horizontal = True)

        title = Label(scrollable_frame.scrollable_frame,
                      text="Goal " + str(sdg["id"]) + ":",
                      bg="white", justify="left",
                      font=("Bahnschrift SemiCondensed", 18, "bold")
                      )
        title.grid(row=0, column=0, sticky=W)
        description = Label(scrollable_frame.scrollable_frame,
                      text=sdg["goal"] + "\n---------------------------------------------------------------------------"
                                         "-----------------------------------------------------------------------------"
                                         "-----------------------------------------------------------------------------"
                                         "------------------------------------------",
                      bg="white", justify="left",
                      font=("Bahnschrift Light", 14)
                      )
        description.grid(row=1, column=0, sticky=W)
        j = 2
        for t in sdg["targets"]:
            id = t["absolute_id"]
            desc = t["description"]
            title = Label(scrollable_frame.scrollable_frame,
                          text="Target " + id + ":",
                          bg="white", justify="left",
                          font=("Bahnschrift SemiCondensed", 14, "bold")
                          )
            title.grid(row=j, column=0, sticky=W)
            j += 1
            descr = Label(scrollable_frame.scrollable_frame,
                          text=desc + "\n",
                          bg="white", justify="left",
                          font=("Bahnschrift Light", 12)
                          )
            descr.grid(row=j, column=0, sticky=W)
            j += 1

        scrollable_frame.pack()
        variable_frame.pack()
        btn_frame.pack_forget()


    def __close_popup__(self, popupwindow):
        """
        Closes the popupwindow
        :param popupwindow: TopLevel
            the popupwindow
        :return:
        """
        popupwindow.destroy()
        self.__sfogliami_btn__.configure(state=NORMAL, cursor="hand2", bg = "#F0F0F0")

    def __go_back__(self, back_btn,  btn_frame, variable_frame):
        """
        Manages the go back button belonging to the popupwindow toplevel
        :param back_btn: Button, the back button
        :param btn_frame: Frame, the Frame containing the buttons
        :param variable_frame: Frame, the Frame containing each SDG description (SDG description is updated each
        time the use clicks on a button)
        :return:
        """
        btn_frame.pack()
        for widgets in variable_frame.winfo_children():
            widgets.destroy()
        variable_frame.pack_forget()
        back_btn.grid_forget()


    def __popup_sdgs__(self):
        """
        Pops up a new window with the SDGs list
        :return:
        """
        #open json file with SDGs and get vocabulary
        dest_sdgs= __get_path__("SDGs\\SDGs_json.json")
        with open(dest_sdgs, "r", encoding="utf-8") as file:
            sdgs = json.load(file)

        id_color_right = "#F7F7F7"
        popupwindow = Toplevel(self.__root__)
        popupwindow.configure(bg="white")
        popupwindow.configure(width = 1500, height = 700)

        width = popupwindow.winfo_screenwidth()

        if width<1680:
            popupwindow.tk.call("tk", "scaling", 1)
        if width>2000:
            popupwindow.tk.call("tk", "scaling", 1.5)

        popupwindow.wm_title("Obiettivi di Sviluppo Sostenibile: SDGs")

        master_frame = Frame(popupwindow, bg="white",width = 1500, height = 700 )
        master_frame.grid(row=0, column = 0, padx = 10, pady=10)

        # title label
        title = "Obiettivi di Sviluppo Sostenibile"
        title_lbl__ = Label(master_frame, justify="center", text=title, font=("Bahnschrift SemiCondensed", 35), bg="white")
        title_lbl__.grid(row=0, column=0, sticky=N)

        #---------------------------------intern frame
        intern_frame = Frame(master_frame, bg="white",width = 1100, height = 700)
        intern_frame.grid(row=1, column = 0, padx = 5, pady=5)

        variable_frame = Frame(intern_frame, bg="white",width = 1100, height = 700)

        # ---------------------------------------------------- BUTTONS

        close_btn = Button(master_frame, bg = id_color_right, height=1, width=10, borderwidth=0, font=("Bahnschrift SemiCondensed", 12),
                           command=(lambda:self.__close_popup__(popupwindow)), text="Chiudi", cursor = "hand2")
        back_btn = Button(master_frame, bg = id_color_right,text="Indietro", height=1, width=10, borderwidth=0,  cursor = "hand2", font=("Bahnschrift SemiCondensed", 12),
                          command=(lambda:self.__go_back__(back_btn, btn_frame, variable_frame)))
        close_btn.grid(row=2, sticky=E, padx=(5), pady=5)

        # ------------------------------------- BTN FRAME
        btn_frame = Frame(intern_frame, bg=id_color_right, width=1100, height=700)


        heigh = popupwindow.winfo_screenheight()

        if heigh<900:
            dest = __get_path__("utils\\images\\SDG\\goals_min\\*.png")
        else:
            dest = __get_path__("utils\\images\\SDG\\goals\\*.png")


        for img in sorted(glob(dest), key=len):
            name = int(path.splitext(path.basename(img))[0])
            image = PhotoImage(file=img)
            if name >= 1 and name <= 6:
                b = Button(btn_frame, image=image, cursor="hand2", borderwidth=0,command = (lambda name = name: self.__show_targets__(back_btn,  btn_frame, variable_frame, sdgs, name-1)))
                b.grid(row=0, column=name - 1, padx=5, pady=5)
            elif name >= 7 and name <= 12:
                b = Button(btn_frame, image=image, cursor="hand2", borderwidth=0,command = (lambda name = name: self.__show_targets__(back_btn,  btn_frame, variable_frame, sdgs, name-1)))
                b.grid(row=1, column=name - 7, padx=5, pady=5)
            else:
                b = Button(btn_frame, image=image, cursor="hand2", borderwidth=0,command = (lambda name = name: self.__show_targets__(back_btn,  btn_frame, variable_frame, sdgs, name-1)))
                b.grid(row=2, column=name - 13, padx=5, pady=5)
            b.photo = image # <-- assign PhotoImage to other widget too DO NOT REMOVE!!!!

        btn_frame.pack()

        popupwindow.resizable(False, False)

        popupwindow.protocol("WM_DELETE_WINDOW",  lambda:self.__close_popup__(popupwindow))

    def __enable_sfogliami(self):
        """
        Enables 'Sfogliami' btn
        :return:
        """
        self.__sfogliami_btn__.configure(state=NORMAL, cursor="hand2")

    def __consult_sdgs__(self):
        """
        If the sfogliami_btn is pressed it will pop up a page with the SDG list.
        :return:
        """
        self.__sfogliami_btn__.configure(state=DISABLED, cursor="arrow", bg = "#A6F7AA")
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
                output = get_relevant(path_law=self.__file_name__, ngram=self.__ngram__.get(), sim_target=self.__sim_target__.get())
            except ValueError:
                messagebox.showwarning("Warning", "Il file selezionato potrebbe essere protetto da password.\nPer favore, seleziona un altro file.")
                warning = True
            except IOError:
                messagebox.showwarning("Warning", "Impossibile processare il file per uno dei seguenti motivi:"
                                                    "\n-\til file è vuoto;"
                                                    "\n-\til file contiene solo immagini;"
                                                    "\n-\til file è corrotto."
                                                  "\n\nPer favore, seleziona un altro file.")
                warning = True
            except Exception as e:
                messagebox.showerror("Error", e + "\nContatta gli sviluppatori per fare un report del problema.\n")
                warning = True

            # get file name from path
            file_name = path.basename(dest)
            if warning: #if law wasn't correctly selected
                self.__adv_sel_lbl__.config(
                    text="Il file selezionato ('" + file_name + "') non può essere processato. Per favore, seleziona un'altra legge.")
                self.__sel_lbl__.config(text="Premi su 'Seleziona Legge'")
            else:
                # get string containing the output
                self.__output__ = "I primi tre"
                self.__output__ += (" SDG " if not self.__sim_target__.get() else " Target ")
                self.__output__ += "più similari alla legge " + file_name + " sono:\n\n" + output + " \n\nPer favore seleziona un'altra Legge per una nuova computazione."
                self.__txt_box__.configure(state=NORMAL)
                self.__txt_box__.insert(INSERT, self.__output__)
                self.__txt_box__.configure(state="disabled")
                self.__keycatch_frame__.configure(text = "  Inserisci la parola chiave ")
                self.__insert_key__.configure(state="normal", cursor = "xterm")
                self.__cerca_btn__.configure(state="normal")
                self.__cerca_btn__.configure(cursor="hand2")

                self.__adv_sel_lbl__.config(text="")
        self.__start_btn__.configure(state="disabled")
        self.__start_btn__.configure(cursor="arrow")




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
            0: "Questa sezione è dedicata all'utilizzo di 'Puglia Sostenibile'."
               "\nIl software ti permette di estrapolare, in modo semplice ed intuitivo, i tre goal (o target), appartenenti all'Agenda 2030,\n"
                "più rilevanti per la legge da te selezionata.\n"
                "\nUtilizzare 'Puglia Sostenibile' è molto semplice!\n"
                "Ti basterà selezionare il file ('.pdf', '.docx' o '.txt') contenente la legge che vorresti analizzare e quindi cliccare sul pulsante 'Start'.\n\n"
                "Inoltre, potrai anche effettuare una ricerca manuale per capire se una parola chiave è inclusa, o meno, all'interno della legge; \n"
               "per farlo, devi soltanto digitare la keyword nell'apposito box e, dopo aver premuto il pulsante 'Cerca',"
               " il programma ti restituirà il \nnumero di volte che la stessa compare nel testo.",
            1: "Questa sezione è dedicata alla storia dell'Agenda 2030 e di 'Puglia Sostenibile'.\n"
               "Se sei curioso di conoscere com'è nato questo progetto, prosegui nella lettura.",
            2: "In questa sezione potrai mettere mano alle impostazioni avanzate di 'Puglia Sostenibile', cambiando le"+
               " seguenti proprietà:"+
               "\n-\tGrammatura;"+
               "\n-\tRileva SDG o Target.\n\n"+
               "Prima di andare avanti, è bene forniti delle informazioni preliminari.\n"+
               "Devi sapere che 'Puglia Sostenibile', per il momento, effettua la computazione di similarità"+
               " tra il documento da te caricato (la Legge) ed \ni vari Obiettivi di Sviluppo Sostenibile (SDGs),"+
               " dell'Agenda 2030, per mezzo della Similarità del Coseno.\n"+
               "La matrice TFIDF, propedeutica a questo calcolo, suddivide ogni documento"+
               " in una serie di parole chiave (keyphrase).\n\nUn esempio di keyphrase è 'Emancipazione' oppure 'Femminile'.\n\n"+
               "Si è dato modo all'utente di cambiare la Grammatura, ossia il numero di parole da cui è composta ogni parola chiave, "+
               "facendoti scegliere \ntra una computazione Unigram ed una Bigram.\n" +
               "\nNella computazione Unigram ogni keyphrase è composta da una singola parola (DEFAULT)." + ("\n" if self.__root__.winfo_screenheight()>768 and not self.__root__.winfo_screenheight()==800 else "") +
               "\nNella computazione Bigram ogni keyphrase è composta da una o due parole:\n"+
               "esempi di keyphrase Bigram sono 'Emancipazione Femminile', 'Paternariato', 'Povertà Assoulta', etc.\n\n"
               "Fai attenzione, però, nel caso di grammatura Bigram la computazione risulterà più"+
               " precisa ma allo stesso tempo più selettiva.\n\nPuoi, inoltre, selezionare il tipo di output da computare "+
               "decidendo tra il visualizzare gli SDGs più similari alla Legge (es. SDG 5, SDG 3, SDG 15, etc.)\n"+
               "ovvero, nello specifico, i Target più rilevanti (es. Target 5.5, Target 3.1, Target 15.c, etc.). Per farlo, ti basta modificare "+
               "l'apposita impostazione.\n\nOra tocca a te!",
            3: "In questa sezione puoi consultare l'Agenda 2030.\n\n"
               "Per maggiori informazioni visita il sito ''https://unric.org/it/agenda-2030/''.",
            4: "In questa sezione trovi tutti i contatti necessari per inviare feedback, chiedere informazioni e"
               " comunicare qualsiasi \ntipo di problema dovessi riscontrare con il programma."
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
            - home
            - info
            - advanced
            - agenda
            - contact

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

        self.__welcome_frame__.grid_forget()
        self.__right_frame__.grid(row = 0, column = 2, sticky = "n")

        #show the desired frame while hiding the others
        frame_list = self.__get_variable_frame_list__()

        self.__forget_grid_variable_frames__()
        frame_list[id].grid(row=3, column=0, sticky=W)


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
class ScrollableFrame(Frame):
    """
    Defines a ScrollbarFrame class
    """
    def __init__(self, container, width=800, height=700, bg = "#FCFCFC", horizontal = False,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.horizontal = horizontal
        #container.bind("<MouseWheel>", self._on_mousewheel)  # bind on the parent window

        # highlightthickness=0 to hide the border
        highlightthickness = 0

        # Create a main frame

        self.main_frame = Frame(container, width=width, height=height,bg=bg)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=1)  # expand frame to the size of the container

        #create a canvas

        self.canvas = Canvas(self.main_frame, width=width, height=height, bg=bg, highlightthickness=highlightthickness)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        #width = 0 to hide the bar


        self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL, command=self.canvas.yview, bg = bg)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        if self.horizontal:
            self.scrollbar_x = Scrollbar(container, orient=HORIZONTAL, command=self.canvas.xview, bg = bg)
            self.scrollbar_x.pack(side=BOTTOM, fill=X)
            self.canvas.configure(xscrollcommand = self.scrollbar_x.set)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        #if I need greed
        #self.canvas.grid(row=0, column = 0)
        #self.scrollbar.grid(row = 0, column = 1, sticky="NS")
        #self.scrollbar_x.grid(row=1, column = 0, sticky="EW")

        self.scrollable_frame = Frame(self.canvas, bg=bg)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        #DO NOT TOUCH!!!!!! DO NOT PUT bind_all!!!
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<MouseWheel>", self.set_mousewheel(self.canvas, self._on_mousewheel))

    def _on_mousewheel(self, event):
        """
        Permits to scroll with mouse
        IF YOU TOUCH ME I WONT WORK ANYMORE!
        :param event:
        """
        #DO NOT TOUCH
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        """
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift:
            self.canvas.xview_scroll(scroll, "units")
        else:
            self.canvas.yview_scroll(scroll, "units")

        """

    def set_mousewheel(self, widget, command):
        """Activate / deactivate mousewheel scrolling when
        cursor is over / not over the widget respectively."""
        #DO NOT TOUCH!!!!
        widget.bind("<Enter>", lambda _: widget.bind_all('<MouseWheel>', command))
        widget.bind("<Leave>", lambda _: widget.unbind_all('<MouseWheel>'))


    def background(self, bg):
        """
        Modifies the background color
        :param bg: string
            specifies the background color
            use bg = "#FCFCFC" for a soft green near the white
        :return:
        """
        self.scrollbar.configure(bg=bg)
        if self.horizontal:
            self.scrollbar_x.configure(bg=bg)
        self.scrollable_frame.configure(bg=bg)
        self.canvas.configure(bg=bg)
        self.main_frame.configure(bg=bg)

    def bar_width(self, width):
        """
        Modifies the bar of the scroll bar width
        :param width: int
            bar of the scrollbar dimension
            if width=0 the bar will disappear
        :return:
        """
        self.scrollbar.config(width=width)

    def highlightthickness(self, highlightthickness):
        """
        Modifies the thickness of the border of the frame
        :param highlightthickness: integer
            thickness of the border of the frame
            if highlightthickness=0 the border will disappear
        :return:
        """
        self.canvas.configure(highlightthickness=highlightthickness)

    def frame_dimension(self, width=800, height=700):
        """
        Modifies the dimension of the frame
        :param width: int
            specified the (orizontal) width of the frame
        :param height: int
            specified the (vertical) height of the frame
        :return:
        """
        self.canvas.configure(width=width, height=height)
        self.scrollable_frame.configure(width=width, height=height)
        self.main_frame.configure(width=width, height=height)

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

    # use the code below only for CLI uses;
    # to extract the exe with pyinstaller comment the code below
    # and remove the comments at the bottom of the page
    termination = False
    try:
        from re import sub
        from tkPDFViewer import tkPDFViewer
        from Compute_Similarity import get_relevant
        from FileHandler import ask_path, extract_content
        import json
        from glob import glob

        termination = True
    except ModuleNotFoundError:
        install = Installation()
        termination = install.get_termination()

    if termination:
        app = App()
    """
    #README before attempting to create the .exe
    #PYINSTALLER DOESN'T NEED THE INSTALLATION MODULE
    #YOU NEED TO COMMENT THE CODE ABOVE AND USE WHAT'S BELOW !ONLY!
    from Compute_Similarity import get_relevant
    from FileHandler import ask_path, extract_content
    from tkPDFViewer import tkPDFViewer as pdf
    from re import sub
    from glob import glob
    import json
    app = App()
    """