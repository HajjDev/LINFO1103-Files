from List import List

def length(l):
    """
    pre: `l` est une `List`
    post: retourne le nombre d’éléments dans la liste
    """
    if l.is_empty(): return 0
    return 1 + length(l.tail())

# Exemples :
# length([1[2[3[]]]]) → 3
# length([]) → 0