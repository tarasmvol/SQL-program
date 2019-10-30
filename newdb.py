import sqlite3

conn = sqlite3.connect("newdb.sqlete")
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS Names""")
cur.execute("""
CREATE TABLE Names (name TEXT, surname TEXT)""")

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.strip()
    line = line.split()
    if len(line)>=2:
        word1 = line[0]
        word2 = line[-1]
    else: continue
    row = cur.fetchone()
    cur.execute("""
    INSERT INTO Names(name, surname) VALUES (?, ?)""", (word1, word2,))
    conn.commit()

sqlstr = cur.execute("SELECT name, surname FROM Names")

for row in sqlstr:
    print(row[0], row[1])

cur.close()