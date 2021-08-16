#Dependencies
from flask import Flask
from flask import request, render_template, redirect
import csv
from typing import List, Dict

#App
app = Flask(__name__)

#Utils
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
    
    if sortCriteria not in criteria_table:
        print("Criteria invalid")
        return -1

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

MOVIE_FILEPATH = "../../movies.csv"
movie_data = parseMovieData(MOVIE_FILEPATH)

#Routing
@app.route("/")
def root():
    return render_template("index.html")


@app.route("/movies", methods=["POST"])
def sort():
    criteria = request.form["Criteria"].strip().upper()
    sortedMovies = insertSort(movie_data, criteria)

    if sortedMovies != -1:
        return render_template("movies.html", sortedMovies=sortedMovies)
    else:
        return redirect("/")

#Run
app.run()