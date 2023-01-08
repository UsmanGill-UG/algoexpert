# Simple Bubble sort - time complexity O(n) always
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

# Modified bubble sort 
def bubbleSort1(array):
    ch = True
    for i in range(len(array)):
        if ch == False:
            break
        ch = False
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                ch = True
    return array


array = [1, 2, 3]
print(bubbleSort1(array))