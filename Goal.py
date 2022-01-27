# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:10:04 2021

@author: Claudia Lorusso
"""

class Goal:
    """
    Represents a Goal representative of a SDG belonging to the Agenda 2030.
    Each Goal has the following properties:
        -   a numerical identifier (id). Goals in total are 17 so
            each id belongs to the domain (1, 17).
        -   a descriprion, in the shape of a string.
    """
    def __init__(self, index, description):
        self.__index__, self.__description__ = index, description
        
        
    def get_id(self):
        """
        Returns
        -------
        Goal's id
        """
        
        return self.__index__
    
    
    def get_description(self):
        """
        Returns
        -------
        String
            Goal's description
        
        """
        return self.__description__
        
    def __str__(self):
        """
        Returns
        -------
        Returns a string which describes the current Goal:
            "#id": "description"
        """
        return "Goal " + str(self.__index__) + ": " + self.__description__ 
    
    
    def print_Goal(self):
        """
        Prints the Goal.

        Returns
        -------
        None.

        """
        print(self, "\n")



