#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan
#
# Created:     22/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Peinture :
    """
    Classe permettant de definir la peinture d'un vehicule
    """
    def __init__(self, p_id, p_libelle_peinture, p_prix_peinture, p_tva):

        """ Constructeur """
        self.id_peinture = p_id
        self.libelle_peinture = p_libelle_peinture
        self.prix_peinture = p_prix_peinture
        self.id_tva_peiture = p_tva


    def getLibellePeinture(self):
        """ methode permettant d'acceder au nom du type de peinture courante"""
        print ("Libelle de la peinture selectionnee")
        return self.libelle_peinture

    def getPrixPeinture(self):
        """ methote qui renvoie le prix du type de peiture courante """
        print ("Prix de la peinture ")
        return self.prix_peinture

    def getTVA(self):
        """ methode qui renvoie la tva appliquee sur la peinture """
        print("TVA de la peinture")
        return self.id_tva_peiture

    def setLibelle(self, new_libelle):
        """ methode qui modifie le libelle de peinture courante """

        self.libelle_peinture = new_libelle
        print("Libelle  :"+ self.libelle_peinture)

    def setPrixPeinture(self, new_prix_peinture):
        """ methode qui modifie le prix du type de peinture courante """

        self.prix_peinture = new_prix_peinture
        print("le nouveau prix enregistre est  :"+ self.prix_peinture)

    def setTVA(self, new_tva):
        """ methode qui permet de modifier la tva """
        self.id_tva_peiture = new_tva
        print("TVA:" + self.tva.getTaux())


    def __del__(self):
        """ methode qui supprime du type de peinture """
        del self