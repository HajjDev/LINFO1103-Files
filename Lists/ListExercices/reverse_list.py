from List import List

def reverse_list(l):
    """
    pre: `l` est une `List`
    post: retourne une nouvelle liste contenant les éléments de `l` dans l'ordre inverse
    """
    def rec(l, reversed_list):
        if l.is_empty(): return reversed_list
        return rec(l.tail(), reversed_list.concat(l.head()))

    return rec(l, List())

# Exemples :
# reverse_list([1[2[3[]]]]) → [3[2[1[]]]]
# reverse_list([]) → []