from List import List

def contains(l, e):
    """
    pre: `l` est une `List`
    post: retourne True si `e` est dans `l`, False sinon
    """
    if l.is_empty(): return False
    
    if l.head() == e: return True
    return contains(l.tail(), e)
    
# Exemples :
# contains([1[2[3[]]]], 2) → True
# contains([1[2[3[]]]], 5) → False