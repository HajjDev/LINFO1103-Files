from List import List

def get_nth(l, n):
    """
    pre: `l` est une `List`
    pre: `n` >= 0
    post: retourne le n-ième élément de la liste (0 pour le premier)
    """
    if l.is_empty(): raise IndexError
    
    if n == 0: return l.head()
    return get_nth(l.tail(), n - 1)

# Exemples :
# get_nth([1[2[3[]]]], 0) → 1
# get_nth([1[2[3[]]]], 2) → 3
# get_nth([1[]], 3) → IndexError