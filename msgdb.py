import os
import sqlite3

def writeid(dcmsgid, qqmsgid):
    dbpath = os.path.abspath('./msgdb.db')
    if not os.path.exists(dbpath):
        createdb = open(dbpath,'w')
        createdb.close()
        conn = sqlite3.connect(dbpath)
        c = conn.cursor()
        c.execute('''CREATE TABLE ID
               (DCID TEXT PRIMARY KEY     NOT NULL,
               QQID           TEXT    NOT NULL);''')
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("INSERT INTO ID (DCID, QQID) VALUES (?, ?)", (dcmsgid, qqmsgid))
    conn.commit()