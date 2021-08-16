#Date: 16/8/2021
#Author: Omgeta
#Description: Program file for Task 2.3
#Version: 1.0
from flask import Flask
from flask import redirect, request, render_template
import csv
from typing import List, Dict

app = Flask(__name__)
TRACK_FILEPATH = "../../top2018.csv"
global err
err = None

#Utils
def parseTrackData(filepath: str) -> List[Dict]:
    """
    Read spotify track data from a file into a list of records.

    Args:
        filepath: Path to the file to read from
    Returns:
        List of track records.
    """
    res = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        with open(filepath, "r") as f:
            for record in reader:
                record["Rank"] = int(record["Rank"])
                record["Duration_ms"] = int(record["Duration_ms"]) // 1000
                record["Danceability"] = float(record["Danceability"])
                record["Energy"] = float(record["Energy"])
                record["Speechiness"] = float(record["Speechiness"])
                record["Valence"] = float(record["Valence"])
                res.append(record)
    return res

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

track_data = parseTrackData(TRACK_FILEPATH)

@app.route("/")
def index():
    return render_template("index.html", err=err)

@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        criteria = request.form["criteria"]
        res = quickSort(track_data, criteria)

        if isinstance(res, str): #Error handling
            err = res
            return redirect("/")
        else:
            return render_template("result.html", data=res)

app.run()