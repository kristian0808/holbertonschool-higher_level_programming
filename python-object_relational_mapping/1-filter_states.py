#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

# Create a connection to the database
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",  # replace with your host name
        port=3306,  # add port
        user=argv[1],  # replace with your username
        passwd=argv[2],  # replace with your password
        database=argv[3],  # replace with your database name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch all the rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the connection
    cursor.close()
    db.close()
