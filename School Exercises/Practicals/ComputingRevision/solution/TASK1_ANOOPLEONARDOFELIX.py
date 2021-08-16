#TASK 1.1
#Note: Alternatively, you can do all of this in one-shot but
#this way seems easier to break down the problem and reuse code

from typing import List, Dict
import csv

CSV_FILES = [
    "../rainfall-monthly-highest-daily-total.csv",
    "../rainfall-monthly-number-of-rain-days.csv",
    "../rainfall-monthly-total.csv",
    "../relative-humidity-monthly-mean.csv",
    "../surface-air-temperature-monthly-mean.csv"
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


rainfall_data = merge_csv(CSV_FILES)


with open("../combined_data.csv", "w", newline="") as f:
    fieldnames = rainfall_data[0].keys() #Get headers from the first row
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for row in rainfall_data:
        writer.writerow(row)

#TASK 1.2

#We aim to generate a dict for each year where the value will be the max for a given column
max_yearly = {}
for row in rainfall_data:
    year, month = row["month"].split("-")

    #Initialize for years not yet in
    if year not in max_yearly:
        max_yearly[year] = {
            "total_rainfall": (0, None), #Current highest is set to 0, and the month in which the highest occurs is set to None
            "maximum_rainfall_in_a_day": (0, None),
            "no_of_rainy_days": (0, None),
            "mean_rh": (0, None),
            "mean_temp": (0, None),
        }
    
    #Since we just need to look for the highest of every key
    #we can just generically apply the same comparison for every key
    #If, for example, we need to look for different comparisons such as finding the lowest for some of the keys,
    #we need to adjust this below procedure to do specific comparisons for each of the keys
    for key in max_yearly[year].keys():
        if float(row[key]) > max_yearly[year][key][0]: #if for the given factor, our current row has a higher value, we adjust the max_yearly dict
            max_yearly[year][key] = (float(row[key]), month) #Set current max

for year, row in max_yearly.items():
    print(year)
    for key in row.keys():
        print(f"\t{key}: {row[key][0]} (Month {row[key][1]})")


#TASK 1.3
#We already have the yearly data, so all we need to do is now find the max for all the years
max_overall = {
    "total_rainfall": (0, None), #Current highest is set to 0, and the year in which the highest occurs is set to None
    "maximum_rainfall_in_a_day": (0, None),
    "no_of_rainy_days": (0, None),
    "mean_rh": (0, None),
    "mean_temp": (0, None),
}

for year, row in max_yearly.items():
    for key in row.keys():
        if row[key][0] > max_overall[key][0]:
            max_overall[key] = (row[key][0], year) #Set to highest if max is found

#Max overall prints
print("Max overall:")
for key, value in max_overall.items():
    print(f"\t{key}: {value[0]} (Year {value[1]})")


#TASK 1.4
#Just modify the same code we used for max_yearly but with different values and comparisons
min_yearly = {}
for row in rainfall_data:
    year, month = row["month"].split("-")

    #Initialize for years not yet in
    if year not in min_yearly:
        min_yearly[year] = {
            "total_rainfall": (1e99, None), #1e99 here represents infinity but any large number will do
            "maximum_rainfall_in_a_day": (1e99, None),
            "no_of_rainy_days": (1e99, None),
            "mean_rh": (1e99, None),
            "mean_temp": (1e99, None),
        }
    
    for key in min_yearly[year].keys():
        if float(row[key]) < min_yearly[year][key][0]:
            min_yearly[year][key] = (float(row[key]), month) #Set current min


print("Difference:")
for year in min_yearly.keys():
    max_row, min_row = max_yearly[year], min_yearly[year]
    for key in max_row.keys():
        print(f"\t{key}: {round(max_row[key][0] - min_row[key][0], 1)} (Year {year})")







