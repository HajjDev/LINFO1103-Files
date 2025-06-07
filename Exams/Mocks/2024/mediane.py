# We need to sort the list with a O(nlog(n)) algorithm and then find the mean
def mediane(liste):
    """
     Cette fonction permet de calculer la médiane d'une liste non ordonnée

     @pre:  Le paramètre liste est une liste de nombre réels

     @post: Renvoie la médiane de la liste ou None si celle-ci est vide.
    """
    def sort_algorithm(array):
        def merge_sort(array, low, high):
            if low >= high: return array
            
            mid = (low + high) // 2
            merge_sort(array, low, mid)
            merge_sort(array, mid + 1, high)
            merge(array, low, mid, high)
            
            return array
        
        def merge(array, low, mid, high):
            aux = array[:]
            i = low
            j = mid + 1
            
            for k in range(low, high + 1):
                if i > mid: array[k] = aux[j]; j += 1
                elif j > high: array[k] = aux[i]; i += 1
                elif aux[i] <= aux[j]: array[k] = aux[i]; i += 1
                else: array[k] = aux[j]; j += 1
        
        return merge_sort(array, 0, len(array) - 1)

    sorted_array = sort_algorithm(liste)
    return sorted_array[len(sorted_array) // 2] if len(sorted_array) % 2 != 0 else (sorted_array[len(sorted_array) // 2] + sorted_array[(len(sorted_array) // 2) - 1]) / 2 

print(mediane([3, 4, 2, 1, 9, 7]))