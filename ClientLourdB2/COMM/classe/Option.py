#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan
#
# Created:     17/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Option :
    """
    Classe permettant de definir les option d'un vehicule
    """
    def __init__(self, p_id, p_libelle, p_prix, p_tva):

        """ Constructeur """
        self.id_option = p_id
        self.libelle_option = p_libelle
        self.prix_option = p_prix
        self.id_tva_option = p_tva


    def getLibelle(self):
        """ methode permettant d'acceder au nom de l'option courante"""
        print ("L'option selectionnee")
        return self.libelle_option

    def getPrix(self):
        """ methote qui renvoie le prix de l'option courante """
        print ("Prix de l'option ")
        return self.prix_option

    def getTVA(self):
        """ methode qui renvoie la tva appliquee sur l'option """
        print("TVA de l'option")
        return self.id_tva_option

    def setLibelle(self, new_libelle):
        """ methode qui modifie le libelle de l'option courante """

        self.libelle_option = new_libelle
        print("le nouveau libelle enregistre est  :"+ self.libelle_option)


    def setPrix(self, new_prix):
        """ methode qui modifie le prix de l'option courante """

        self.prix_option = new_prix
        print("le nouveau prix enregistre est  :"+ self.prix_option)


    def setTVA(self, new_tva):
        """ methode qui permet de modifier la tva d'une option """
        self.id_tva_option = new_tva
        print("TVA:" + self.tva.getTaux())

    def __del__(self):
        """ methode qui supprime l'option courante """
        del self