def linear_search(array: list, element: any) -> int:
    """
    Searches any list for the specified element for its index

    Args:
        array: List of elements
        element: Element to search for
    Returns:
        Index of the element in the array
        or -1 if the element is not found
    """
    # search through indexes
    for index in range(len(array)):
        # return index if element is found
        if array[index] == element:
            return index
    # -1 to signify that element is not included in the array
    return -1
