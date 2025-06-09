from List import List

def insert_at(l, e, n):
    """
    pre: `l` est une `List`
    pre: `n` >= 0
    pre: `e` est un élément non None
    post: retourne une nouvelle liste contenant `e` inséré à l'indice `n`
    """
    if l.is_empty(): return List(e)
    
    if n == 0: return l.concat(e)
    return insert_at(l.tail(), e, n - 1).concat(l.head())

# Exemples :
# insert_at([3[2[1[]]]], 9, 1) → [3[9[2[1[]]]]]
# insert_at([2[1[]]], 5, 2) → [2[1[5[]]]]