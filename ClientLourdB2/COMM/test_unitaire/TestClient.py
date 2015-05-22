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
from Client import *
from CP_Ville import *

class TestClasseClient(unittest,TestCase):
    #initialisation des tests
    def SetUp(self):

        self.cpVille = CP_Ville('33', 'Bordeaux')
        self.cpVille2 = CP_Ville('75', 'Paris')
        self.clientATester = Client('1', 'Messi', 'Lionel', '35 rue Marseille', '0608054487', 'messi@epsi.fr', self.cpVille)

     # test de recuperation du nom du client
    def Test_getNom(self):
        self.assertEqual(self.clientATester.getNom(), 'Messi')

    # test de recuperation du prenom du client
    def Test_getPrenom(self):
        self.assertEqual(self.clientATester.getprenom(), 'Lionel')

    # test de recuperation de l'adresse du client
    def Test_getAdresse(self):
        self.assertEqual(self.clientATester.getAdresse(), '35 rue Marseille')

    # test de recuperation du numero du telephone du client
    def Test_getTelephone(self):
        self.assertEqual(self.clientATester.getTelephone(), '0608054487')

    # test de recuperation de l'email du client
    def Test_getEmail(self):
        self.assertEqual(self.clientATester.getEmail(), 'messi@epsi.fr')

    # test de recuperation de la ville du client
    def Test_getCPVille(self):
        self.assertEqual(self.clientATester.getCPVille(), self.cpVille)

     # Test qui modifie le nom du client
    def Test_SetNom(self):
        self.clientATester.SetNom('Ronaldo')
        self.assertEqual(self.clientATester.GetNom(),'Ronaldo')

    # Test qui modifie le prenom du client
    def Test_SetPrenom(self):
        self.clientATester.SetPrenom('Cristiano')
        self.assertEqual(self.clientATester.GetPrenom(),'Cristiano')

    # Test qui modifie l'adresse du client
    def Test_SetAdresse(self):
        self.clientATester.SetAdresse('61 cours de la marne')
        self.assertEqual(self.clientATester.GetAdresse(),'61 cours de la marne')

    # Test qui modifie le numero de telephone du client
    def Test_SetTelephone(self):
        self.clientATester.SetTelephone('0565566556')
        self.assertEqual(self.clientATester.GetPrenom(),'0565566556')

    # Test qui modifie l'email du client
    def Test_SetEmail(self):
        self.clientATester.SetEmail('ronaldo@epsi.fr')
        self.assertEqual(self.clientATester.GetEmail(),'ronaldo@epsi.fr')

    # Test qui modifie la ville du client
    def Test_SetCPVille(self):
        self.clientATester.SetCPVille(self.cpVille2)
        self.assertEqual(self.clientATester.GetEmail(), self.cpVille2)





