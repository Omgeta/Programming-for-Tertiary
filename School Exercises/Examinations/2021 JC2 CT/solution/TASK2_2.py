#Date: 16/8/2021
#Author: Omgeta
#Description: Program file for Task 2.2
#Version: 1.0

from typing import List, Dict

def quickSort(inputArray: List[Dict], sortCriteria: str):
    """
    Sort a list of track records by a given sort criteria (D, E or V)
    in ascending order 

    Args:
        inputArray: Unsorted list of track records
        sortCriteria: Character representing sort criteria
    Returns:
        Sorted list of track records
    """
    criteria_table = {
        "D": "Danceability",
        "E": "Energy",
        "V": "Valence"
    }

    upperSortCriteria = sortCriteria.upper() #Always caps
    if upperSortCriteria not in criteria_table:
        return f"Invalid sort criteria {sortCriteria}. Should be one of D, E, V"
    else:
        if len(inputArray) > 1:
            expandedSortCriteria = criteria_table[upperSortCriteria]
            pivot = inputArray.pop()
            lte_pivot, gt_pivot = [], []

            for record in inputArray:
                if record[expandedSortCriteria] <= pivot[expandedSortCriteria]:
                    lte_pivot.append(record)
                else:
                    gt_pivot.append(record)

            lte_pivot, gt_pivot = quickSort(lte_pivot, sortCriteria), quickSort(gt_pivot, sortCriteria)
            return lte_pivot + [pivot] +gt_pivot
        else:
            return inputArray
