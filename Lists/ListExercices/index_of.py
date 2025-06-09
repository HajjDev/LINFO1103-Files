from List import List

def index_of(l, e):
    """
    pre: `l` est une `List`
    pre: `e` est un élément quelconque
    post: retourne l’indice (0-indexé) de la première occurrence de `e` dans `l`.
          Si `e` n’est pas présent, retourne -1.
    """
    def rec(l, e, occs):
        if l.is_empty(): return -1

        if l.head() == e: return occs
        return rec(l.tail(), e, occs + 1)

    return rec(l, e, 0)

# Exemples :
# index_of([4[3[2[1[]]]]], 2) → 2
# index_of([4[3[2[1[]]]]], 5) → -1
# index_of([], 3) → -1