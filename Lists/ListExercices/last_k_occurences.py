from List import List

def last_k_occurrences(l, e, k):
    """
    pre: `l` est une `List`
    pre: `e` est un élément non-None
    pre: `k` > 0
    post: retourne la sous-liste commençant à la position de la (k-ième en partant de la fin) occurrence de `e`.
          Si `e` apparaît moins de `k` fois, retourne []
    """
    if l.is_empty():
        return List()
    
    if l.head() == e:
        k -= 1
        if k == 0:
            return l
    
    return last_k_occurrences(l.tail(), e, k)

# Exemples :
# last_k_occurrences([1[2[3[2[4[2[]]]]]], 2, 2) → [2[4[2[]]]]
# last_k_occurrences([1[2[3[2[4[]]]]]], 2, 3) → [2[3[2[4[]]]]]
# last_k_occurrences([1[2[3[]]]], 5, 1) → []
