def quick_sort(array):
    lte_pivot, gt_pivot = [], []
    pivot = array.pop()

    for i in range(len(array)):
        if array[i] > pivot:
            gt_pivot.append(array[i])
        else:
            lte_pivot.append(array[i])

    lte_pivot, gt_pivot = quick_sort(lte_pivot), quick_sort(gt_pivot)
    return lte_pivot + [pivot] + gt_pivot