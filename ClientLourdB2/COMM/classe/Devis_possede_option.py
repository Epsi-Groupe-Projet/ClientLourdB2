#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan
#
# Created:     04/12/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Devis_possede_option :
    """
    Constructeur Devis_possede_option
    """
    def __init__(self, p_id_devis_possede_option, p_id_voiture_devis_possede_option, p_id_option_devis_possede_option):


        self.id_devis_possede_option = p_id_devis_possede_option
        self.id_voiture_devis_possede_option = p_id_voiture_devis_possede_option
        self.id_option_devis_possede_option = p_id_option_devis_possede_option


    def getDevisOption(self):

        print ("ID")
        return self.id_devis_possede_option

    def getVoitureOption(self):

        print ("Voiture ")
        return self.id_voiture_devis_possede_option

    def getOptionDevis(self):

        print("Option")
        return self.id_option_devis_possede_option



    def __del__(self):
        """ methode qui supprime l'option courante """
        del self