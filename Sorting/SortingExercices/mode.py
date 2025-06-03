#!/usr/bin/python3

def mode(values):
    """
    pre: `values` est un tableau (list) d objets comparables, len(values) >= 1
    post: renvoie le mode du tableau (ou le mode de plus petite valeur si plusieurs modes)
          le tableau `values` ne peut pas être modifié
    """
    def sort_values(values):
        """
        """
        for i in range(1, len(values)):
            key = values[i]
            j = i - 1
            
            while j >= 0 and values[j] > key:
                values[j + 1] = values[j]
                j -= 1
            
            values[j + 1] = key
        return values

    data = sort_values(values[:])
    modes = {}
    for value in data:
        if modes.get(value): modes[value] += 1
        else: modes[value] = 1
    
    max_mode = 0
    best_mode = 0
    for mode in modes:
        if modes[mode] > max_mode: max_mode = modes[mode]; best_mode = mode
        elif modes[mode] == max_mode: best_mode = mode if mode < best_mode else best_mode
    
    return best_mode

############
#Exemple de test:
if not mode([1,2,2,3,3,3,4,4,4,4]) == 4:
    print("Erreur de mode")

val = [2,1,2,2,3,3,3,3,4,4,4,4]
if not mode(val) == 3:
    print("Erreur de mode")
print(val)