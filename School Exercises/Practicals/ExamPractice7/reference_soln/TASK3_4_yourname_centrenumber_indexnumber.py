# Task 3.4
# Author: SAMPLE CODE
# Date: 25/03/2021
# version: 1

import pymongo

def verify_data_in(dbname, collname):
    client = pymongo.MongoClient()
    cursor = client[dbname][collname].find({})
    for rec in cursor:
        if not verify_row(rec):
            print(f'Deleting record:')
            for key, value in rec.items():
                print(f'{key}: {value}')
            client[dbname][collname].delete_one({'Serial_No': rec['Serial_No']})

def verify_row(rec):
    if not is_ok_serialno(rec['Serial_No']) \
            or not is_ok_name(rec['Name']) \
            or not is_ok_qty(rec['Quantity']):
        return False
    return True
   

def is_ok_serialno(sn):
    return (len(sn) == 4
            and sn[0].isdigit()
            and sn[1].isalpha()
            and sn[2].isalpha()
            and sn[3].isdigit()
            )

def is_ok_name(name):
    for char in name:
        if not (char.isdigit() or char.isalpha() or char == ' '):
            return False
    return True

def is_ok_qty(qty):
    try:
        qty = int(qty)
    except:
        return False
    else:
        if not qty >= 0:
            return False
    return True

verify_data_in('OUTLETS', 'GEM')
