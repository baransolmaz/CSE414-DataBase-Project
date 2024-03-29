import mysql.connector

def initialize_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DataBase_414",
    )

    cursor = mydb.cursor()
    create_database(cursor)
    create_table(cursor,mydb)

    return mydb, cursor

def create_database(cursor):
    cursor.execute("SHOW DATABASES")
    temp = cursor.fetchall()
    databases = [item[0] for item in temp]
    if "event_management" not in databases:
        cursor.execute("CREATE DATABASE event_management")

    cursor.execute("USE event_management")
    print("DATABASE CONNECTED")

def create_table(cursor,conn):
    print("TABLE CONTROL")
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]

    if "Speaker" not in tables:
        cursor.execute("""CREATE TABLE Speaker(
            speaker_id INT PRIMARY KEY AUTO_INCREMENT,
            speaker_name VARCHAR(50),
            event_id INT NULL,
            topic VARCHAR(50)
         )""")
        conn.commit()
        addSpeaker(cursor, conn)

    if "Report" not in tables:
        cursor.execute("""CREATE TABLE Report(
            report_id INT PRIMARY KEY AUTO_INCREMENT,
            details VARCHAR(200)
         )""")
        conn.commit()
        createProcedure1(cursor, conn)
        addReport(cursor,conn)
        
    if "Venue" not in tables:
        cursor.execute("""CREATE TABLE Venue(
            venue_id INT PRIMARY KEY AUTO_INCREMENT,
            venue_name VARCHAR(50),
            address VARCHAR(100),
            capacity INT
         )""")
        conn.commit()
        createProcedure2(cursor, conn)
        addVenue(cursor, conn)
        
    if "Organizer" not in tables:
        cursor.execute("""CREATE TABLE Organizer(
            organizer_id INT PRIMARY KEY AUTO_INCREMENT,
            organizer_name VARCHAR(50),
            event_id INT NULL
         )""")
        conn.commit()
        createProcedure3(cursor, conn)
        addOrganizer(cursor,conn)
        
    if "Staff" not in tables:
        cursor.execute("""CREATE TABLE Staff(
            staff_id INT PRIMARY KEY AUTO_INCREMENT,
            staff_name VARCHAR(50),
            age INT,
            event_id INT NULL
         )""")
        conn.commit()
        addStaff(cursor, conn)

    if "Attendee" not in tables:
        cursor.execute("""CREATE TABLE Attendee(
            attendee_id INT PRIMARY KEY AUTO_INCREMENT,
            attendee_name VARCHAR(50),
            age INT,
            ticket_quantity INT NULL
         )""")
        conn.commit()
        addAttendee(cursor, conn)
        
    if "Ticket" not in tables:
        cursor.execute("""CREATE TABLE Ticket(
            ticket_id INT PRIMARY KEY AUTO_INCREMENT,
            event_id INT NULL,
            event_name VARCHAR(50) NULL,
            event_date DATE NULL,
            venue_id INT NULL,
            venue_name VARCHAR(50) NULL,
            attendee_id INT NULL
         )""")
        conn.commit()
        addTicket(cursor, conn)
        
    if "Event" not in tables:
        cursor.execute("""CREATE TABLE Event(
            event_id INT PRIMARY KEY AUTO_INCREMENT,
            event_name VARCHAR(50),
            organizer_id INT NULL,
            venue_id INT NULL,
            ticket_quantity INT,
            staff_quantity INT,
            speaker_id INT NULL,
            report_id INT NULL,
            date DATE 
         )""")
        conn.commit()
        addEvent(cursor, conn)
        
    print("TABLES CREATED")
    alter_event_table_query = """
    ALTER TABLE Event
    ADD CONSTRAINT fk_event_venue FOREIGN KEY (venue_id) REFERENCES Venue(venue_id),
    ADD CONSTRAINT fk_event_organizer FOREIGN KEY (organizer_id) REFERENCES Organizer(organizer_id),
    ADD CONSTRAINT fk_event_speaker FOREIGN KEY (speaker_id) REFERENCES Speaker(speaker_id),
    ADD CONSTRAINT fk_event_report FOREIGN KEY (report_id) REFERENCES Report(report_id)
    """

    alter_organizer_table_query = """
    ALTER TABLE Organizer
    ADD CONSTRAINT fk_organizer_event FOREIGN KEY (event_id) REFERENCES Event(event_id)
    """

    alter_ticket_table_query = """
    ALTER TABLE Ticket
    ADD CONSTRAINT fk_ticket_event FOREIGN KEY (event_id) REFERENCES Event(event_id),
    ADD CONSTRAINT fk_ticket_venue FOREIGN KEY (venue_id) REFERENCES Venue(venue_id),
    ADD CONSTRAINT fk_ticket_attendee FOREIGN KEY (attendee_id) REFERENCES Attendee(attendee_id)
    """

    alter_staff_table_query = """
    ALTER TABLE Staff
    ADD CONSTRAINT fk_staff_event FOREIGN KEY (event_id) REFERENCES Event(event_id)
    """

    alter_speaker_table_query = """
    ALTER TABLE Speaker
    ADD CONSTRAINT fk_speaker_event FOREIGN KEY (event_id) REFERENCES Event(event_id)
    """
    
    cursor.execute("SHOW CREATE TABLE Event")
    event_table_definition = cursor.fetchone()[1]
    if "fk_event_venue" not in event_table_definition:
        cursor.execute(alter_event_table_query)
        addTrigger1(cursor,conn)
        addTrigger2(cursor, conn)
        addTrigger3(cursor, conn)
        addTrigger4(cursor, conn)
        addTrigger6(cursor, conn)

    cursor.execute("SHOW CREATE TABLE Organizer")
    organizer_table_definition = cursor.fetchone()[1]
    if "fk_organizer_event" not in organizer_table_definition:
        cursor.execute(alter_organizer_table_query)
        
    cursor.execute("SHOW CREATE TABLE Ticket")
    ticket_table_definition = cursor.fetchone()[1]
    if "fk_ticket_event" not in ticket_table_definition:
        cursor.execute(alter_ticket_table_query)

    cursor.execute("SHOW CREATE TABLE Staff")
    staff_table_definition = cursor.fetchone()[1]
    if "fk_staff_event" not in staff_table_definition:
        cursor.execute(alter_staff_table_query)
        addTrigger5(cursor, conn)
    
    cursor.execute("SHOW CREATE TABLE Speaker")
    speaker_table_definition = cursor.fetchone()[1]
    if "fk_speaker_event" not in speaker_table_definition:
        cursor.execute(alter_speaker_table_query)
    
    print("FOREIGN KEYS ADDED")
    
    if "AttendeeView" not in tables:
        createView1(cursor,conn)
    
    if "StaffView" not in tables:
        createView2(cursor, conn)
    
    if "SpeakerView" not in tables:
        createView3(cursor, conn)
        
    if"SpeakerInfo" not in tables:
        createView4(cursor, conn)
        
    if "TicketView" not in tables:
        createView5(cursor, conn)
    print("VIEWS ADDED")
    print("PROCEDURES ADDED")

