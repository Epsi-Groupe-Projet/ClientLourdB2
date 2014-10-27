from Tkinter import *
from Parametre import *
from MysqlDef import *
import ttk

class Fenetre():
	def __init__(self,ptitle,pconnexion):
		self.mfenetre = Tk()
		self.mconnexion = pconnexion
		self.mtitle = ptitle
		self.mfenetre.title(self.mtitle)
		self.mfenetre['bg'] = backGroundColor  # couleur de fond
		self.mdicoFrame = {}
		self.mdicoLabel = {}
		self.mdicoEntry = {}
		self.mdicoList = {}
		self.mresultat = []
		self.mcompteurEntry = 0
		for element in dicoFenetre[ptitle]:
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
				self.AjoutLabel(element[1],frameParent,element[3],element[4],element[5],element[6])

			if element[0] == 'Entry':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]
				self.mresultat.append(None)
				self.AjoutEntry(element[1],frameParent,self.mresultat[self.mcompteurEntry],element[3],element[4],element[5])
				self.mcompteurEntry += 1

			if element[0] == 'ListeDeroulante':
				if element[2] == None:
					frameParent = self.mfenetre
				else:
					frameParent = self.mdicoFrame[element[2]]
				self.mresultat.append(None)
				requete = "SELECT libelle_"+element[2].lower()+" FROM "+element[2].lower()
				resultat = executeRequete(self.mconnexion,requete)
				self.AjoutListeDeroulante(element[1],frameParent,self.mresultat[self.mcompteurEntry],resultat,element[3],element[4])

	def AfficherFenetre(self):
		self.mfenetre.mainloop()

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

	def AjoutEntry(self,plibelle, pfather, ptextvariable, pside, pdx, pdy):
		self.mdicoEntry['plibelle'] = Entry(pfather, textvariable = ptextvariable, bg = backGroundColor, fg = fgColor)
		self.mdicoEntry['plibelle'].focus_set()
		self.mdicoEntry['plibelle'].pack(side = pside, padx = pdx, pady = pdy)

	def AjoutListeDeroulante(self,plibelle,pfather,ptextvariable, pliste,pside,pstate):
		self.mdicoList[plibelle] = ttk.Combobox(pfather, textvariable = ptextvariable, values = pliste, state = pstate)
		self.mdicoList[plibelle].pack(side = pside)





