# Task 3.3
# Author: SAMPLE CODE
# Date: 25/03/2021
# version: 1

import csv
import pymongo


def import_to_nosql(filename):
    with open(filename, 'r') as f:
        client = pymongo.MongoClient()
        for row in csv.reader(f, delimiter="\t"):
            record = {}
            headers = ['Serial_No', 'Name', 'Type',
                       'Purchase_Price', 'Selling_Price', 'Quantity']
            for i in range(len(headers)):
                record[headers[i]] = row[i]
            # Insert into MongoDB
            client['OUTLETS']['GEM'].insert_one(record)


client = pymongo.MongoClient()
client.drop_database('OUTLETS')
import_to_nosql('INVENTORY_SERIAL.txt')
