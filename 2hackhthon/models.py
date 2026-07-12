import sqlite3

DATABASE = "vehicle.db"


def add_vehicle(name, number, model, status):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO vehicles (name, number, model, status)
        VALUES (?, ?, ?, ?)
        """,
        (name, number, model, status),
    )

    connection.commit()
    connection.close()


def get_vehicles():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()

    connection.close()

    return vehicles
