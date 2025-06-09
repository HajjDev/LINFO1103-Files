from List import List

def drop(l, n):
    """
    pre: `l` est une instance de la classe List, `n` est un entier ≥ 0
    post: retourne une nouvelle List contenant les éléments de `l` sans les `n` premiers,
          ou une List vide si `n` ≥ longueur de `l`
    """
    if l.is_empty(): return List()
    
    if n <= 0: return drop(l.tail(), n - 1).concat(l.head())
    return drop(l.tail(), n - 1)

# Exemples d'utilisation de la fonction drop avec la classe List :

# l = List(3).concat(2).concat(1)  # l → [1[2[3[]]]]

# drop(l, 0) → [1[2[3[]]]]
# drop(l, 1) → [2[3[]]]
# drop(l, 2) → [3[]]
# drop(l, 3) → []
# drop(l, 4) → []

# l_vide = List()
# drop(l_vide, 2) → []