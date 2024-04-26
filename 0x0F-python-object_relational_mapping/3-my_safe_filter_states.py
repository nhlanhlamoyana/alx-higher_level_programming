#!/usr/bin/python3
"""Module that lists all states from hbtn_0e_0_usa database."""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(hosts="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    match = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
    
