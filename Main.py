'''
MSc Computer Systems and Management
CSTM65 Software Engineering Principles
Author: Paul Jones
Date: 27/11/2020

ePortfolio Task 1 - Using Python and Sqlite 3, create a 3 record table and query it 
'''

import sqlite3
from Create import *
from Records import *
from Queries import *

Create_DB()
print("Database Created Successfully!")
Add_Records()
print("Records inserted Successfully!")
Select_All()
Select_Hard()   
