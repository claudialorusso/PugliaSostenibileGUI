# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:42:21 2021

Extracts all of the information necessary to model all of the SDG's.
Extracts the goals and targets from a .json file - in the form of a dictionary -
to model each SDG into the SDGs class.

You can choose between:
- SDGs_indicatori.json, (DEFAULT) which contains each SDG in italian in addiction to the global indicators;
- SDGs_json.json, which contains only the SDGs in italian.

After the extraction, each SDG will contain:
- the SDG (  = goal) id;
- the correspondent Goal;
- a list of Target.

Each Goal is characterised by:
- an id;
- a description.

Each Target is characterised by:
- the goal's id they belong to;
- an alphanumeric id;
- a description.

@author: Claudia Lorusso
"""

from Goal import Goal
from Target import Target
from SDG import SDG
from SDGs import SDGs

import sys
from os import path


class SDGs_Extractor:
    """
    Extracts all of the information necessary to model all of the SDG's.
    Extracts the goals and targets from a .json file - in the form of a dictionary -
    to model each SDG into the SDGs class.

    You can choose between:
    - SDGs_indicatori.json, which contains each SDG in italian in addiction to the global indicators;
    - SDGs_json.json, which contains only the SDGs in italian.

    After the extraction, each SDG will contain:
    - the SDG (  = goal) id;
    - the correspondent Goal;
    - a list of Target.

    Each Goal is characterised by:
    - an id;
    - a description.

    Each Target is characterised by:
    - the goal's id they belong to;
    - an alphanumeric id;
    - a description.

    """

    def __init__(self):
        self.__sdgs__ = SDGs()

    def __get_path__(self, relative_path):
        """
        Converts the relative path into an absolute path
        :param relative_path: string, relative path of the file
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

    def __get_sdgs_dict__(self):
        """
        Extracts the dictionary contained in the specified .json file:
        -   SDGs\\SDGs_json.json : contains each SDG extracted from the AGENDA 2030
        -   SDGs\\SDGs_indicatori.json : contains each SDG in addiction to each indicator extracted from Metadati_SDGs.xlsx
        Irrespectively of what file is chosen, the dictionary appears like this:
        {
            "Agenda":
            [ # is a list of dictionaries
                {
                    "id": "string representing the SDG_1 id",
                    "goal": "description of SDG_1",
                    "targets": [ #is a list of dictionaries for each target
                        {
                            "id": "string representing the target_1 id",
                            "description": "description of target_1",
                            "absolute_id": "goal_1 id + target_1 id"
                        },
                        ...
                        {
                            "id": "string representing the target_n id",
                            "description": "description of target_n",
                            "absolute_id": "goal_1 id + target_n id"
                        }

                }, ...
                {
                    #same as above for each SDG till the n-th
                }
            ]
        }
        :return: dictionary
        -------
        A dictionary containing each SDGs
        """
        import json
        file = "SDGs\\SDGs_idicatori.json" #REPLACE HERE with SDGs_json.json to have the classical SDGs with no indicatori
        dest = self.__get_path__(file)
        with open(dest, "r", encoding="utf-8") as f:
            sdgs = json.load(f)
        return sdgs

    def __process_sdgs__(self):
        """
        Processes each SDG contained into the dictionary
        outputted by the json file.
        :return: None
        """
        sdg_dict = self.__get_sdgs_dict__()
        for sdg in sdg_dict["Agenda"]:
            self.__process_Goal__(sdg)
            self.__process_Targets__(sdg)

    def __process_Goal__(self, sdg):
        """
        Processes a Goal object with the relative informations (id and description)
        extracted from the sdg argument.
        (see self.__get_sdgs_dict__ for more informations)
        The Goal is, then, added to an SDG object.
        The SDG is then added to the sdg list, self.__sdgs__ .

        :param sdg: a dictionary containing information about an SDG.
        :return:
        -------
            None.
        """

        id = sdg["id"]
        description = sdg["goal"]

        goal = Goal(int(id), description)
        s = SDG(goal)
        self.__sdgs__.add(s)

    def __process_Targets__(self, sdg):
        """
        Processes each Target contained into the sdg.
        Extracts the relative information (alphanumeric id and description)
        from the sdg (argument).
        Each target is, progressively, added to the correspondent SDG into
        self.__sdgs__ .
        :param sdg: a dictionary containing informations about an SDG.
        :return:
        -------
            None.
        """

        sdg_id = sdg["id"]
        target_list = sdg["targets"]
        for target in target_list:
            id = target["id"]
            description = target["description"]
            t = Target(int(sdg_id), id, description)
            self.__sdgs__.get_SDG(int(sdg_id)).add_Target(t)

    def get_SDGs(self):
        """
        Processes and outputs the SDGs contained into the Agenda.
        :return: SDGs
        -------
        An SDGs object containing each SDG.
        """
        self.__process_sdgs__()
        return self.__sdgs__

    def __str__(self):
        """
        Override of str.
        :return: string
        -------
        Returns a String containing the SDGs (in Italian).
        WARNING: if the sdgs are not yet processed
        the String will be equal to:
        Agenda 2030:
            *void*
        """
        return str(self.__sdgs__)

    def print(self):
        """
        Prints the SDGs.

        :return:
        -------
        None.

        """
        print(self)


"""
#test
#remove triple prime to test the class
if __name__ == '__main__':
    s = SDGs_Extractor()
    s.get_SDGs()
    print(s)
"""
