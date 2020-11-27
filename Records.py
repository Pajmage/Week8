'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 27/11/2020

ePortfolio Task 1 - Using Python and Sqlite 3, create a 3 record table and query it 
'''
import sqlite3

def Add_Records():
    '''
    Add 3 records to the River_Details table
    '''
    connection = sqlite3.connect("Rivers_Database.db")
    cursor = connection.cursor()
    sql_command = """INSERT INTO River_Details (River_ID, River_Name, River_Length, Rapids_Grade)
              VALUES (001, "River Wear", 12.15, 3),
              (002, "River Tees", 5.65, 2),
              (003, "River Tyne", 6.7, 4);"""
    cursor.execute(sql_command)
    connection.commit()
