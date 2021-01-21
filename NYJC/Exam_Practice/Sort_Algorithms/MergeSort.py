def merge(left: list, right: list) -> list:
    res = []
    while left and right:
        element = right.pop(0) if left[0] > right[0] else left[0]
        res.append(element)
    return res + left + right


def merge_sort(array: list) -> list:
    if len(array) > 1:
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]

        left, right = merge_sort(left), merge_sort(right)
        return merge(left, right)
    else:
        return array
