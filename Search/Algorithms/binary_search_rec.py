# Recursive Binary Search
def binary_search_rec(array, key, low, high):
    if low > high: return -1
    
    mid = (low + high) // 2
    if array[mid] == key: return mid
    elif array[mid] > key: return binary_search_rec(array, key, low, mid)
    else: return binary_search_rec(array, key, mid + 1, high)
    
data = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "date",
    5: "fig",
    6: "grape",
    7: "kiwi"
}

print(binary_search_rec(data, 'kiwi', 1, 7))