def addVenue(cursor, conn):
    cursor.callproc("AddVenue",["Room 1","Block A, Floor 1",300])
    cursor.callproc("AddVenue",["Room 2", "Block A, Floor 2", 150])
    cursor.callproc("AddVenue",["Room 3", "Block A, Floor 3", 100])
    cursor.callproc("AddVenue",["Kartal", "Istanbul,Kartal", 200])
    cursor.callproc("AddVenue",["Pendik", "Istanbul,Pendik", 150])
    cursor.callproc("AddVenue",["Kartal 2", "Istanbul,Kartal", 20])
    cursor.callproc("AddVenue",["Room 7", "Block B, Floor 1", 60])
    cursor.callproc("AddVenue",["Room 8", "Block B, Floor 2", 90])
    conn.commit()

def addSpeaker(cursor, conn):
    cursor.execute("INSERT INTO Speaker(speaker_name,event_id,topic) values(%s,%s,%s)",
                   ("Ahmet",2, "History"))
    cursor.execute("INSERT INTO Speaker(speaker_name,event_id,topic) values(%s,%s,%s)",
                   ("Mehmet",1,"Math"))
    cursor.execute("INSERT INTO Speaker(speaker_name,event_id,topic) values(%s,%s,%s)",
                   ("Ayşe", 5, "Science"))
    cursor.execute("INSERT INTO Speaker(speaker_name,event_id,topic) values(%s,%s,%s)",
                   ("Ali", 6, "Human Rights"))
    cursor.execute("INSERT INTO Speaker(speaker_name,event_id,topic) values(%s,%s,%s)",
                   ("Yakup", 7, "Justice"))
    cursor.execute("INSERT INTO Speaker(speaker_name,event_id,topic) values(%s,%s,%s)",
                   ("Talha", 8, "Economy"))
   
    conn.commit()
    
