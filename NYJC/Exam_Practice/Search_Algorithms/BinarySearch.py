def binary_search(array, value):
    start, end = 0, len(array)-1
    mid = (start + end) // 2

    while start != end:
        if array[mid] >= value:
            end = mid
        else:
            start = mid + 1
        mid = (start + end) // 2

    return mid

def recursive_search(array, value, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == value:
        return mid
    elif array[mid] > value:
        return recursive_search(array, value, start, mid)
    else:
        return recursive_search(array, value, mid+1, end)
