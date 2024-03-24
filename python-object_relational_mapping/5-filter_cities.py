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
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s"
        "ORDER BY cities.id", (argv[4], )
    )

    # Fetch all the rows
    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    # Close the connection
    cursor.close()
    db.close()
