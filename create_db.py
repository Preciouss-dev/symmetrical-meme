import sqlite3


connc = sqlite3.connect("expenses.db")

cur = connc.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY,
Date DATE,
description TEXT,
category TEXT,
price REAL)""")
            
connc.commit()
connc.close()