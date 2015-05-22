#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Yan
#
# Created:     17/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Marque :
    """ classe qui permet l'ajout d'une marque de voiture """
    def __init__(self,p_id, p_libelle):
        """ Constructeur """

        self.id_marque = p_id
        self.libelle_marque = p_libelle

    def getID(self):
        """ methode qui renvoie l'id de la marque de la voiture """
        print("id de la marque")
        return self.id_marque

    def getLibelle(self):
        """ methode qui renvoie le nom de la marque de la voiture """
        print ("Marque")
        return self.libelle

    def setID(self, new_ID):
        """ methode qui modifie l'id de la marque """
        self.id_marque = new_ID
        print("Le nouvel id de la marque "+ self.libelle_marque + " est "+ self.id_marque)

    def setLibelle(self, new_libelle):
        """ methode qui modifie le code de la marque """
        self.libelle_marque = new_libelle
        print("Marque"+ self.libelle_marque)

    def __del__(self):
        """ methode qui supprime la marque """
        del self

