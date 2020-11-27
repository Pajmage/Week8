import sqlite3


# Connect to the database
connection = sqlite3.connect("Test_Database.db")

# Create a cursor
cursor = connection.cursor()

print("="*100)
print("DATABASE CREATED: Test_Database.db")
print("="*100)
