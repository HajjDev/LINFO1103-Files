def split_at(l, e):
    """
    pre: `l` est une `List`
    pre: `e` est un élément
    post: retourne une paire de listes `[left, right]` où :
          - `left` contient les éléments de `l` avant la première occurrence de `e`
          - `right` contient `e` et tout ce qui le suit
          Si `e` n’est pas trouvé, `left` = `l` et `right` = []
    """
    pass

# Exemples :
# split_at([1[2[3[4[]]]]], 3) → [[1[2[]]], [3[4[]]]]
# split_at([1[2[3[4[]]]]], 1) → [[], [1[2[3[4[]]]]]]
# split_at([1[2[3[]]]], 5) → [[1[2[3[]]]], []]
