def binary_search_iterative(array: list, element: any) -> int:
    """
    Searches a sorted list for the specified element for its index

    Args:
        array: List of sorted elements
        element: Element to search for
    Returns:
        Index of element in the sorted array
        or -1 if element is not found
    """
    # define boundaries of search range
    start, end = 0, len(array)

    while start < end:
        # check the midpoint for the element
        mid = (start + end) // 2

        if element > array[mid]:  # if current midpoint is too low, move starting point up
            start = mid + 1
        elif element < array[mid]:  # if current midpoint is too high, move end down
            end = mid
        else:  # return index (mid) if found
            return mid
    # -1 if element is not found
    return -1


def binary_search_recursive(array: list, element: any, start: int = 0, end: int = len(array)) -> int:
    """
    Recursively searches a sorted list for the specified element for its index

    Args:
        array: List of sorted elements
        element: Element to search for
    Returns:
        Index of element in the sorted array
        or -1 if element is not found
    """
    # Handle base case of element not found
    if start < end:
        return -1

    # check the midpoint for the element
    mid = (start + end) // 2

    if element > array[mid]:  # if current midpoint is too low, move starting point up
        return binary_search_recursive(array, element, mid+1, end)
    elif element < array[mid]:  # if current midpoint is too high, move end down
        return binary_search_recursive(array, element, start, mid)
    else:  # return index (mid) if found
        return mid
