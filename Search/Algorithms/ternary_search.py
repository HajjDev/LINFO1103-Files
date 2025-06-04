# Regular ternarySearch
def ternary_search(array, key, low, high):
    if low > high: return -1
    
    third = (high - low) // 3
    first_cut = low + third
    second_cut = high - third
    if array[first_cut] == key: return first_cut
    if array[second_cut] == key: return second_cut
    
    if array[first_cut] > key: return ternary_search(array, key, low, first_cut - 1)
    if array[second_cut] > key: return ternary_search(array, key, first_cut, second_cut - 1)
    
    return ternary_search(array, key, second_cut + 1, high)

data = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "date",
    5: "fig",
    6: "grape",
    7: "kiwi"
}

print(ternary_search(data, 'kiwi', 1, 7))