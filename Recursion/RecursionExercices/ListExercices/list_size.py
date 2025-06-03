#! /usr/bin/python3

from List import List

def length(l: List):
    """
    Calcule la taille d une liste à l aide d une boucle (version itérative)
    pre: -
    post: retourne la taille de la liste `l`
    """
    if l.is_empty():
        return 0

    length = 0
    while not l.is_empty():
        length += 1
        l = l.tail()

    return length



#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(3)
l = l.concat(2)
l = l.concat(1)

if not length(l) == 5:
    print("Erreur : liste " + str(l) + " est de longueur 5.")