# Regular BubbleSort Algorithm
def bubble_sort(array):
    for i in range(len(array), 0, -1):
        for j in range(1, i):
            if array[j - 1] > array[j]:
                current_value = array[j - 1]
                array[j - 1] = array[j]
                array[j] = current_value
    
    return array

print(bubble_sort([2, 1, 4]))
print(bubble_sort([2, 1, 7, 0, 10, 23]))