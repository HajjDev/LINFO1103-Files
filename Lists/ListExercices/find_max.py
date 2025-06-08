from List import List

def find_max(l):
    """
    pre: `l` est une `List` non vide contenant des éléments comparables
    post: retourne le plus grand élément de la liste
    """
    if l.is_empty():
        return None
    def rec(l, candidat):
        if l.is_empty():
            return candidat

        if l.head() > candidat:
            return rec(l.tail(), l.head())
        
        return rec(l.tail(), candidat)
    
    return rec(l, candidat = float('-inf'))

# Exemples :
# find_max([3[7[2[9[]]]]]) → 9
# find_max([5[]]) → 5
# find_max([]) → None
