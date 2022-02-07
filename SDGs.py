# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:34:20 2021

It represents the set of SDGs that belongs to the Agenda 2030.
Each SDG has:
-   a Goal
-   a list of Target

@author: Claudia Lorusso
"""

#total number of SDGs
MAX_SDGs = 17

class SDGs:
    """
    It represents the set of SDGs that belongs to the Agenda 2030.
    Each SDG has:
    -   a Goal
    -   a list of Target
    """
    def __init__(self):
       self.__sdgs__ = []
       self.__max__ = MAX_SDGs


    def add(self, sdg):
        """
        Adds a SDG to the SDG list.

        :parameter:
        ----------
        sdg : SDG to insert into the SDG list

        :return:
        -------
        None.

        """
        if self.__sdgs__ == []:
            sdg_list = [sdg]
            self.__sdgs__ = sdg_list
        else:
            self.__sdgs__.append(sdg)
        self.__sdgs__.sort(key=lambda x: x.get_Goal_id())

    def get_SDGs(self):
        """
        :return: SDGs
        -------
        Rreturns a SDGs object containing each SDG

        """
        return self.__sdgs__

    def get_SDG(self, id):
        """
        Returns the id-th SDG.

        Parameters
        ----------
        :parameter: id : integer identifier of the SDG to be returned.

        :return: SDG
        -------
        The is-th SDG

        """
        if(id >= 1 and id <= MAX_SDGs):
            return self.__sdgs__[id - 1]
        else:
            print("Inserire un id valido.")


    def __iter__(self):
        """
        re-defines the iterator
        """
        self.n = 0
        return self

    def __next__(self):
        """
        re-defines the next's iterator
        """

        if (self.n < self.__max__):
            
            result = self.__sdgs__[self.n]
            self.n += 1
            
            return result
        else:
            raise StopIteration
        

    
    def __str__(self):
        """
        Override of str function
        :return:
        -------
        Returns a string containing each SDG that belongs to the Agenda 2030.:
            "AGENDA 2030:"
            "SDG 1"
            ...
            "SDG 17"

        """
        sdgs = "AGENDA 2030:\n"
        for sdg in self.__sdgs__:
            sdgs = sdgs + str(sdg) + "\n"
        return sdgs

    def print_SDGs(self):
        """
        Prints each SDG
        """
        print(self)

    def get_len_SDGs(self):
        """
        Returns the total number of SDGs

        :return:
        -------
        int
            Total number of SDGs
        """
        return len(self.__sdgs__)
    
    
    
    def get_len_tot_target(self):
        """
        returns the number of targets

        :return:
        -------
        tot : int
            total number of targets
        """
        tot = 0
        for sdg in self.__sdgs__:
            tot += sdg.get_len_target()
        
        return tot
