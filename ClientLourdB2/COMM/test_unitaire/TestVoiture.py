# -*- coding: utf8 -*-

import sys
sys.path.append("../classe/")

import unittest
from Voiture import *
from Modele import *
from Marque import *
from TVA import *

class TestClasseVoiture(unittest.TestCase):

    def setUp(self):

        self.marque = Marque('1','renault')
        self.marque2 = Marque('2','toyota')

        self.modele = Modele('1', 'Languna', self.marque,'test','test2')
        self.modele2 = Modele('2', 'prius', self.marque2,'test','test3')

        self.tva = TVA('1', '15', '15/06/2014')
        self.tva2 = TVA('2', '05', '15/04/2014')

        self.voitureATester = Voiture('SRVSR54801RG1', '15000', '30000', '50000', self.modele, self.tva)

    # test de recuperation du numero de serie
    def test_getNumeroSerie(self):
        self.assertEqual(self.voitureATester.GetNumeroSerie(), 'SRVSR54801RG1')

    # test de recuperation du kilometrage
    def test_getKilometrage(self):
        self.assertEqual(self.voitureATester.GetKilometrage(), '15000')

    # test qui renvoie le prix de vente de la voiture
    def test_getPrixVente(self):
        self.assertEqual(self.voitureATester.GetPrixVente(), '50000')

    # test qui renvoie le prix d'achat de la voiture
    def test_getPrixAchat(self):
        self.assertEqual(self.voitureATester.GetPrixAchat(), '30000')

    # test qui renvoie le modele de la voiture
    def test_getModele(self):
        self.assertEqual(self.voitureATester.GetModele(), self.modele)

    # Test de la modification du kilometrage
    def test_SetKilometrage(self):
        self.voitureATester.SetKilometrage('1200')
        self.assertEqual(self.voitureATester.GetKilometrage(),'1200')

    # Test qui modifie le prix d'achat de la voiture
    def test_SetPrixAchat(self):
        self.voitureATester.SetPrixAchat('6000')
        self.assertEqual(self.voitureATester.GetPrixAchat(),'6000')

    # Test qui modifie le prix de vente de la voiture
    def test_SetPrixVente(self):
        self.voitureATester.SetPrixVente('8000')
        self.assertEqual(self.voitureATester.GetPrixVente(),'8000')

    # Test qui modifie le modele de la voiture
    def test_SetModele(self):
        self.voitureATester.SetModele(self.modele2)
        self.assertEqual(self.voitureATester.GetModele(),self.modele2)

# Ceci lance le test si on execute le script
# directement.
if __name__ == '__main__':
    unittest.main()






