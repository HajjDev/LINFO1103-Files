#! /usr/bin/python3

def sum_first_rec(t, k):
    """
    Calcule la somme des `k` premiers éléments de `t` par récursion
    pre: `t` un tableau (list) non vide
    pre: `k` un entier tel que 1<=`k`<=len(`t`)
    post: retourne la somme des `k` premiers éléments de `t`
    """
    if k == 1:
        return t[k - 1]

    return t[k - 1] + sum_first_rec(t, k - 1)


#Exemple de test:
if not sum_first_rec([1,2,3,5,7,9,11], 2) == 3:
    print("Erreur : 1+2 = 3")