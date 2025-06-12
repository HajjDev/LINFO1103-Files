def merge(array, low, cut1, cut2, high):
    placement = array[:]
    
    i = low
    j = cut1 + 1
    h = cut2 + 1
    
    for k in range(low, high + 1):
        if i > cut1:
            if j > cut2:
                array[k] = placement[h]
                h += 1
            elif h > high or placement[j] <= placement[h]:
                array[k] = placement[j]
                j += 1
            else:
                array[k] = placement[h]
                h += 1
        elif j > cut2:
            if h > high or placement[i] <= placement[h]:
                array[k] = placement[i]
                i += 1
            else:
                array[k] = placement[h]
                h += 1
        elif h > high:
            if placement[i] <= placement[j]:
                array[k] = placement[i]
                i += 1
            else:
                array[k] = placement[j]
                j += 1
        else:
            if placement[i] <= placement[j] and placement[i] <= placement[h]:
                array[k] = placement[i]
                i += 1
            elif placement[j] <= placement[i] and placement[j] <= placement[h]:
                array[k] = placement[j]
                j += 1
            else:
                array[k] = placement[h]
                h += 1

            
    

def merge_sort(array, low, high):
    if low >= high: return array
    
    cut1 = low + ((high - low) // 3)
    cut2 = low + 2 * ((high - low) // 3)
    
    merge_sort(array, low, cut1)
    merge_sort(array, cut1 + 1, cut2)
    merge_sort(array, cut2 + 1, high)
    
    merge(array, low, cut1, cut2, high)
    return array

print(merge_sort([2, 2, 1, 4], 0, 3))                           