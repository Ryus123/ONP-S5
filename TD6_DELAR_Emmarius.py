#-----> python -m pip install openpyxl, seaborn

"""---------------------------------IMPORT------------------------------------"""
import os
from turtle import title
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

"""---------------------------------EXERCICE------------------------------------"""

#--1. Importer notes_2012 depuis "notes_etudiants.xlsx"
chemin1 = os.getcwd()+"/DataTD/DataTD6/notes_etudiants.xlsx"
Donnees1 = pd.read_excel(chemin1, "notes_2012", header=0)
notes_2012 = pd.DataFrame(Donnees1)

#--2. Afficher 6 premiere ligne + les dimensions
dim_data = notes_2012.shape
#print("6 première lignes : ",notes_2012.head(6), "\n", "Dimension du jeu de données : {} lignes et {} colonnes.".format(dim_data[0], dim_data[1]) )

#--3. Conserver note_stat
tmp= notes_2012["note_stat"]
#print(type(tmp))

#--4. Conserver num_etudiant, note_stat et note_macro
tmp_2 = notes_2012[["num_etudiant","note_stat", "note_macro"]]
#print(tmp_2)

#--5. Conserver note_stat >10

tmp_3 = notes_2012[notes_2012["note_stat"]>10]
#print("Nombre d'observation : ",len(tmp_3))

#--6. Conserver note_stat entre [10;15]

tmp_int = notes_2012[notes_2012["note_stat"]>=10]
tmp_4 =  tmp_int[tmp_int["note_stat"]<15]
#print("Nombre d'observation : ",len(tmp_4))

#--7. Doublons dans notes_2012
doublon = notes_2012.duplicated()
nb_doub = sum(doublon)
notes_2012.drop_duplicates(keep = 'first', inplace=True)
#print("Il y a {} doublon dans le jeu de donnees".format(nb_doub))

#--8. Ajout note_stat_maj
notes_2012["note_stat_maj"] = notes_2012["note_stat"]+1

#--9. Renommer year en annee
notes_2012.rename(columns={"year":"annee"}, inplace=True)

#--10.
Donnees2 = pd.read_excel(chemin1, "notes_2013", header=0)
notes_2013 = pd.DataFrame(Donnees2)

Donnees3 = pd.read_excel(chemin1, "notes_2014", header=0)
notes_2014 = pd.DataFrame(Donnees3)

Donnees4 = pd.read_excel(chemin1, "prenoms", header=0)
prenoms = pd.DataFrame(Donnees4)

#--11. Empiler les notes pour 2012, 2013 et 2014 dans notes
notes = pd.concat([notes_2012, notes_2013, notes_2014], axis=0)
#print(notes)

#--12. Joindre notes et prenoms
notes = notes.merge(prenoms, on=["num_etudiant", "annee"], how="left")
#print(notes)

#--13. Trie notes par annee decroissant
notes.sort_values(by = ["annee", "note_macro"], ascending=[False, True], inplace=True)

#--14. Apres 2012
notes["apres_2012"] = notes["annee"]>2012

#--15. Moyenne et ecart-type
#i. annuels par matière
#print(notes.loc[:, ['annee', 'note_stat','note_macro']].groupby('annee').mean())
#ii. annuels et par sexe pour chaque matière
#print(notes.loc[:, ['annee', 'note_stat','note_macro','sexe']].groupby(['annee', 'sexe']).mean())

#--16. Seaborn
sns.displot(notes, x="note_stat", hue="sexe", element="step")
plt.xlabel("Note de stat")
plt.ylabel("Nombre de notes")
plt.title("Distribution des notes de stat par sexe")
#plt.show()
