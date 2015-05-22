class Modele :
    """ Classe qui permet l'ajout d'un modele de voiture """
    def __init__(self, p_id, p_libelle,p_marque_modele, p_carburant, p_puissance):
        """ Constructeur """

        self.id_modele = p_id
        self.libelle_modele = p_libelle
        self.id_marque_modele = p_marque_modele
        self.carburant_modele = p_carburant
        self.puissance_moteur_modele = p_puissance

    def GetID(self):
        """ methode qui renvoie l'id du modele de la voiture """
        return self.id_modele

    def GetLibelle(self):
        """ methode qui renvoie le nom de modele de la voiture """
        return self.libelle_modele

    def GetCarburant(self):
        """ methode qui renvoie le carburant du modele de la voiture """
        return self.carburant_modele

    def GetPuissance(self):
        """ methode qui renvoie la puissance du moteur de la voiture """
        return self.puissance_moteur_modele

    def SetCarburant(self, new_carburant):
        """ methode qui renvoie modifie le carburant du modele """
        self.carburant_modele = new_carburant

    def SetLibelle(self, new_libelle):
        """ methode qui modifie le code du modele """
        self.libelle_modele = new_libelle

    def SetPuissance(self, new_puissance):
        """ methode qui renvoie modifie la puissance du moteur """
        self.puissance_moteur_modele = new_puissance


    def GetMarqueModele(self):
        """ methode qui renvoie la marque du modele de la voiture """
        return self.id_marque_modele

    def SetMarqueModele(self, new_marque):
        """ methode qui modifie la marque du modele de la voiture """
        self.id_marque_modele = new_marque


    def __del__(self):
        """ methode qui supprime le modele """
        del self



