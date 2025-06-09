from List import List

def cum_sum(l):
    """
    pre: `l` est une instance de la classe List contenant des entiers ou flottants
    post: retourne une nouvelle List de même longueur où chaque élément est la somme cumulée
          des éléments de `l` jusqu’à cet index
    """
    def cum_sum_rec(l, rec_sum = 0):
        if l.is_empty(): return List()
        
        rec_sum += l.head()
        return cum_sum_rec(l.tail(), rec_sum).concat(rec_sum)
    
    return cum_sum_rec(l)

# Exemples d'utilisation de la fonction cum_sum avec la classe List :

# l = List(3).concat(2).concat(1)  # l → [1[2[3[]]]]

# cum_sum(l) → [1[3[6[]]]]

# l2 = List(5).concat(-2)          # l2 → [-2[5[]]]
# cum_sum(l2) → [-2[3[]]]

# cum_sum(List()) → []
