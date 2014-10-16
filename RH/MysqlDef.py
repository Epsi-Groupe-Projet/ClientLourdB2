import MySQLdb

def executeRequete(connexion,requete):

    # execute une requete

    # on demande un curseur

    curseur = connexion.cursor()

    # execute la requete SQL sur la connexion

    try:
        curseur.execute(requete)

        connexion.commit()

    except MySQLdb.OperationalError,message:

        print "Erreur : {0}, pour la requete: {1}".format(message, requete)

    finally:
        return curseur