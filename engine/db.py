import sqlite3

conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor() # cursor object is used to interact with the database

query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

query="INSERT INTO sys_command VALUES(null,'Visual Studio Code','C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
cursor.execute(query)
conn.commit()


# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
# cursor.execute(query)


# query="INSERT INTO web_command VALUES(null,'Excali','https://excalidraw.com/')"
# cursor.execute(query)
# conn.commit()
