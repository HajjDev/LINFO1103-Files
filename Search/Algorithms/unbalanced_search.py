# UnbalancedSearch - Divided by 3
def unbalanced_search(array, key, low, high):
    if low > high: return -1
    
    cut = low + (high - low) // 3
    if array[cut] == key: return cut
    if array[cut] > key: return unbalanced_search(array, key, low, cut - 1)
    
    return unbalanced_search(array, key, cut + 1, high)

data = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "date",
    5: "fig",
    6: "grape",
    7: "kiwi"
}

print(unbalanced_search(data, 'kiwi', 1, 7))