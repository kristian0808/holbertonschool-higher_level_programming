#!/usr/bin/python3
import MySQLdb

conn = MySQLdb.connect(
    host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM hbtn_0e_0_usa ORDER BY id")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
