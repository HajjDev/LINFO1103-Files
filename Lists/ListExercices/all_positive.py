from List import List

def all_positive(l):
    """
    pre: `l` est une `List` contenant des nombres
    post: retourne True si tous les éléments sont positifs, False sinon
    """
    if l.is_empty(): return True
    
    if l.head() < 0: return False
    return all_positive(l.tail())

# Exemples :
# all_positive([1[2[3[]]]]) → True
# all_positive([-1[2[3[]]]]) → False