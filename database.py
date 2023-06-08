import mysql.connector


def initialize_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DataBase_414",
    )

    cursor = mydb.cursor()
    create_database(cursor)
    create_table(cursor)

    return mydb, cursor


def create_database(cursor):
    cursor.execute("SHOW DATABASES")
    temp = cursor.fetchall()
    databases = [item[0] for item in temp]

    if "event_management" not in databases:
        cursor.execute("CREATE DATABASE event_management")

    cursor.execute("USE event_management")


def create_table(cursor):
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]

    if "users" not in tables:
        cursor.execute("""CREATE TABLE users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstName VARCHAR(100),
            lastName VARCHAR(100),
            password VARCHAR(30),
            email VARCHAR(100) UNIQUE,
            gender VARCHAR(1),
            age INT,
            address VARCHAR(200)
         )""")


def login(cursor, data):
    cursor.execute(f"""SELECT * FROM users WHERE email = '{data["email"]}' 
                       AND password = '{data["password"]}' """)

    if cursor.fetchone() != None:
        return True
    return False


def register(cursor, conn, data):
    print(data)

    cursor.execute(f"""INSERT INTO users values( 
        NULL,
        '{data["firstName"]}', 
        '{data["lastName"]}', 
        '{data["password"]}', 
        '{data["email"]}', 
        '{data["gender"]}', 
        '{data["age"]}', 
        '{data["address"]}'
    )""")

    conn.commit()
