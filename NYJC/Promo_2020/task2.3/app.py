#Dependencies
from flask import Flask
from flask import url_for, request, render_template, redirect

#App
app = Flask(__name__)


#Utilities
def parseMovieData(filename):
    with open(filename) as f:
        lines = [line.rstrip("\n").split(",") for line in f]
        headers = lines.pop(0)

        result = []
        for line in lines:
            row = {}
            for i in range(len(headers)):
                key, value = headers[i], line[i]
                if key in ("Audience score %", "Rotten Tomatoes %"):
                    value = int(value)
                elif key in ("Profitability", "Worldwide Gross"):
                    if key == "Worldwide Gross":
                        value = value.replace("$", "")
                    value = float(value)
                row[key] = value
            result.append(row)
        return result

def insertSort(inputarray: list, sortCriteria: str):
    allCriteria = {"P": "Profitability", "A": "Audience score %", "G": "Worldwide Gross"}
    if sortCriteria not in allCriteria.keys():
        print("Invalid sort critera, must be P, A or G")
    else:
        sortCriteria = allCriteria[sortCriteria]

        result = [inputarray[0]]
        for i in range(len(inputarray)-1):
            e = inputarray[i+1]
            if e[sortCriteria] < result[0][sortCriteria]:
                result.insert(0, e)
            elif e[sortCriteria] >= result[i][sortCriteria]:
                result.insert(i+1, e)
            else:
                for j in range(i):
                    if result[j][sortCriteria] <= e[sortCriteria] < result[j+1][sortCriteria]:
                        result.insert(j+1, e)
                        break
        return result


#Routing
@app.route("/")
def root():
    return render_template("index.html")


@app.route("/sort", methods=["POST"])
def sort():
    criteria = request.form["Criteria"].strip().upper()
    movies = parseMovieData("movies.csv")
    
    global sortedMovies
    sortedMovies = insertSort(movies, criteria)

    if sortedMovies:
        return redirect("/movies")
    else:
        return redirect("/")

@app.route("/movies")
def movies():
    return render_template("movies.html", sortedMovies=sortedMovies)


#Run
app.run()