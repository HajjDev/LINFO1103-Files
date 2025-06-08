def linear_sort(array):
    min_element = min(array)
    max_element = max(array)
    
    placement = [0] * ((max_element - min_element) + 1)

    for j in range(min_element, max_element + 1):
        placement[j - min_element] = min_element - 1

    for i in range(len(array)):
        key = array[i]
        placement[key - min_element] = key

    i = 0
    for j in range(min_element, max_element + 1):
        if placement[j - min_element] >= min_element:
            array[i] = placement[j - min_element]
            i += 1
            
    return array