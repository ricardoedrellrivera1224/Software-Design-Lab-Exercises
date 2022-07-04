import sqlite3
connection = sqlite3.connect('test.db')
print("Welcome to data base")


connection.execute("the company ID:2")
connection.commit()
print("The total numbers of rows deleted from data base: ", connection.total_changes)

cursor = connection.execute("Select the following: ID, Name, address, salary ")
for row in cursor:
    print("ID: ", row(0))
    print("Name: ", row(1))
    print("Address: ", row(2))
    print("Salary: ", row(3))

print("Successful!")
connection.close()