'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 27/11/2020

Week 8 - SQLite and Python 
'''

import sqlite3


connection = sqlite3.connect("Test_Database.db") # no spaces allowed!


cursor = connection.cursor()

# Adding a Record - Must be in same order as schema for data entry
sql_command = """INSERT INTO students (student_number, student_name)
              VALUES (33289,"Joe Bloggs"),
              (234536,"Jane Smith");"""

cursor.execute(sql_command)

connection.commit