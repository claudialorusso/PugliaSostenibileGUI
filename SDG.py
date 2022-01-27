# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:36:52 2021

@author: Claudia Lorusso
"""

class SDG:
    """
    Represents a SDG that belongs to the Agenda 2030
    Each SDG has the following properties:
        - one Goal
        - a list of Target
    """
    def __init__(self, goal):
       self.__goal__ = goal
       self.__id__ = goal.get_id()
       self.__target_list__ = []
    
    def get_Goal(self):
        """ 
        Returns
        -------
        returns the current Goal

        """
        return self.__goal__

    
    def add_Target(self, target):
        """
        Adds a Target to the Target list associated to the current SDG.

        Parameters
        ----------
        target: Target
            Target to add to the Target List
        
        Returns
        -------
        None.

        """
        if(self.__target_list__ == []):
            t_list = [target]
            self.__target_list__ = t_list
        else:
            self.__target_list__.append(target)
    
    def get_Target_id(self, description):
        """
        Parameters
        ----------
        description : Target's description
        
        Returns
        -------
        Returns the id of the Target which description
        is the same as the argument, if it exists;
         -1, else
        """
        for target in self.__target_list__:
            if (target.get_description() == description):
                return target.get_id()

        print("Nessun target con quella descrizione.")
        return -1
    

    def get_Target_description(self, id):
        """
        Parameters
        ----------
        id : Target's id
        
        Returns
        -------
        Returns the description of the id-th Target,
        if it exists; else, "-1".

        """
        for target in self.__target_list__:
            if (target.get_id() == id):
                return target.get_description()
            
        print("Nessun target con quell'identificativo.")
        return -1
    
    
    def get_Target_list(self):
        """
        Returns
        -------
        Returns the list of Target, __target_list_,
        of the current Goal
        """
        return self.__target_list__


    def get_Goal_id(self):
        """
        Returns
        -------
        int
            the goal id
        """
        
        return self.__goal__.get_id()
    
    
    def get_Goal_description(self):
        """
        Returns
        -------
        a string containing the Goal description
        
        """
        return self.__goal__.get_description()

    def __str__(self):
        """
        Returns
        -------
        Returns a string describing the current SDG, in the following way:
            "Goal m"
                "Target 1"
                "Target 2"
                ...
                "Target n"
        """
        t_list = ""
        for target in self.__target_list__:
            t_list = t_list + str(target)
        return "SDG " + str(self.__id__) + ":\n" + str(self.__goal__) + "\n" + t_list

    def print_SDG(self):
        """
        Prints the current SDG

        Returns
        -------
        None.

        """
        print(self)

    def get_len_target(self):
        """
        Returns the total number of targets contained in the current SDG

        Returns
        -------
        integer
            the total number of targets contained in the current SDG

        """
        return len(self.__target_list__)
