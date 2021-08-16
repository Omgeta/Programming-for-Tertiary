def quick_sort(array: list) -> list:
    lte_pivot, gt_pivot = [], []
    pivot = array[len(array) - 1]

    for i in range(len(array) - 1):
        if array[i] <= pivot:
            lte_pivot.append(array[i])
        else:
            gt_pivot.append(array[i])

    lte_pivot, gt_pivot = quick_sort(lte_pivot), quick_sort(gt_pivot)

    return lte_pivot + [pivot] + gt_pivot
