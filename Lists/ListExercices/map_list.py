from List import List

def map_list(l, f):
    """
    pre: `l` est une `List`
    pre: `f` est une fonction prenant un élément de la liste
    post: retourne une nouvelle liste contenant les résultats de f appliquée à chaque élément de l
    """
    def rec(l, f, updated_list):
        if l.is_empty(): return updated_list
        
        operation = f(l.head())
        updated_list = rec(l.tail(), f, updated_list)
        updated_list = updated_list.concat(operation)
        return updated_list
    
    return rec(l, f, List())

# Exemples :
# map_list([1[2[3[]]]], lambda x: x * 2) → [2[4[6[]]]]
# map_list([], lambda x: x + 1) → []