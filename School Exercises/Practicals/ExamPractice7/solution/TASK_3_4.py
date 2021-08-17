import pymongo


def verify_coll(dbname, collname):
    client = pymongo.MongoClient()
    db = client[dbname]
    coll = db[collname]
    for record in coll.find({}):
        if not verify_row(record):
            print(f"Removing record:")
            for key, value in record.items():
                print(f"\t{key}: {value}")
            coll.delete_one(record)


def verify_row(record):
    return valid_serialno(record["Serial_No"]) \
        and valid_name(record["Name"]) \
        and valid_quantity(record["Quantity"])


def valid_serialno(sn: str):
    return len(sn) == 4 \
        and sn[0].isdigit() \
        and sn[1:3].isalpha() \
        and sn[3].isdigit()


def valid_name(name: str):
    for char in name:
        if not (char.isdigit() or char.isalpha() or char == " "):
            return False
    return True


def valid_quantity(quantity: int):
    return quantity > 0


verify_coll("OUTLETS", "GEM")
