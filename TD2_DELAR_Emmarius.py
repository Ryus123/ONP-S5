import numpy as np
import random 


"""Exercice 1"""

###----------1 Créer le vecteur x 
#x= np.array([1,2,3,4,5])
#print(x)

###----------2Type et longueur de x
#print("x est de type {} et à pour longueur {}".format(x.dtype, x.size))

###----------3 Extraire la 1er et la dernière valeur
#print("La 1er valeur du vecteur est {} et la dernière valeur du vecteur est {}".format(x[0], x[-1]))

###----------4 Extraire les 3 premiers éléments et les stocker dans un verteur que l'on nommera "a"
#a = np.array(x[:3])
#print(a)

###----------5 Extraire le 1er, 2e et 5e elements du vecteur dans un vecteur b

def ext_array():
    res = np.array([])
    for i in [0,1,4]:
        res = np.append(res, x[i])
    return res

#b= ext_array()
#print(b)

###----------6 Additionner 10 au vecteur x, puis multiplier le résultat par 2.
#print((x+10)*2)

###----------7 Effectuer l'addition de a et de b, commenter le résultat

#print(a+b)  #---> Addition de terme à terme

###----------8 Effectuer la multiplication "x*a", commenter le résultat
#print(a*x) #---> Erreur sur la dimensions des vecteurs

###---------9 Récupérer les multiples de 2 et les stocker dans un vecteur "ind", puis conserver uniquement les multiples de 2 de x
### dans un vecteur "mult_2"

#ind = np.logical_and(x%2==0, x%2==0)
#print(ind)

#mult_2 = x[ind]
#print(mult_2)

###--------- 10 Afficher les elements de x qui sont superieurs à 3 ou multiples de 2

#ind_2 = np.logical_or(x>3, x%2==0)
#print(x[ind_2])

###--------- 11 créer un vecteur y de dimension 6 dont le 1er element est la valeur NaN et les éléments suivants sont générés de maniere aléatoire,

#y= np.array([])
#y = np.append([np.NaN], random.sample(range(0, 30), 5)) #---> ou np.arange(0, 30, nb_pas) valeur test : [nan  6. 20.  9. 14. 11.]
#print(y)

###--------- 12 Calculer la somme des elements de x
#print("Somme de x : {}, Somme de y : {} (avec nansum() : {}".format(x.sum(), y.sum(), np.nansum(y))) #---> utiliser np.nansum() pour y


"""EXercice 2"""

###1. Créer la matrice A

a = np.array([[-3, 5, 6],[-1, 2, 2], [1, -1, -1]])
#print(a)

###2.  Afficher la dimension de 𝐴, son nombre de colonnes, son nombre de lignes et sa longueur.
#print("La matrice A possède {} colonnes, {} lignes et, est de longueur {}".format(a.shape[0], a.shape[1], a.size))

###3. Extraire la seconde colonne de 𝐴, puis la première ligne.
#print(a[0,1])

###4. Extraire la sous-matrice de dimension 2×2 du coin inférieur de A
A2 = np.array([a[1, 1:],a[2,1:]])
#print(A2)

###5.  Calculer la somme des colonnes puis des lignes de A
#print("La somme des colonnes de A vaut : {} et la somme des lignes de A vaut : {}".format(np.sum(a, axis=0), np.sum(a, axis=1 )))

###6.  Afficher la diagonale de A
#print("La diagonale de A est : {}".format(np.diag(a)))

###7.  Rajouter le vecteur transposer [1 2 3] à droite de la matrice 𝐴 et stocker le résultat dans un objet appelé B
b = np.array( [np.append(a[0], 1),np.append(a[1], 2),np.append(a[2], 3)] )
#print(b)

###8.  Retirer le quatrième vecteur de B
#print(b[0:,:3])

###9.  Retirer la première et la troisième ligne de B
#print(b[1])

###10. Ajouter le scalaire 10 à A
a+= 10
print(a)