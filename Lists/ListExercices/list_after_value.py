from List import List

def list_after_value(l, e):
    """
    pre: `l` est une `List`
    pre: `e` est un élément pouvant être dans `l`
    post: retourne la sous-liste de `l` débutant juste après la première occurrence de `e`
    """
    if l.is_empty(): return List()
    if l.head() == e: return l.tail()
    return list_after_value(l.tail(), e)

# Exemples :
# list_after_value([3[4[5[]]]], 4) → [5[]]
# list_after_value([1[2[3[]]]], 7) → []