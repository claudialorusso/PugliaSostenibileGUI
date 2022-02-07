# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:14:19 2021
This class represents one of the Target's belonging to a SDG in the Agenda 2030.
Each Goal has the following properties:
    -   __goal_id__, which is an integer representing the Goal's id to which the current Target belongs;
    -   __id__, an alphanumeric id, representing the current Target;
        The number of Targets belonging to a Goal is variable.
    -   __description__, a string representing the Target's description.

@author: Claudia Lorusso
"""

class Target:

    """
    This class represents one of the Target's belonging to a SDG in the Agenda 2030.
    Each Goal has the following properties:
        -   __goal_id__, which is an integer representing the Goal's id to which the current Target belongs;
        -   __id__, an alphanumeric id, representing the current Target;
            The number of Targets belonging to a Goal is variable.
        -   __description__, a string representing the Target's description.
    """
    def __init__(self, goal_id, index, description):
        self.__goal_id__, self.__id__, self.__description__ = goal_id, index, description

    def get_Goal_id(self):
        """
        :return:
        -------
        int
            Goal's id
        """
        return self.__goal_id__
    
    def get_id(self):
        """
        :return:
        -------
        String
            Target's id
        """
        return self.__id__

    def get_description(self):
        """
        :return:
        -------
        Returns a string containing the Target's description.
        """
        return self.__description__
    
    def __str__(self):
        """
        :return:
        -------
        Returns a String which describes the current Target:
            "#Goals'id"."Target's id": "Target's description"

        """
        return "\tTarget " + str(self.__goal_id__) + "." + self.__id__ +": " + self.__description__ + "\n"
    
    def print_Target(self):
        """
        Prints the Target

        :return:
        -------
        None.

        """
        print(self)
