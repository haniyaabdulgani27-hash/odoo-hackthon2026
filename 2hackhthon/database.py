import sqlite3


def create_database():
    connection = sqlite3.connect("vehicle.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        number TEXT NOT NULL,
        model TEXT,
        status TEXT
    )
    """)

    connection.commit()
    connection.close()


create_database()
