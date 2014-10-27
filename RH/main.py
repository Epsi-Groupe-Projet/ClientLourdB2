from MySQLdb import *
from Parametre import *
from Initialisation import *
from Employe import *
from Ville import *
from Service import *
from Grade import *
from Diplome import *
from Diplome_Obtenu import *
from Fenetre import *

connexion = start()

fenetre = Fenetre('Ajout d\'un employe',connexion)
fenetre.AfficherFenetre()
