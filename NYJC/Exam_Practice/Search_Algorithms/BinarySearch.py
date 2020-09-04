def binary_search(array, value):
    start, end = 0, len(array)-1
    mid = (start + end)//2

    while start != end:
        if array[mid] >= value:
            end = mid
        else:
            start = mid + 1
        mid = (start + end)//2

    return mid