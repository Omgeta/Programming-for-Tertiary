#Date: 16/8/2021
#Author: Omgeta
#Description: Program file for Task 2.2
#Version: 1.0

from typing import List, Dict
from TASK2_1 import parseMovieData

def insertSort(inputarray: List[Dict], sortCriteria: str) -> List[Dict]:
    """
    Sorts a list of movie records by a given sort criteria
    in ascending order out-of-place

    Args:
        inputarray: Unsorted list of movie records
        sortCriteria: Criteria to sort by (A, P or G)
    """
    criteria_table = {
        "A": "Audience score %",
        "P": "Profitability",
        "G": "Worldwide Gross"
    }

    sort_key = criteria_table[sortCriteria] #Get expanded form of sort criteria to index records with

    sortedarray = [inputarray[0]]
    for i in range(1, len(inputarray)):
        e = inputarray[i]
        if e[sort_key] >= sortedarray[-1][sort_key]:
            sortedarray.append(e)
        elif e[sort_key] < sortedarray[0][sort_key]:
            sortedarray.insert(0, e)
        else:
            found = False
            j = 0
            while not found:
                if sortedarray[j][sort_key] <= e[sort_key] < sortedarray[j+1][sort_key]:
                    sortedarray.insert(j+1, e)
                    found = True
                j += 1

    return sortedarray