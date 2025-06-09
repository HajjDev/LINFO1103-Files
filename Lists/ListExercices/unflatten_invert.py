from List import List

def unflatten_invert(liste):
    """
    pre: `liste` est une liste Python contenant des éléments (ex. : entiers ou flottants)
    post: retourne une instance de la classe List contenant les mêmes éléments que `liste`,
          mais dans l’ordre inverse
    """
    inverted_list = List()

    for i in range(len(liste)):
        inverted_list = inverted_list.concat(liste[i])
    
    return inverted_list

# Exemples d'utilisation de la fonction unflatten_invert avec la classe List :

# unflatten_invert([1, 2, 3]) → [3[2[1[]]]]

# unflatten_invert([]) → []

# unflatten_invert([42]) → [42[]]