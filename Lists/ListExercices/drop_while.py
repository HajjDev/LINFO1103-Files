from List import List

def drop_while(l, predicate):
    """
    pre: `l` est une `List`
    pre: `predicate` est une fonction booléenne
    post: retourne la sous-liste à partir du premier élément qui ne vérifie pas `predicate`
    """
    if l.is_empty(): return List()
    
    if predicate(l.head()): return drop_while(l.tail(), predicate)
    
    return l

# Exemples :
# drop_while([1[2[3[4[]]]]], lambda x: x < 3) → [3[4[]]]
# drop_while([1[1[1[]]]], lambda x: x == 1) → []