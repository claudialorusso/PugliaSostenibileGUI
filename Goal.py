# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:10:04 2021

Represents a Goal representative of a SDG belonging to the Agenda 2030.
Each Goal has the following properties:
        -   a numerical identifier (id). Goals in total are 17 so
            each id belongs to the domain (1, 17).
        -   a description, in the shape of a string.

@author: Claudia Lorusso
"""

class Goal:
    """
    Represents a Goal representative of a SDG belonging to the Agenda 2030.
    Each Goal has the following properties:
        -   a numerical identifier (id). Goals in total are 17 so
            each id belongs to the domain (1, 17).
        -   a description, in the shape of a string.
    """
    def __init__(self, index, description):
        self.__id__, self.__description__ = index, description
        
        
    def get_id(self):
        """
        Returns the goal id
        -------
        :return: integer
            Goal's id
        """
        
        return self.__id__
    
    
    def get_description(self):
        """
        Returns the goal description
        -------
        :return: String
            Goal's description
        
        """
        return self.__description__
        
    def __str__(self):
        """

        :return: a string which describes the current Goal:
            "#id": "description"
        """
        return "Goal " + str(self.__id__) + ": " + self.__description__
    
    
    def print_Goal(self):
        """
        Prints the Goal.
        """
        print(self, "\n")



