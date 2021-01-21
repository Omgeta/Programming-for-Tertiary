# Task 2.1
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


# Task 2.2
def insertSort(inputarray: list, sortCriteria: str):
    allCriteria = {"P": "Profitability",
                   "A": "Audience score %",
                   "G": "Worldwide Gross"}
    if sortCriteria not in allCriteria.keys():
        print("Invalid sort critera, must be P, A or G")
    else:
        sortCriteria = allCriteria[sortCriteria]

        result = [inputarray[0]]
        for i in range(1, len(inputarray)):
            e = inputarray[i]
            if e[sortCriteria] < result[0][sortCriteria]:
                result.insert(0, e)
            elif e[sortCriteria] >= result[i][sortCriteria]:
                result.insert(i, e)
            else:
                for j in range(i):
                    if result[j][sortCriteria] <= e[sortCriteria] < result[j+1][sortCriteria]:
                        result.insert(j, e)
                        break
        return result
