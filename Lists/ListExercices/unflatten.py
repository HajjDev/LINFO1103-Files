from List import List

def unflatten(liste):
    """
    pre: `liste` est une liste Python contenant des éléments (par exemple des entiers ou des flottants)
    post: retourne une instance de la classe List contenant les mêmes éléments que `liste`, dans le même ordre
    """
    class_list = List()

    for number in liste[::-1]:
        class_list = class_list.concat(number)
    
    return class_list

# Exemples d'utilisation de la fonction unflatten avec la classe List :

# unflatten([1, 2, 3]) → [1[2[3[]]]]

# unflatten([]) → []

# unflatten([42]) → [42[]]