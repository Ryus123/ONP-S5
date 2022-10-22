from unicodedata import decimal
import numpy as np
import pandas as pd
import os
from pprint import pprint
"""-----------------------------------IMPORT----------------------------------------"""

###1. Visualiser les données présentes dans le fichier « notes.csv ». Quel est le séparateur de champs ? décimal ? Importer le contenu du fichier dans Python.
chemin1 = os.getcwd()+"/DataTD/DataTD4/notes.csv"
chemin2 = os.getcwd()+"/Data/notes.csv"

try:
    Donnees = pd.read_csv(chemin1, delimiter=",")
except:
    Donnees = pd.read_csv(chemin2, delimiter=",")

df1 = pd.DataFrame(Donnees)
#print(df1)
"REP : Le séparateur de champs est une virgule "

###2. À présent, importer le contenu du fichier « notes_decim.csv ». Le séparateur de champs est un point-virgule et le séparateur décimal est une virgule
chemin3 = os.getcwd()+"/DataTD/DataTD4/notes_decim.csv"
chemin4 = os.getcwd()+"/Data/notes_decim.csv"

try:
    Donnees2 = pd.read_csv(chemin3, delimiter=";", decimal=",")
except:
    Donnees2 = pd.read_csv(chemin4, delimiter=";", decimal=",")

df2 = pd.DataFrame(Donnees2)
#print(df2)

###3. Importer le contenu du fichier « notes_h.csv »
chemin5 = os.getcwd()+"/DataTD/DataTD4/notes_h.csv"
chemin6 = os.getcwd()+"/Data/notes_h.csv"

try:
    Donnees3 = pd.read_csv(chemin5, delimiter=";", header=None)
except:
    Donnees3 = pd.read_csv(chemin6, delimiter=";", header=None)

df3 = pd.DataFrame(Donnees3)
#print(df3)

###4. Importer le contenu du fichier « notes_h_s.csv »
chemin7 = os.getcwd()+"/DataTD/DataTD4/notes_h_s.csv"
chemin8 = os.getcwd()+"/Data/notes_h_s.csv"

try:
    Donnees4 = pd.read_csv(chemin7, delimiter=";", skiprows=1)
except:
    Donnees4 = pd.read_csv(chemin8, delimiter=";", skiprows=1)

df4 = pd.DataFrame(Donnees4)
#print(df4)

###5. Importer le contenu de la première feuille du fichier Excel « notes.xlsx »

Donnees5 = pd.read_excel("notes.xlsx", sheet_name="notes_pv")
df5 = pd.DataFrame(Donnees5)

print(df5)

###6. Importer le contenu de la seconde feuille (notes_h_s) du fichier Excel « notes.xlsx ».
Donnees6 = pd.read_excel("notes.xlsx", sheet_name="note_h_s", header=None)
df6 = pd.DataFrame(Donnees6)

#print(df6)

###7. Exporter le contenu de l’objet contenant les notes de la question précédente au format csv 

notescsv = Donnees6.to_csv("notes1.csv", sep = ',', decimal=".", index_label=None)
