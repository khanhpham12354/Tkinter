import sqlite3 as sql
import os

data = {}
path = os.path.dirname(__file__)+"\\data_user.db";

con = sql.connect(path);
with con:
    cur = con.cursor();
    cur.execute("SELECT* FROM customer")
    rows  = cur.fetchall();
    print(rows)
    for i in range(0,len(rows)):
        data[rows[i][1]] = rows[i][2];
    print(data)