# Adaptive BubbleSort Algorithm
def adaptive_bubble_sort(array):
    for i in range(len(array), 0, -1):
        # We add this condition to avoid unecessary iterations
        # So we can enhance the complexity
        swapped = False
        
        for j in range(1, i):
            if array[j - 1] > array[j]:
                current_value = array[j - 1]
                array[j - 1] = array[j]
                array[j] = current_value
                swapped = True
        
        if not swapped: break
    
    return array

print(adaptive_bubble_sort([4, 5, 1, 2, 3, 1]))