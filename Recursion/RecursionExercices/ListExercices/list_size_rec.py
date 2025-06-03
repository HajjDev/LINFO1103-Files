#! /usr/bin/python3

from List import List

def length_rec(l: List):
    """
    Calcule la taille d une liste par récursion
    pre: -
    post: retourne la taille de la liste `l`
    """
    if l.is_empty():
        return 0

    return 1 + length_rec(l.tail())



#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(3)
l = l.concat(2)
l = l.concat(1)

if not length_rec(l) == 5:
    print(length_rec(l))
    print("Erreur : liste " + str(l) + " est de longueur 5.")