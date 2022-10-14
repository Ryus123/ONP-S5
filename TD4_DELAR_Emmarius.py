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
print(df1)
"REP : Le séparateur de champs est une virgule "

###2. À présent, importer le contenu du fichier « notes_decim.csv ». Le séparateur de champs est un point-virgule et le séparateur décimal est une virgule
chemin3 = os.getcwd()+"/DataTD/DataTD4/notes_decim.csv"
chemin4 = os.getcwd()+"/Data/notes_decim.csv"

try:
    Donnees2 = pd.read_csv(chemin3, delimiter=";")
except:
    Donnees2 = pd.read_csv(chemin4, delimiter=";")

df2 = pd.DataFrame(Donnees2)
print(df2)

###3. Importer le contenu du fichier « notes_h.csv »
chemin5 = os.getcwd()+"/DataTD/DataTD4/notes_h.csv"
chemin6 = os.getcwd()+"/Data/notes_h.csv"

try:
    Donnees3 = pd.read_csv(chemin3, delimiter=";")
except:
    Donnees3 = pd.read_csv(chemin4, delimiter=";")

df2 = pd.DataFrame(Donnees3)
print(df2)
###4. Importer le contenu du fichier « notes_h_s.csv »
