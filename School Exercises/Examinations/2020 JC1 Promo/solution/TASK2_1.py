#Date: 16/8/2021
#Author: Omgeta
#Description: Program file for Task 2.1
#Version: 1.0

import csv
from typing import List, Dict

MOVIE_FILEPATH = "../movies.csv"

def parseMovieData(filepath: str) -> List[Dict]:
    """
    Parse movie records into a list of records

    Args:
        filepath: File to parse from
    Returns:
        List of records containing movie data for each movie
    """
    movie_data = []

    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for record in reader:
            #Set appropriate types
            record["Audience score %"] = int(record["Audience score %"])
            record["Rotten Tomatoes %"] = int(record["Rotten Tomatoes %"])
            record["Profitability"] = float(record["Profitability"])
            record["Worldwide Gross"] = float(record["Worldwide Gross"].replace("$", ""))
            
            movie_data.append(record)
    #f.close() is automatically called here

    return movie_data

movie_data = parseMovieData(MOVIE_FILEPATH)

