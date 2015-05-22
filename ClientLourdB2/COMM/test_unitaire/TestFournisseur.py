#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan
#
# Created:     21/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
from Fournisseur import *
from CP_Ville import *

class TestClasseFournisseur(unittest,TestCase):
    #initialisation des tests
    def SetUp(self):

        self.cpVille = CP_Ville('33', 'Bordeaux')
        self.cpVille2 =CP_Ville.CP_Ville('75', 'Paris')
        self.fournisseurATester = Fournisseur('1', 'Aquifourni','0605054821', 'Andre', self.cpVille)

    # test de recuperation de la raison social du fournisseur
    def Test_getRS(self):
        self.assertEqual(self.fournisseurATester.getRS(), 'Aquifourni')

    # test de recuperation du numero de telephone du fournisseur
    def Test_getTel(self):
        self.assertEqual(self.fournisseurATester.getTel(), '0605054821')

    # test de recuperation de l'adresse du client
    def Test_getRepresentant(self):
        self.assertEqual(self.fournisseurATester.getRepresentant(), 'Andre')

    # test de recuperation de la ville du fournisseur
    def Test_getCPVille(self):
        self.assertEqual(self.fournisseurATester.getCPVille(), self.cpVille)

    # test qui permet de modifier la raison social du fournisseur
    def Test_setRS(self):
        self.fournisseurATester.SetRS('Livrapid')
        self.assertEqual(self.fournisseurATester.GetRS(),'Livrapid')

    # test qui permet de modifier la raison social du fournisseur
    def Test_setRS(self):
        self.fournisseurATester.SetRS('Livrapid')
        self.assertEqual(self.fournisseurATester.GetRS(),'Livrapid')

    # test qui permet de modifier le numero de telephone du fournisseur
    def Test_setTelephone(self):
        self.fournisseurATester.SetTelephone('0502041995')
        self.assertEqual(self.fournisseurATester.GetTelephone(),'0502041995')

    # test qui permet de modifier le nom du reprÃ©setant du fournisseur
    def Test_setRepresentant(self):
        self.fournisseurATester.SetRepresentant('Junior')
        self.assertEqual(self.fournisseurATester.GetRepresentant(),'Junior')

    # test qui permet de modifier la ville du fournisseur
    def Test_setCPVille(self):
        self.fournisseurATester.SetCPVille(self.cpVille2)
        self.assertEqual(self.fournisseurATester.GetCPVille(), self.cpVille2)

    if __name__ == '__main__':
        unittest.main()



