#! /usr/bin/python3

from List import List

def cum_sum(l: List):
    """
    Calcule la liste des sommes cumulées des éléments de `l`
    par itération
    pre: -
    post: retourne une liste dont le `i`^ième élément est la somme
        des `i` premiers éléments de `l`
    """
    sum_list = List()
    cum_sum_list = List()

    cum_sum = 0
    while not l.is_empty():
        cum_sum += l.head()
        sum_list = sum_list.concat(cum_sum)
        l = l.tail()

    while not sum_list.is_empty():
        cum_sum_list = cum_sum_list.concat(sum_list.head())
        sum_list = sum_list.tail()

    return cum_sum_list


#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(3)
l = l.concat(2)
l = l.concat(1)
cm = cum_sum(l)
print(cm)
if not isinstance(cm, List):
    print("Erreur avec cum_sum : doit renvoyer une List")
elif cm.is_empty():
    print("Erreur avec cum_sum : la List ne devrait pas être vide")
else:
    if not cm.head() == 1:
        print("Erreur avec cum_sum. Le premier élement devrait être 1.")
    if not cm.tail().head() == 3:
        print("Erreur avec cum_sum. Le second élément devrait être 3.")
