import sqlite3

connect = sqlite3.connect('links.db', check_same_thread=False)
cursor = connect.cursor()
print("success")

def createDB():

    cursor.execute('''CREATE TABLE IF NOT EXISTS "users" (
        "id" INTEGER NOT NULL UNIQUE,
        "email" TEXT NOT NULL UNIQUE,
        "password" TEXT NOT NULL, 
        PRIMARY KEY("id" AUTOINCREMENT)
        );''')
    connect.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS "links" (
        "id" INTEGER UNIQUE NOT NULL,
        "user_id" INTEGER NOT NULL REFERENCES users (id),
        "link" TEXT NOT NULL,
        "shortLink" TEXT NOT NULL,
        "access" TEXT NOT NULL,
        "counter" INTEGER NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
        );''')
    connect.commit()
    