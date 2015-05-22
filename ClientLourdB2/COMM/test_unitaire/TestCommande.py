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

import unittest
from Commande_Client import *
from Voiture import *
from Modele import *
from Marque import *
from Fournisseur import *
from CP_Ville import *
from TVA import *
from Client import *
from Facture import *
from Peinture import *

class TestClasseCommandeClient(unittest,TestCase):
    #initialisation des tests
    def SetUp(self):

        self.listOption = ['25', '1', '3']
        self.listOption2 = ['5', '11', '13']

        self.marque = Marque('1','renault')
        self.marque2 = Marque('2','toyota')

        self.modele = Modele('1', 'Languna', self.marque)
        self.modele2 = Modele('2', 'prius', self.marque2)

        self.cpVille = CP_Ville('33', 'Bordeaux')
        self.cpVille2 = CP_Ville('75', 'Paris')

        self.tva = TVA('1', '15', '15/06/2014')
        self.tva2 = TVA('2', '05', '15/04/2014')

        self.facture = Facture('1', '20/04/2014','20/03/2015', self.commande, self.tva)
        self.facture2 = Facture('2', '21/10/2014','30/07/2014', self.commande2, self.tva2)

        self.voiture = Voiture('SRVSR54801RG', '1500', '3000', '5000', self.modele, self.fournisseur, self.commande)
        self.voiture2 = Voiture('SRVSR54801RG1', '15000', '30000', '50000', self.modele2, self.fournisseur2, self.commande2)

        self.peinture = Peinture('41', 'peinturama', '120')
        self.peinture2 = Peinture('1', 'belpeinture', '165')

        self.commande2 = Commande_Client('2','15/06/18', self.voiture, self.client2, self.facture2, self.peinture2, self.listOption2 )

        self.client1 = Client.Client('1','Yohan','Cabaye','32 rue epsi', '0000', 'cabaye@epsi.fr', self.cpVille)
        self.client2 = Client.Client('','Paul','Pogba','36 rue epsi', '0011', 'pogba@epsi.fr', self.cpVille2)

        self.fournisseur = Fournisseur('1', 'Aquifourni','0605054821', 'Andre', self.cpVille)
        self.fournisseur2 = Fournisseur('2', 'Livrapid','0621589636', 'Gerald', self.cpVille2)

        self.commandeATester = Commande_Client('1','02/06/18', self.voiture, self.client1, self.facture, self.peinture, self.listOption )

    # test de recuperation de la date de la commande
    def Test_getDate(self):
        self.assertEqual(self.commandeATester.getDate(), '02/06/18')

    # test de recuperation de la voiture commandee
    def Test_getVoiture(self):
        self.assertEqual(self.commandeATester.getVoiture(), self.voiture)

    # test qui renvoie le client de la commande
    def Test_getClient(self):
        self.assertEqual(self.commandeATester.getClient(), self.client1)

    # test qui renvoie la facture de la commande
    def Test_getFacture(self):
        self.assertEqual(self.commandeATester.getFacture(), self.facture)

    # test qui renvoie le le type de peinture de la voiture concernee
    def Test_getPeinture(self):
        self.assertEqual(self.commandeATester.getPeinture(), self.peinture)

    # test qui renvoie la liste des option de la voiture concernee
    def Test_getOptions(self):
        self.assertEqual(self.commandeATester.getOptions(), self.listOption)


    # Test de la modification la date de la commande
    def Test_SetDate(self):
        self.commandeATester.SetDate('12/06/2010')
        self.assertEqual(self.commandeATester.GetDate(),'12/06/2010')

    # Test qui modifie la voiture concernee
    def Test_SetVoiture(self):
        self.commandeATester.SetVoiture(self.voiture2)
        self.assertEqual(self.commandeATester.GetVoiture(), self.voiture2)

    # Test qui modifie le client de la commande
    def Test_SetClient(self):
        self.commandeATester.SetClient(self.client2)
        self.assertEqual(self.commandeATester.GetClient(), self.client2)

    # Test qui modifie la facture de la commande
    def Test_SetFacture(self):
        self.commandeATester.SetFacture(self.facture2)
        self.assertEqual(self.commandeATester.GetFacture(),self.facture2)

    # Test qui modifie le type de peinture de la voiture concernee
    def Test_SetPeinture(self):
        self.commandeATester.SetPeinture(self.peinture2)
        self.assertEqual(self.commandeATester.GetPeinture(), self.peinture2)


     # Test qui modifie la liste des options de la voiture concernee
    def Test_SetOptions(self):
        self.commandeATester.SetOptions(self.listOption2)
        self.assertEqual(self.commandeATester.GetOptions(), self.listOption2)

    if __name__ == '__main__':
        unittest.main()
