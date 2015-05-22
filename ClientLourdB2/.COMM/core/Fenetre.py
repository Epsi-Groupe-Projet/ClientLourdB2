from Tkinter import *
from Parametre import *
from MysqlDef import *
from PIL import Image, ImageTk
import Function
import ttk

class Fenetre():
	def __init__(self,ptitle,pconnexion,pprecedentResult):
		self.mfenetre = Tk()
		#taille souhaite de la fenetre
		w = 400
		h = 400
		#pour centrer la fenetre
		#taille de l'ecran
		ws = self.mfenetre.winfo_screenwidth()
		hs = self.mfenetre.winfo_screenheight()
		#calcul la position de la fenetre
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		#applique la position
		self.mfenetre.geometry("+%d+%d" % (x, y))

		self.mconnexion = pconnexion
		self.mtitle = ptitle
		self.mfenetre.title(self.mtitle)
		self.mfenetre['bg'] = backGroundColor  # couleur de fond
		self.mdicoFrame = {}
		self.mdicoLabel = {}
		self.mdicoEntry = {}
		self.mdicoList = {}
		self.mdicoButton = {}
		self.mdicoImage = {}
		self.mcompteurEntry = 0
		self.mdicoResult = {}
		self.mprecedentResult = pprecedentResult
		self.mdicoResult['listResultEntry'] = []
		self.resultatButton = None
		self.mnextFenetre = None


		for element in dicoFenetre[self.mtitle]:
			if element[0] == 'Frame':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]
				self.AjoutFrame(element[1],frameParent,element[3],element[4],element[5],element[6],element[7])

			if element[0] == 'Label':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]

				if element[3] == '#Selected#':
					element[3] = self.mprecedentResult['selectedButton']
				self.AjoutLabel(element[1],frameParent,element[3],element[4],element[5],element[6])

			if element[0] == 'Entry':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]
				var = StringVar()
				self.mdicoResult['listResultEntry'].append(var)
				self.AjoutEntry(element[1],frameParent,self.mdicoResult['listResultEntry'][self.mcompteurEntry],element[3],element[4],element[5],element[6])
				self.mcompteurEntry += 1

			if element[0] == 'ListeDeroulante':
				if element[1] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[1]]
				requete = "SELECT "+element[2]+" FROM "+element[3]
				resultat = executeRequete(self.mconnexion,requete)
				var = StringVar()
				self.mdicoResult['listResultEntry'].append(var)
				self.AjoutListeDeroulante(element[1],frameParent,self.mdicoResult['listResultEntry'][self.mcompteurEntry],resultat,element[4],element[5])
				self.mcompteurEntry += 1

			if element[0] == 'ListeDynamiqueButton':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]
				requete = "SELECT " + element[3] + " FROM " + element[4]
				if element[5] != None:
					if element[5] == '#SelectedButton#':
						element[5] = self.mprecedentResult['selectedButton']
					requete += " WHERE id_" + element[4] + "_"+ element[4] + " IS " + element[5]
				print requete
				resultats = executeRequete(self.mconnexion,requete)
				for resultat in resultats:
					self.AjoutButton(element[1]+";"+resultat[0],frameParent,resultat[0],Function.FonctionQuiFoutRien,TOP,5,5,element[6])

			if element[0] == 'Button':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]
				self.AjoutButton(element[1],frameParent,element[3],element[4],element[5],element[6],element[7],element[8])

			if element[0] == 'Image':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]
				self.AjoutImage(element[1],frameParent,element[3])
				
	def AfficherFenetre(self):
		self.mfenetre.mainloop()

	def GetTitre(self):
		return self.mtitle

	def GetFenetre(self):
		return self.mfenetre

	def GetFrame(self,plibelle):
		return self.mdicoFrame[plibelle]

	def AjoutFrame(self, plibelle, pfather, pborderW, prelief,pdx,pdy,pside):
		self.mdicoFrame[plibelle] = Frame(pfather,borderwidth = pborderW, relief = prelief)
		self.mdicoFrame[plibelle].pack(side = pside, padx = pdx, pady = pdy)


	def AjoutLabel(self,plibelle, pfather, ptext,	pside, pdx, pdy):
		self.mdicoLabel[plibelle] = Label (pfather, text = ptext)
		self.mdicoLabel[plibelle].pack(side = pside, padx = pdx, pady = pdy)	

	def AjoutEntry(self,plibelle, pfather, ptextvariable,pshow, pside, pdx, pdy):
		self.mdicoEntry[plibelle] = Entry(pfather, textvariable = ptextvariable,show = pshow, bg = backGroundColor, fg = fgColor)
		self.mdicoEntry[plibelle].pack(side = pside, padx = pdx, pady = pdy)

	def AjoutListeDeroulante(self,plibelle,pfather,ptextvariable, pliste,pside,pstate):
		self.mdicoList[plibelle] = ttk.Combobox(pfather, textvariable = ptextvariable, values = pliste, state = pstate)
		self.mdicoList[plibelle].pack(side = pside)

	def AjoutButton(self,plibelle,pfather,ptext,pcommand,pside,pdx,pdy,pnextFenetre):
		self.mdicoButton[plibelle] = Button(pfather,text = ptext, command = lambda: self.ExecuterFonction(pcommand,pnextFenetre,ptext))
		self.mdicoButton[plibelle].pack(side = pside,padx = pdx, pady = pdy)

	def AjoutImage(self,plibelle,pfather,ppath):
		image = Image.open(ppath)
		self.mdicoImage[plibelle] = ImageTk.PhotoImage(image)
		zoneImage = Label(pfather, image = self.mdicoImage[plibelle])
		zoneImage.pack()

	def ExecuterFonction(self,function,pnextFenetre,pselectedButton):
		resultat = function(self.mdicoResult,self.mconnexion)
		if resultat != False:
			self.resultatButton = resultat
			self.mnextFenetre = pnextFenetre
			self.mdicoResult['selectedButton'] = pselectedButton
			self.Close()
		else:
			self.resultatButton = None


	def GetResultatButton(self):
		return self.resultatButton

	def GetDicoResult(self):
		return self.mdicoResult

	def GetNextFenetre(self):
		return self.mnextFenetre

	def Close(self):
		self.mfenetre.destroy()
