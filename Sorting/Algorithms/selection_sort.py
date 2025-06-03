# Regular SelectionSort Algorithm
def selection_sort(array):
    for i in range(len(array)):
        min_element = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_element]: min_element = j
        
        if min_element != i:
            value = array[i]
            array[i] = array[min_element]
            array[min_element] = value
    
    return array

print(selection_sort([2, 9, 1, 0, 7]))