'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 27/11/2020

Week 8 - SQLite and Python 
'''

import sqlite3
connection = sqlite3.connect("Test_Database.db")
cursor = connection.cursor()

# Execute an SQL query
# Will not print or display the results
# stores results in the cursor
cursor.execut("SELECT * FROM students;")

# Stores the results of the query to the results variable
# Must be done to display the results
# Fetches all rows the query returned
results = cursor.fetchall()
print(results)

# Prettier, more effective way to print the results:
print("="*50)
print("QUERY RESULTS")
print("="*50)

for row in results:
    # row[0] returns the first column in the query (student_number),
    # row[1] returns student_rep name
    print('{0} : {1}. '
            .format(row[0], row[1],))

print("="*50)
print("End of query.")
print("="*50)