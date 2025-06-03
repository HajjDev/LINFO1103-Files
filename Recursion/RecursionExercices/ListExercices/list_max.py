#! /usr/bin/python3

from List import List

def maximum(l: List):
    """
    Calcule le maximum d une liste à l aide d une boucle (= version itérative)
    pre: `l` contient au moins un élément
    post: retourne l élément maximum de `l`
    """
    maximum = float('-inf')
    
    while not l.is_empty():
        maximum = l.head() if l.head() > maximum else maximum
        l = l.tail()
        
    return maximum




#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(3)
l = l.concat(2)
l = l.concat(1)

if not maximum(l) == 5:
    print("Erreur : le maximum de la liste " + str(l) + " est 5.")