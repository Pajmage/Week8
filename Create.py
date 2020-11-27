'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 27/11/2020

ePortfolio Task 1 - Using Python and Sqlite 3, create a 3 record table and query it 
'''
import sqlite3

def Create_DB():
    '''
    Creates an initial database with a table
    '''
    connection = sqlite3.connect("Rivers_Database.db")
    cursor = connection.cursor()
    sql_command = """
    CREATE TABLE IF NOT EXISTS River_Details (
    River_ID INTEGER PRIMARY KEY,
    River_Name VARCHAR(50),
    River_Length REAL(5),
    Rapids_Grade INTEGER(1))
    """
    cursor.execute(sql_command)
    print("Table Created!")
    connection.commit()

