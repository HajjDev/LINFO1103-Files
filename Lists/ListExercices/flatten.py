from List import List

def flatten(l):
    """
    pre: `l` est une instance de la classe List
    post: retourne une liste Python contenant les mêmes éléments que `l`, dans le même ordre
    """
    def rec(l, python_list):
        if l.is_empty(): return python_list
        
        python_list.append(l.head())
        rec(l.tail(), python_list)
        return python_list

    return rec(l, [])

# Exemples d'utilisation de la fonction flatten avec la classe List :

# l = List(3).concat(2).concat(1)  # l → [1[2[3[]]]]
# flatten(l) → [1, 2, 3]

# flatten(List()) → []

# l2 = List(42)
# flatten(l2) → [42]