import sqlite3
from hashlib import sha256
from typing import List, Tuple, Optional

def init_db():
    con = sqlite3.connect("Student.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXIST student(
                id INTEGER PRIMARY KEY,
                std_id TEXT UNIQUE,
                fullname TEXT NOT NULL, 
                course TEXT,
                section TEXT,
                dob TEXT,
                gender TEXT,
                mobile TEXT)""")

    