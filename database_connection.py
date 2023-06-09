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


def create_table(cursor,conn):
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]

    if "report" not in tables:
        cursor.execute("""CREATE TABLE report(
            report_id INT PRIMARY KEY AUTO_INCREMENT,
            details VARCHAR(200),
         )""")
        
    if "venue" not in tables:
        cursor.execute("""CREATE TABLE venue(
            venue_id INT PRIMARY KEY AUTO_INCREMENT,
            venue_name VARCHAR(50),
            address VARCHAR(100),
            capacity INT,
         )""")
        addVenue(cursor, conn)
        
    if "ticket" not in tables:
        cursor.execute("""CREATE TABLE ticket(
            ticket_id INT PRIMARY KEY AUTO_INCREMENT,
            event_id INT,
            event_name VARCHAR(50),
            event_date DATE,
            venue_id INT,
            venue_name VARCHAR(50)
         )""")
        
    if "speaker" not in tables:
        cursor.execute("""CREATE TABLE speaker(
            speaker_id INT PRIMARY KEY AUTO_INCREMENT,
            speaker_name VARCHAR(50),
            event_id INT,
            topic VARCHAR(50)
         )""")
        
    if "organizer" not in tables:
        cursor.execute("""CREATE TABLE organizer(
            organizer_id INT PRIMARY KEY AUTO_INCREMENT,
            organizer_name VARCHAR(50),
            event_id INT,
         )""")
        
    if "attendee" not in tables:
        cursor.execute("""CREATE TABLE attendee(
            attendee_id INT PRIMARY KEY AUTO_INCREMENT,
            attendee_name VARCHAR(50),
            age INT,
            ticket_id INT,
         )""")
        
    if "staff" not in tables:
        cursor.execute("""CREATE TABLE staff(
            staff_id INT PRIMARY KEY AUTO_INCREMENT,
            staff_name VARCHAR(50),
            age INT,
            event_id INT
         )""")
    
    if "event" not in tables:
        cursor.execute("""CREATE TABLE event(
            event_id INT PRIMARY KEY AUTO_INCREMENT,
            event_name VARCHAR(50),
            organizer_id INT,
            organizer_name VARCHAR(50),
            venue_id INT,
            venue_name VARCHAR(50),
            ticket_quantity INT,
            speaker_id INT,
            speaker_name VARCHAR(50),
            report_id INT,
            date DATE
         )""")


def login(cursor, data):
    cursor.execute(f"""SELECT * FROM users WHERE email = '{data["email"]}' 
                       AND password = '{data["password"]}' """)

    if cursor.fetchone() != None:
        return True
    return False


def addVenue(cursor, conn):

    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Room 1","Block A, Floor 1",300))
    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Room 2", "Block A, Floor 2", 150))
    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Room 3", "Block A, Floor 3", 100))
    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Kartal", "Istanbul,Kartal", 200))
    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Pendik", "Istanbul,Pendik", 150))
    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Kartal 2", "Istanbul,Kartal", 20))
    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Room 7", "Block B, Floor 1", 60))
    cursor.execute("INSERT INTO venue(venue_name,address,capacity) values(%s,%s,%s)",
                   ("Room 8", "Block B, Floor 2", 90))
    conn.commit()
    
    
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
