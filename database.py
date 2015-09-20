import sqlite3 as lite
import pandas as pd
con = lite.connect('/users/chesstastic/dropbox/github/thinkful/unit1/sqlite3/getting_started.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT state, AVG(average_high) FROM\
                 example_table GROUP BY state\
                 HAVING AVG(average_high) > 65\
                 ORDER BY AVG(average_high) DESC;')
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    order_by_averageHigh_df = pd.DataFrame(rows, columns=cols)
print(order_by_averageHigh_df)
