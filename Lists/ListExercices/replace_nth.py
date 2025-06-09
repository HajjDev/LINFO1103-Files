from List import List

def replace_nth(l, n, e):
    """
    pre: `l` est une `List`
    pre: `n` est un entier ≥ 0
    pre: `e` est un élément non-None
    post: retourne une nouvelle liste identique à `l` sauf que le `n`-ième élément est remplacé par `e`.
          Si `n` dépasse la longueur de `l`, retourne `l` inchangée.
    """
    if l.is_empty(): return List()
    
    if n == 0: return replace_nth(l.tail(), n - 1, e).concat(e)
    return replace_nth(l.tail(), n - 1, e).concat(l.head())

# Exemples :
# replace_nth([1[2[3[]]]], 1, 9) → [1[9[3[]]]]
# replace_nth([1[2[]]], 0, 7) → [7[2[]]]
# replace_nth([1[2[]]], 3, 8) → [1[2[]]]