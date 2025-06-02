def filter_list(l, predicate):
    """
    pre: `l` est une `List`
    pre: `predicate` est une fonction booléenne
    post: retourne une nouvelle liste contenant uniquement les éléments pour lesquels predicate retourne True
    """
    pass

# Exemples :
# filter_list([1[2[3[4[]]]]], lambda x: x % 2 == 0) → [2[4[]]]
# filter_list([1[3[5[]]]], lambda x: x > 5) → []
