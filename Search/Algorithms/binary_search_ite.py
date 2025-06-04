# Iterative binarySearch
def binary_search_ite(array, key, low, high):
    
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == key: return mid
        elif array[mid] > key: high = mid
        else: low = mid + 1
        
    return -1

data = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "date",
    5: "fig",
    6: "grape",
    7: "kiwi"
}

print(binary_search_ite(data, 'banana', 1, 7))