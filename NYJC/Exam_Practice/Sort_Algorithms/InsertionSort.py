def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        element = array.pop(i)
        if element < array[0]:
            array.insert(0, element)
        elif element > array[i-1]:
            array.insert(i, element)
        else:
            for j in range(i):
                if array[j] <= element < array[j+1]:
                    array.insert(j+1, element)
                    break
    return array
