def parse_csv(filename):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n").split(",") for line in f]
        headers = lines.pop(0)
        result = []
        for line in lines:
            row = {}
            for i in range(len(headers)):
                row[headers[i]] = line[i]
            result.append(row)
        return result