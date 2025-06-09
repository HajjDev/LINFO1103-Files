from List import List

def split_at(l, e):
    """
    pre: `l` est une `List`
    pre: `e` est un élément
    post: retourne une paire de listes `[left, right]` où :
          - `left` contient les éléments de `l` avant la première occurrence de `e`
          - `right` contient `e` et tout ce qui le suit
          Si `e` n’est pas trouvé, `left` = `l` et `right` = []
    """
    def search_right(l, e):
        if l.is_empty(): return List()
        if l.head() == e: return l
        return search_right(l.tail(), e)
    
    def search_left(l, e, passed):
        if l.is_empty(): return List()
        if l.head() == e: passed = True
        if not passed: return search_left(l.tail(), e, passed).concat(l.head())
        return search_left(l.tail(), e, passed)
    
    left_split = search_left(l, e, False)
    right_split = search_right(l, e)
    return [left_split, right_split]

# Exemples :
# split_at([1[2[3[4[]]]]], 3) → [[1[2[]]], [3[4[]]]]
# split_at([1[2[3[4[]]]]], 1) → [[], [1[2[3[4[]]]]]]
# split_at([1[2[3[]]]], 5) → [[1[2[3[]]]], []]