import csv
import sqlite3

con=sqlite3.connect("jarvis.db")
cursor=con.cursor() # cursor object is used to interact with the database

# query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
# cursor.execute(query)

# query="INSERT INTO sys_command VALUES(null,'Visual Studio Code','C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
# cursor.execute(query)
# conn.commit()


# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
# cursor.execute(query)


# query="INSERT INTO web_command VALUES(null,'Twitter','https://twitter.com/')"
# cursor.execute(query)
# conn.commit()

# query="CREATE TABLE IF NOT EXISTS contacts(id integer primary key,name VARCHAR(100),mobile_no VARCHAR(255), email VARCHAR(255) NULL)"
# cursor.execute(query)

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 33]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
# con.commit()
# con.close()


# searching query inside the contacts

query="srijan"
query=query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",('%' + query + '%', query + '%'))
results=cursor.fetchall()
print(results[0][0])