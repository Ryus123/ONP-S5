from unicodedata import decimal
import numpy as np
import pandas as pd
import os
from pprint import pprint
"""-----------------------------------IMPORT----------------------------------------"""

###Exercice 1 : Définir le plus simplement possible v1, v2, v3, v4
v1 = np.array([5,9,1,3])
v2 = 2*np.ones(20)
v3 = np.arange(1,17)
v4 = np.arange(28,11, -2)

###Exercice 2
#3. Charger ce fichier en utilisant les fonctionnalités de pandas.
chemin1 = os.getcwd()+"/DataTD/Enquete_prog.csv"
chemin2 = os.getcwd()+"/Data/Enquete_prog.csv"

try:
    Donnees = pd.read_csv(chemin1, delimiter=";")
except:
    Donnees = pd.read_csv(chemin2, delimiter=";")

df = pd.DataFrame(Donnees)

#4. A l'aide de la fonction adaptée, afficher le nom de chaque colonne
#print(df.columns)

#5. Décrire les données (nombre d’observations, nombre de variables)
#print("Nombre d'observation : {}, Nombre de variable : {}".format(len(df.axes[0]), len(df.axes[1])))

#6. Combien y a-t-il de données manquantes pour la variable MaritalStatus ?
#print(df["MaritalStatus"].isna().sum())

#7. Compléter pour la variable Age
#print(np.round(df["Age"].describe(), decimals=2))





