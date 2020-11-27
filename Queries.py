'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 27/11/2020

ePortfolio Task 1 - Using Python and Sqlite 3, create a 3 record table and query it 
'''

import sqlite3

def Select_All():
    connection = sqlite3.connect("Rivers_Database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM River_Details;")
    results = cursor.fetchall()
    print(results)

    print("*"*50)
    print("Query Results")
    print("*"*50)

    for row in results:
    # row[0] returns the first column in the query (student_number),
    # row[1] returns student_rep name
        print('{0} : {1}, {2}, {3} '
                .format(row[0], row[1], row[2], row[3]))

    print("*"*50)
    print("End of query.")
    print("*"*50)

def Select_Hard():
    connection = sqlite3.connect("Rivers_Database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM River_Details WHERE Rapids_Grade > 3;")
    results = cursor.fetchall()
    print(results)

    print("*"*50)
    print("Query Results")
    print("*"*50)

    for row in results:
        print('{0} : {1}, {2}, {3} '
                .format(row[0], row[1], row[2], row[3]))

    print("*"*50)
    print("End of query.")
    print("*"*50)