from List import List

def sort(l):
    """
    pre: `l` est une instance de la classe List contenant des éléments comparables (par ex. des entiers)
    post: retourne une nouvelle List contenant les mêmes éléments que `l`, triés dans l’ordre croissant
    """
    def linear_sort(l):
        min_ele = min(l)
        max_ele = max(l)
        aux = [0] * ((max_ele - min_ele) + 1)
        
        for i in range(len(l)):
            key = l[i]
            aux[key - min_ele] += 1
        
        i = 0
        for k in range(min_ele, max_ele + 1):
            count = aux[k - min_ele]
            while count > 0:
                l[i] = k
                i += 1
                count -= 1
        
        return l
    
    def get_values(l, numbers):
        if l.is_empty(): return numbers
        
        get_values(l.tail(), numbers)
        numbers.append(l.head())
        return numbers
    
    numbers = reversed(linear_sort(get_values(l, [])))
    sorted_list = List()
    for num in numbers:
        sorted_list = sorted_list.concat(num)
        
    return sorted_list
# Exemples d'utilisation de la fonction sort avec la classe List :

# l = List(3).concat(1).concat(2)  # l → [2[1[3[]]]]
# sort(l) → [1[2[3[]]]]

# sort(List()) → []

# l2 = List(5).concat(1).concat(5).concat(3)
# l2 → [3[5[1[5[]]]]]
# sort(l2) → [1[3[5[5[]]]]]