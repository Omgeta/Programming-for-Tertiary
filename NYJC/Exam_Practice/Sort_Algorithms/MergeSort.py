def merge_sort(array):
    def merge(left, right):
        sorted = []
        while left and right:
            element = right.pop(0) if left[0] > right[0] else left.pop(0)
            sorted.append(element)
        return sorted + left + right

    if len(array) > 1:
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]

        left, right = merge_sort(left), merge_sort(right)
        return merge(left, right)
    else:
        return array