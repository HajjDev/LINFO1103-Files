from List import List

def list_equals(l1, l2):
    """
    pre: `l1` et `l2` sont des List
    post: retourne True si les deux listes sont identiques (contenu et ordre), sinon False
    """
    if l1.is_empty() and l2.is_empty(): return True
    if l1.is_empty() or l2.is_empty(): return False
    
    if l1.head() == l2.head(): return list_equals(l1.tail(), l2.tail())
    return False

# Exemples :
# list_equals([1[2[3[]]]], [1[2[3[]]]]) → True
# list_equals([1[2[]]], [2[1[]]]) → False
# list_equals([], []) → True