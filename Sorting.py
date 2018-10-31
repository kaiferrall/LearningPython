#bubble sort
def bubble_sort(array):
    for j in range(0, len(array)-1):
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                placeholder = array[i+1]
                array[i+1] = array[i]
                array[i] = placeholder

    return array

def selection_sort(array):
    largest = array[len(array)-1]
    for j in range(len(array)-1, 0, -1):
        for i in range(0, j):
            if array[i] > largest:
                largest = array[i]
                placeholder = array[j]
                array[j] = array[i]
                array[i] = placeholder
        largest = array[j-1]

    return array


a = [1, 3, 45, 29, 29, 9, 10, 100, 1010]
print(selection_sort(a))
print(bubble_sort(a))
