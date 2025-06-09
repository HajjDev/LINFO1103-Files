from List import List

def find_mode(l):
    """
    pre: `l` est une instance de la classe List non vide, contenant des entiers ou des flottants
    post: retourne l’élément apparaissant le plus de fois dans la liste ;
          en cas d’égalité, retourne la plus petite valeur parmi les plus fréquentes
    """
    def get_occurences(l, occurences):
        if l.is_empty(): return
        
        if occurences.get(l.head()): occurences[l.head()] += 1
        else: occurences[l.head()] = 1
        return get_occurences(l.tail(), occurences)
    
    occurences = {}
    mode = float('inf')
    minimum_value = float('-inf')
    get_occurences(l, occurences)
    for value in occurences:
        if occurences[value] >= minimum_value:
            if value < mode: minimum_value = occurences[value]; mode = value
    
    return mode
        
        
# Exemples d'utilisation de la fonction find_mode avec la classe List :

# l = List(3).concat(2).concat(1).concat(2).concat(3).concat(2)
# l → [2[3[2[1[2[3[]]]]]]
# find_mode(l) → 2

# l2 = List(5).concat(4).concat(5).concat(4)
# l2 → [4[5[4[5[]]]]]
# find_mode(l2) → 4  (égalité entre 4 et 5, on retourne le plus petit)

# l3 = List(10)
# find_mode(l3) → 10
print(find_mode(List(5).concat(4).concat(5).concat(4)))