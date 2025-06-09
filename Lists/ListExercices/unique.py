from List import List

def unique(l):
    """
    pre: `l` est une instance de la classe List contenant des éléments comparables (ex. : entiers)
    post: retourne une nouvelle List contenant les mêmes éléments que `l`,
          mais sans doublons, et en conservant leur premier ordre d’apparition
    """
    def get_values(l, unique):
        if l.is_empty(): return unique
        
        unique.add(l.head())
        return get_values(l.tail(), unique)
    
    unique = get_values(l, set())
    unique_list = List()
    for value in unique:
        unique_list = unique_list.concat(value)
    
    return unique_list
        

# Exemples d'utilisation de la fonction unique avec la classe List :

# l = List(3).concat(2).concat(1).concat(2).concat(3)  # l → [3[2[1[2[3[]]]]]]
# unique(l) → [3[2[1[]]]]

# l2 = List(1).concat(1).concat(1)  # l2 → [1[1[1[]]]]
# unique(l2) → [1[]]

# unique(List()) → []