from List import List

def count_occurrences(l, e):
    """
    pre: `l` est une `List`
    pre: `e` est un élément quelconque
    post: renvoie le nombre d'occurrences de `e` dans la liste `l`
    """
    if l.is_empty(): return 0
    
    if l.head() == e: return 1 + count_occurrences(l.tail(), e)
    return 0 + count_occurrences(l.tail(), e)

# Exemples :
# count_occurrences([1[2[1[]]]], 1) → 2
# count_occurrences([3[3[3[]]]], 4) → 0