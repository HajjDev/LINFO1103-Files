# Regular mergeSort Algorithm
def merge(array, low, mid, high):
    placement = array[:]
    
    i = low
    j = mid + 1
    for k in range(low, high + 1):
        if i > mid: array[k] = placement[j]; j += 1
        elif j > high: array[k] = placement[i]; i += 1
        elif placement[i] <= placement[j]: array[k] = placement[i]; i += 1
        else: array[k] = placement[j]; j += 1

# ----------------------------------------------------------
# Other way to do the merge function but with left and right
# ----------------------------------------------------------
def merge(left, right):
    i, j = 0, 0
    merged_lst = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]: merged_lst.append(left[i]); i += 1
        else: merged_lst.append(right[j]); j += 1
        
    while i < len(left):  merged_lst.append(left[i]); i += 1
    while j < len(right): merged_lst.append(right[j]); j += 1
    
    return merged_lst
        
def merge_sort(array, low, high):
    if low >= high: return array
    
    mid = (low + high) // 2
    merge_sort(array, low, mid)
    merge_sort(array, mid + 1, high)
    merge(array, low, mid, high)
    
    return array

print(merge_sort([3, 1, 9, 10, 0], 0, 4))