#Dependencies
from flask import Flask
from flask import render_template, redirect, request
from typing import List, Dict, Tuple
import csv

#Utils
CSV_FILES = [
    "../../rainfall-monthly-highest-daily-total.csv",
    "../../rainfall-monthly-number-of-rain-days.csv",
    "../../rainfall-monthly-total.csv",
    "../../relative-humidity-monthly-mean.csv",
    "../../surface-air-temperature-monthly-mean.csv"
]

def read_csv(filepath: str) -> List[Dict]:
    """
    Read the contents of a CSV file
    and parse into a list of dictionaries
    containing the headers

    Params:
        filepath (str) - Filepath of CSV file to read from.
    Returns:
        result (list) - List of dictionaries
    """
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        result = [row for row in reader]
    return result

def merge_csv(filepaths: List[str]) -> List[Dict]:
    """
    Reads the contents of all the CSVs files
    and merges them into a single list of dictionaries
    containing all the headers.
    Note: this implementation assumes that all files have an identical order

    Params:
        filepaths (list) - List of filepaths to CSV files to merge
    Returns:
        result (list) - List of merged dictionaries
    """
    result = read_csv(filepaths[0]) #Initialize list with data from the first file
    for i in range(1, len(filepaths)): #Iterate over the remaining files
        other_data = read_csv(filepaths[i])
        for j in range(len(other_data)): #Iterate over each row in the list
            result[j].update(other_data[j]) #Update the dictionary for each month with new data
    return result

#Load in the data and manually set the values of specific columns to float/int
rainfall_data = merge_csv(CSV_FILES)

def get_display_headers(data_type: str) -> Tuple[str]:
    """
    Convert the input to the headers that we want to display
    """
    type_to_headers = {
        "rainfall": ("total_rainfall", "maximum_rainfall_in_a_day"),
        "raindays": ("no_of_rainy_days",),
        "humidity": ("mean_rh",),
        "mean_temp": ("mean_temp",)
    }
    if data_type not in type_to_headers:
        return None
    else:
        return type_to_headers[data_type]

def get_display_rows(headers: List[str]) -> List:
    """
    Get data for the given headers
    """
    result = []
    for row in rainfall_data:
        subrow = {
            "month": row["month"],
        }
        for header in headers:
            subrow[header] = row[header]
        result.append(subrow)
    return result


#Flask
app = Flask(__name__)
global err
err = None

@app.route('/')
def index():
    return render_template('index.html', err=err)

@app.route('/result', methods=['POST'])
def result():
    data_type = request.form["data_type"]
    if data_type not in ("rainfall", "raindays", "humidity", "temperature"):
        global err
        err = "Incorrect data type. Must be rainfall, raindays, humidity or temperature"
        return redirect("/")
    else:
        headers = get_display_headers(data_type)
        display_data = get_display_rows(headers)

        #this looks bad but atleast it works
        return render_template('result.html', data=display_data)


app.run()