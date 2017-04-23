#!/usr/bin/env python

import sqlite3

conn=sqlite3.connect('templog.db')

curs=conn.cursor()

print "\nEntire database content:\n"
for row in curs.execute("SELECT * FROM temps"):
    print row

conn.close()
