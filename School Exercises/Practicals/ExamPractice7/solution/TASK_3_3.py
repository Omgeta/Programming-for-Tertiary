import pymongo


def export_to_nosql(filepath: str):
    with open(filepath, "r") as f:
        client = pymongo.MongoClient()
        db = client["OUTLETS"]
        coll = db["GEM"]
        for line in f:
            data = line.strip("\n").split("\t")
            record = {
                "Serial_No": data[0],
                "Name": data[1],
                "Type": data[2],
                "Purchase_Price": float(data[3]),
                "Selling_Price": float(data[4]),
                "Quantity": int(data[5])
            }
            coll.insert_one(record)


export_to_nosql("../INVENTORY_SERIAL.txt")
