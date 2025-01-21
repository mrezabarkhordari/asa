# main.py

import psycopg2
import os

conn = psycopg2.connect(
    dbname=os.environ.get("POSTGRES_DB"),
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    port=os.environ.get("POSTGRES_PORT"),
)

cur = conn.cursor()

cur.execute("SELECT * FROM version()")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
