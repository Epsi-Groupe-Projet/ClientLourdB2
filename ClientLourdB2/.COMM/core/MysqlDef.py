import MySQLdb

def executeRequete(connexion,requete):

    # on demande un curseur

    curseur = connexion.GetConnexion().cursor()

    # Selection de la base si elle est specifier dans la connexion

    if connexion.GetDbName() is not None:
        # Selection de la base
        dbName = connexion.GetDbName()
        requeteDb = "USE "+ dbName +" ; " 

        curseur.execute(requeteDb)

    # execute la requete SQL sur la connexion

    try:
        curseur.execute(requete)

        
    except MySQLdb.OperationalError,message:

        # Suivi

        print "Erreur : {0}, pour la requete: {1}".format(message, requete)
        return False

    finally:

        connexion.GetConnexion().commit()
        try:
            tab = curseur.fetchall()
        except MySQLdb.ProgrammingError:
            return False
        else:
            return tab

# Fonction qui test l'existance d'une bd puis la cree si elle n'existe pas

def existanceBd(connexion,nameBd):
    # Test si la base de donne existe

    try: 
        requete = "SHOW DATABASES LIKE '"+nameBd+"' ;"
        result = executeRequete(connexion,requete)

        # Test de l'existance de la table puis creation sinon

        if not result :

            #suivi

            print "La Base de donnee suivante est inexistante : "+nameBd
            requete = "CREATE DATABASE "+nameBd+";"
            executeRequete(connexion,requete)

            #suivi

            print "La Base de donnee suivante a etait cree : "+nameBd
            connexion.ConnexionBd(nameBd)
        else:
            print "La Base de donnee suivante existe deja : "+nameBd
            connexion.ConnexionBd(nameBd)

    except MySQLdb.OperationalError,message: 

        print "Erreur : {0}".format(message)

# Fonction qui test l'existance d'une table et la cree si elle n'existe pas

def existanceTable(connexion, nameTable, columnTable):

    # Test si la table existe

    try: 
        requete = "SELECT * FROM information_schema.tables WHERE table_name = \'"+nameTable+"\'"
        result = executeRequete(connexion,requete)

        # Test de l'existance de la table puis creation sinon

        if not result:

            # Suivi

            print "La table suivante est inexistante : "+nameTable

            # Creation de la requette pour la creation de la table

            requete = "CREATE TABLE "+nameTable+" "
            requete = requete + '('
            for column in columnTable:
                for champ in column:
                    requete = requete + ' ' + champ
                requete = requete + ', '

            # En suprime la , en trop
            requete = requete[:-2]
            requete = requete + ')'


            # Execution
            executeRequete(connexion,requete)
            print "La table suivante a etait cree : "+nameTable
        
        else:

            # Suivi

            print "La table suivante existe deja : "+nameTable
            

    except MySQLdb.OperationalError,message: 

        print "Erreur : {0}".format(message)