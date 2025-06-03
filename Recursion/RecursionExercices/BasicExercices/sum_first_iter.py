#! /usr/bin/python3

def sum_first(t, k):
    """
    Calcule la somme des `k` premiers éléments de `t` avec une boucle (= version itérative)
    pre: `t` un tableau (list) non vide
    pre: `k` un entier tel que 1<=`k`<=len(`t`)
    post: retourne la somme des `k` premiers éléments de `t`
    """
    result = 0
    
    for i in range(k):
        result += t[i]
        
    return result
        


#Exemple de test:
if not sum_first([1,2,3,5,7,9,11], 3) == 6:
    print(sum_first([1,2,3,5,7,9,11], 3))
    print("Erreur : 1+2 = 3")