def addReport(cursor, conn):
    cursor.callproc("AddReport", ["Good"])
    cursor.callproc("AddReport", ["Nice"])
    cursor.callproc("AddReport", ["Terrible..."])
    cursor.callproc("AddReport", ["Amazing."])
    cursor.callproc("AddReport", ["DO NOT TRY AT HOME"])
    conn.commit()

def addOrganizer(cursor, conn):
    cursor.callproc("AddOrganizer",["Baran",None])
    cursor.callproc("AddOrganizer",["Hüseyin",None])
    cursor.callproc("AddOrganizer",["Killa",None])
    cursor.callproc("AddOrganizer",["Hakan",None])
    cursor.callproc("AddOrganizer",["Bay K.",None])
    conn.commit()
    
def addAttendee(cursor, conn):
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 1", 18, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 1", 22, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 2", 17, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 3", 16, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 4", 21, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 5", 28, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 6", 34, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 7", 31, 0))
    cursor.execute("INSERT INTO Attendee(attendee_name,age,ticket_quantity) values(%s,%s,%s)",
                   ("Attendee 8", 32, 0))

    conn.commit()

def addStaff(cursor, conn):
    cursor.execute("INSERT INTO Staff(staff_name,age,event_id) values(%s,%s,%s)",
                   ("Staff 1",25,None))
    cursor.execute("INSERT INTO Staff(staff_name,age,event_id) values(%s,%s,%s)",
                   ("Staff 2",20,None))
    cursor.execute("INSERT INTO Staff(staff_name,age,event_id) values(%s,%s,%s)",
                   ("Staff 3",30,None))
    cursor.execute("INSERT INTO Staff(staff_name,age,event_id) values(%s,%s,%s)",
                   ("Staff 4",26,None))
    cursor.execute("INSERT INTO Staff(staff_name,age,event_id) values(%s,%s,%s)",
                   ("Staff 5",19,None))

    conn.commit()

def addEvent(cursor, conn):
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 1",1,1,150,15, 1,None,"2023-06-26"))
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 2",1,2,100,20, 2,None,"2023-07-22"))
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 3",1,3,60,10, 2,None,"2023-06-15"))
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 4",3,None,300,50, 1,None,"2023-08-26"))
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 5",2,4,20,5, 3,None,"2023-10-21"))
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 6",3,5,50,10, 4,None,"2023-07-12"))
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 7",4,5,40,15, 5,None,"2023-06-5"))
    cursor.execute("INSERT INTO Event(event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                   ("Event 8",3,4,30,12, 6,None,"2023-11-09"))

    conn.commit()
    
def addTicket(cursor, conn):
    for i in range(5):
        cursor.execute("INSERT INTO Ticket(event_id,event_name,event_date,venue_id,venue_name,attendee_id) values(%s,%s, %s,%s, %s, %s)",
                       (2, "Event 2", "2023-07-22",2, "Room 2",1))
    conn.commit()

def dropAllDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DataBase_414",
    )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    temp = cursor.fetchall()
    dbs = [item[0] for item in temp]
    if "event_management" in dbs:
        cursor.execute("DROP DATABASE event_management")
    print("DATABASE DROPPED")

def addTrigger1(cursor, conn):
    cursor.execute("""CREATE TRIGGER check_capacity_trigger 
            BEFORE INSERT ON Event
            FOR EACH ROW
            BEGIN
                DECLARE venue_capacity INT;
    
            SELECT capacity INTO venue_capacity
            FROM Venue
            WHERE venue_id = NEW.venue_id;
            
            IF NEW.ticket_quantity > venue_capacity THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ticket quantity exceeds venue capacity';
            END IF;
            END;""")
    conn.commit()

