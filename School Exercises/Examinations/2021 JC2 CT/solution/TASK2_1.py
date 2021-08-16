#Date: 16/8/2021
#Author: Omgeta
#Description: Program file for Task 2.1
#Version: 1.0

import csv
from typing import List, Dict

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