from List import List

def sum_list(l):
    """
    pre: `l` est une `List` contenant des nombres
    post: retourne la somme des éléments de la liste
    """
    if l.is_empty():
        return 0
    
    return l.head() + sum_list(l.tail())

# Exemples :
# sum_list([1[2[3[]]]]) → 6
# sum_list([]) → 0

l = List()
l = l.concat(1)
l = l.concat(2)
l = l.concat(3)
print(sum_list(l))