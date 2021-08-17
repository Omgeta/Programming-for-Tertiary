# Task 1.1
from typing import List, Dict


def parseTidalData(self, filepath: str) -> List[Dict]:
    res = []
    with open(filepath, 'r') as f:
        for line in f:
            date, time, tide, height = line.rstrip("\n").split("\t")
            res.append({
                "Date": date,
                "Time": time,
                "Tide": tide,
                "Height": float(height),
            })
    return res


t_data = parseTidalData("TIDES.TXT")

lowest_low = 1e99
highest_high = 0
for record in t_data:
    if record["Tide"] == "HIGH" and record["Height"] > highest_high:
        highest_high = record["Height"]
    elif record["Tide"] == "LOW" and record["Height"] < lowest_low:
        lowest_low = record["Height"]

print(f"Lowest tide: {lowest_low}")
print(f"Highest high: {highest_high}")


# Task 1.2
largest_range = (0, None)
smallest_range = (1e99, None)
for i in range(len(t_data) - 1):
    curr_record, next_record = t_data[i], t_data[i+1]
    if (curr_record["TIDE"] == "HIGH" and next_record["TIDE"] == "LOW") or \
            (curr_record["TIDE"] == "LOW" and next_record["TIDE"] == "HIGH"):
        height_range = abs(curr_record["Height"] - next_record["Height"])
        date = next_record["Date"]
        if height_range > largest_range[0]:
            largest_range = (height_range, date)
        elif height_range < smallest_range[0]:
            smallest_range = (height_range, date)

print(f"Largest tidal range: {largest_range[0]} on {largest_range[1]}")
print(f"Smallest tidal range: {smallest_range[0]} on {smallest_range[1]}")
