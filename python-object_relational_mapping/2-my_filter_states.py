#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N
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

    # Execute a query with filter word
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"
                   .format(argv[4]))

    # Fetch all the rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the connection
    cursor.close()
    db.close()
