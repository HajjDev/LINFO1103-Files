from List import List

def remove_all(l, e):
    """
    pre: `l` est une `List`
    post: retourne une nouvelle liste dans laquelle toutes les occurrences de `e` ont été supprimées
    """
    if l.is_empty(): return List()
    
    if l.head() == e: return remove_all(l.tail(), e)
    return remove_all(l.tail(), e).concat(l.head())

# Exemples :
# remove_all([1[2[1[3[]]]]], 1) → [2[3[]]]
# remove_all([5[5[5[]]]], 5) → []