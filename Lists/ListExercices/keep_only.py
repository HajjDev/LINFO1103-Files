from List import List

def keep_only(l, e):
    """
    pre: `l` est une `List`
    post: retourne une nouvelle liste contenant uniquement les éléments égaux à `e` dans `l`
    """
    if l.is_empty(): return List()
    
    if l.head() == e: return keep_only(l.tail(), e).concat(l.head())
    return keep_only(l.tail(), e)

# Exemples :
# keep_only([1[2[1[3[]]]]], 1) → [1[1[]]]
# keep_only([4[5[6[]]]], 3) → []