import MySQLdb
import Parametre
import Initialisation
import Employe
import Ville
import Service
import Grade

connexion = Initialisation.start()

ville = Ville.Ville(None,'Paris')
ville.VilleIntoTable(connexion)
service = Service.Service(None,'Service Informatique',None)
service.ServiceIntoTable(connexion)
grade = Grade.Grade(None,'Chef de service')
grade.GradeIntoTable(connexion)
employe = Employe.Employe(None,'Yassine','Faris','1992-12-21','2500.5','20 rue Solle','','33200',ville,'0663362470','yass-faris@hotmail.fr','FAIL','Chef du departement Informatique',grade,service)
employe.EmployerIntoTable(connexion)

listNameColumn = ['id_employe','nom_employe','prenom_employe']
listParametre = ['1','Faris','Yassine']

employe.GetEmployeFromTableSQL(connexion,listNameColumn,listParametre)