def addTrigger2(cursor, conn):
    cursor.execute("""CREATE TRIGGER check_future_date_trigger
                BEFORE INSERT ON Event
                FOR EACH ROW
                BEGIN
                    IF NEW.date <= CURDATE() THEN
                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Event date must be in the future';
                    END IF;
                END;""")
    conn.commit()

def addTrigger3(cursor, conn):
    cursor.execute("""CREATE TRIGGER check_month_until_event_delete_trigger
                BEFORE DELETE ON Event
                FOR EACH ROW
                BEGIN
                    IF OLD.date <= DATE_ADD(CURDATE(), INTERVAL 1 MONTH) THEN
                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Event must be at least one month away';
                    END IF;
                END;""")
    conn.commit()

def addTrigger4(cursor, conn):
    cursor.execute("""CREATE TRIGGER check_ticket_quantity_trigger
                BEFORE UPDATE ON Event
                FOR EACH ROW
                BEGIN
                    IF NEW.ticket_quantity < 0 THEN
                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No Ticket';
                    END IF;
                END;""")
    conn.commit()

def addTrigger5(cursor, conn):
    cursor.execute("""CREATE TRIGGER check_staff_age_trigger
                BEFORE UPDATE ON Staff
                FOR EACH ROW
                BEGIN
                    IF OLD.age < 22 THEN
                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Staff age must be at least 22.';
                    END IF;
                END;""")
    conn.commit()

def addTrigger6(cursor, conn):
    cursor.execute("""CREATE TRIGGER check_staff_quantity_trigger
                BEFORE UPDATE ON Event
                FOR EACH ROW
                BEGIN
                    IF NEW.staff_quantity < 0 THEN
                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No Need For Staff';
                    END IF;
                END;""")
    conn.commit()

def createView1(cursor, conn):
    cursor.execute("""CREATE VIEW AttendeeView AS
                SELECT event_id,event_name,organizer_id,venue_id,ticket_quantity,speaker_id,date
                FROM Event;""")
    conn.commit()
    
def createView2(cursor, conn):
    cursor.execute("""CREATE VIEW StaffView AS
                SELECT event_id,event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,date
                FROM Event;""")
    conn.commit()

def createView3(cursor, conn):
    cursor.execute("""CREATE VIEW SpeakerView AS
                SELECT event_id,event_name,organizer_id,venue_id,speaker_id,date
                FROM Event 
                WHERE speaker_id IS NULL;""")
    conn.commit()

def createView4(cursor, conn):
    cursor.execute("""CREATE VIEW SpeakerInfo AS
            SELECT Speaker.*,Event.event_name,Event.date
            FROM Speaker,Event
            WHERE Speaker.event_id = Event.event_id;""")
    conn.commit()

def createView5(cursor, conn):
    cursor.execute("""CREATE VIEW TicketView AS
            SELECT Ticket.*,Speaker.speaker_name,Speaker.topic
            FROM Ticket,Speaker
            WHERE Speaker.event_id = Ticket.event_id;""")
    conn.commit()

def createProcedure1(cursor,conn):
    cursor.execute("""CREATE PROCEDURE AddReport(IN Info VARCHAR(200))
                    BEGIN
                        INSERT INTO Report(details) values(Info);
                    END;""")
    conn.commit()

def createProcedure2(cursor, conn):
    cursor.execute("""CREATE PROCEDURE AddVenue(IN name VARCHAR(50),IN addr VARCHAR(100),IN cap INT)
                    BEGIN
                        INSERT INTO Venue(venue_name,address,capacity) values(name,addr,cap);
                    END;""")
    conn.commit()

def createProcedure3(cursor,conn):
    cursor.execute("""CREATE PROCEDURE AddOrganizer(IN name VARCHAR(50),IN id INT)
                    BEGIN
                        INSERT INTO Organizer(organizer_name,event_id) values(name,id);
                    END;""")
    conn.commit()
