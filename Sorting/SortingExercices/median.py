#!/usr/bin/python3

def median(values):
    """
    pre: `values` est un tableau (list) d objets comparables, len(values) >= 1
    post: renvoie la mesure médiane du tableau `values` sans changer l'ordre du tableau
    """
    def insertion_sort(values):
        """
        pre: `values` est un tableau (list) d objets comparables
        post: renvoie un tableau trié par ordre croissant, le tableau `values` passé en paramètre ne peut pas être modifié.
        """
        for i in range(1, len(values)):
            key = values[i]
            j = i - 1
            while j >= 0 and values[j] > key:
                values[j + 1] = values[j]
                j -= 1
            
            values[j + 1] = key
        
        return values

    data = values[:]
    insertion_sort(data)
    print(data)
    return data[len(data) // 2] if len(data) % 2 != 0 else (data[len(data) // 2] + data[(len(data) // 2) - 1]) / 2
    
print(median([9.4, 0.7, -9.0, -3.4, 3.0, 2.4, 0.3, 10.0]))