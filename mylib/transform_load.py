"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/unisex_names_table.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS unisexdb")
    c.execute("CREATE TABLE unisexdb (ID, name, total, male_share, female_share, gap)")
    # insert
    c.executemany("""INSERT INTO unisexdb VALUES (?, ?, ?, ?, ?,?)""", payload)
    conn.commit()
    conn.close()
    return "unisexdb.db"
