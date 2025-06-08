def linear_sort(array):
    min_element = min(array)
    max_element = max(array)
    
    placement = [0] * ((max_element - min_element) + 1)
    for j in range(len(array)):
        key = array[j]
        placement[key - min_element] += 1
        
    i = 0
    for j in range(min_element, max_element + 1):
        count = placement[j - min_element]
        while count > 0:
            array[i] = j
            i += 1
            count -= 1
    
    return array

print(linear_sort([2, 2, 0, 1, 5]))