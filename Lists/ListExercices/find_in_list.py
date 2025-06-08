from List import List

def find_in_list(l, e, k):
    """
    pre: `l` est une `List`
    pre: `e` est un élément éventuellement présent dans la liste `l` et différent de `None`
    pre: `k` est un entier tel que `k` > 0
    post: renvoie la sous-liste de `l` débutant à la `k`-ième occurrence de `e` dans `l`.
          Si `e` apparaît moins de `k` fois dans la liste `l`, renvoie une `List` vide.
    """
    pass

# Exemples :
# find_in_list([1[2[3[2[4[]]]]]], 2, 1) → [2[3[2[4[]]]]]
# find_in_list([1[2[3[2[4[]]]]]], 2, 2) → [2[4[]]]
# find_in_list([1[2[3[2[4[]]]]]], 2, 3) → []
