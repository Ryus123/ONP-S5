"""
TD1 python -- vendredi 16/09/2022
L3 MIASHS
@author: edelar
"""
"""
Import
"""

from datetime import datetime, time, timedelta, date


"""
Exercice 1 : ch
"""

###1. Créer deux variable a et b

from distutils.command.build_scripts import first_line_re


a= "N'allez pas croire qu'il s'agit du tonnerre"

b= "Rester là vous coûterait très cher."


###2. Afficher le nombre de caractère de la variable a puis de la variable b

#print("La variable a contient {} caractères".format(len(a)))

#print("La variable b contient {} caractères".format(len(b)))

###3. Concaténer a et b avec un . comme caractère de séparation

ab = a+"."+b
#print(ab)

###4.  Même question en choisissant une séparation permettant un retour à la ligne entre les deux phrases.

ab_v2 = a+"\n"+b

#print(ab_v2)

###5. À l’aide de la méthode appropriée, mettre en majuscules a et b

maj_a = a.upper()
maj_b= b.upper()

#print(maj_a, "\n",maj_b)

###6. À l’aide de la méthode appropriée, mettre en minuscules a et b

min_a = a.lower()
min_b= b.lower()

#print(min_a, "\n",min_b)

###7. Extraire le mot là de la chaîne b, en utilisant les indices

mot_ext1 = b[7:9]
mot_ext2 = b[-5:-1]

#print(mot_ext2)

###8. Rechercher si la sous-chaîne er est présente dans b et son nombre d’occurrence...

nb_cher = b.count("er")
nb_ton = b.count("ton")

#print("Nombre de er : {} et Nombre de ton : {}".format(nb_cher, nb_ton))

###9. "Retourner la position (indice) du premier caractère de la sous-chaîne er dans la chaîne b, puis essayer avec le caractère w."

first_er = b.find("er")
first_w = b.find("w")
#print(first_w)


###10. Remplacer les occurrences du motif a par le motif Z dans la sous-chaîne b.
new_b = b.replace("a","Z")
#print(b, "\n", new_b)

###11. Faire en sorte que dans la chaîne b tous les mots soient séparés par des virgules.

new_b2 = b.replace(" ", ",")
#print(b, "\n", new_b2)

###12. Retirer tous les caractères de ponctuation de la chaîne b, puis utiliser une méthode appropriée pour retirer les caractères blancs en début et fin de chaîne



"""
Exercice 2 : les dates
"""

###1: ....

d= datetime(2022,4, 6, 5,25,6)

#print(type(d))

annee_d= d.year
min_d = d.minute
sec_d = d.second

#print("Année : {}, Minute : {}, Seconde {}".format(annee_d, min_d, sec_d) )

###2. Ajouter 2 jours et 3 heures, retirer 25 minutes et 6 secondes à d. Stocker le résultat dans un objet appelé d1

temps1 = timedelta(2, hours=3, minutes=-25, seconds=-6)
d1 = d + temps1
#print(d1)

###3. À l’aide de la fonction appropriée, afficher la date du jour
#print("Aujourd'hui nous sommes le : ", datetime.today())

###4. Calculer la différence en jour entre la date du jour et d1. Stocker ce résultat dans une variable que vous appellerez duree. Afficher le résultat puis le type de l’objet

duree= (datetime.today() - d1)

#print(duree / timedelta(days=1), type(duree))

###5. Afficher cette différence en secondes.
print(duree.total_seconds(), type(duree))