import sqlite3 as lite
import pandas as pd
con = lite.connect('/users/chesstastic/dropbox/github/thinkful/unit1/sqlite3/getting_started.db')
weather = ( ('New York City', 2013, 'July', 'January', 62),
            ('Boston', 2013, 'July', 'January', 59),
            ('Chicago', 2013, 'July', 'January', 59),
            ('Miami', 2013, 'August', 'January', 84),
            ('Dallas', 2013, 'August', 'January', 77),
            ('Seattle', 2013, 'July', 'January', 61),
            ('Portland', 2013, 'July', 'December', 63),
            ('San Francisco', 2013, 'September', 'December', 64),
            ('Los Angeles', 2013, 'September', 'December', 75);')          

with con:
 cur = con.cursor()
 cur.execute('DROP TABLE IF EXISTS weather, cities;')
 cur.execute('CREATE TABLE cities (name text, state text);')
 cur.execute('INSERT INTO cities (name, state) VALUES\
              ('New York City', 'NY'),
              ('Boston',        'MA'),
              ('Chicago',       'IL'),
              ('Miami',         'FL'),
              ('Dallas',        'TX'),
              ('Seattle',       'WA'),
              ('Portland',      'OR'),
              ('San Francisco', 'CA'),
              ('Los Angeles',   'CA');')
 cur.executemany('INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
 
