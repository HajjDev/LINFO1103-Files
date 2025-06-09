from List import List

def zip_lists(l1, l2):
    """
    pre: `l1` et `l2` sont des `List`
    post: retourne une nouvelle liste contenant des paires (tuples) des éléments de l1 et l2,
          jusqu'à ce que l'une des deux listes soit épuisée
    """
    def rec(l1, l2, zipped_list):
        if l1.is_empty() or l2.is_empty(): return zipped_list
        
        zipped_list = rec(l1.tail(), l2.tail(), zipped_list)
        zipped_list = zipped_list.concat((l1.head(), l2.head()))
        return zipped_list
    
    return rec(l1, l2, List())

# Exemples :
# zip_lists([1[2[3[]]]], [4[5[6[]]]]) → [(1,4)[(2,5)[(3,6)[]]]]
# zip_lists([1[2[]]], [3[]]) → [(1,3)[]