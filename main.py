from tkinter import *
from tkinter import messagebox
from database_connection import *

mydb, cursor = initialize_connection()
#dropAllDB()
mydb.autocommit=False

class Main_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x290")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("EVENT MANAGEMENT SYSTEM")  # Pencere ismi

        organizer_button = Button(
            self.window, text="Event Organizer Login", width=46, height=3, command=Organizer_App)
        organizer_button.place(x=2, y=5)

        speaker_button = Button(
            self.window, text="Speaker Login", width=46, height=3, command=Speaker_App)
        speaker_button.place(x=2, y=75)
        attendee_button = Button(
            self.window, text="Attendee Login", width=46, height=3, command=Attendee_App)
        attendee_button.place(x=2, y=145)
        staff_button = Button(
            self.window, text="Staff/Volunteer Login", width=46, height=3, command=Staff_App)
        staff_button.place(x=2, y=215)
class Staff_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Staff-Volunteer")  # Pencere ismi
        self.entries=[]
        list_event_button = Button(self.window, text="List Events",
                                   width=12, height=3 , command=self.listEvents)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="Be Volunteer",
                                           width=12, height=3, command=self.beVolunteer)
        view_event_details_button.place(x=122, y=5)
        list_volunteer_button = Button(self.window, text="List Staff",
                                  width=12, height=3, command=self.listStaff)
        list_volunteer_button.place(x=242, y=5)
        volunteer_button = Button(self.window, text="Add Staff",
                                  width=12, height=3, command=self.addStaff)
        volunteer_button.place(x=362, y=5)
        edit_volunteer_button = Button(self.window, text="Edit Staff",
                                  width=12, height=3, command=self.editStaff)
        edit_volunteer_button.place(x=482, y=5)
        remove_volunteer_button = Button(self.window, text="Remove Staff",
                                  width=12, height=3, command=self.removeStaff)
        remove_volunteer_button.place(x=602, y=5)

    def listEvents(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM StaffView")

        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1

    def listStaff(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM Staff")

        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def removeStaff(self):
        env=StaffDialog(2)
    def addStaff(self):
        env=StaffDialog(0)
    def editStaff(self):
        env=StaffDialog(1)
    def beVolunteer(self):
        env=StaffDialog(3)
class Speaker_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Speaker")  # Pencere ismi
        self.entries = []
        list_event_button = Button(self.window, text="List Events",
                                   width=12, height=3, command=self.listEvents)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="Attend Event",
                                           width=12, height=3, command=self.attend_event)
        view_event_details_button.place(x=122, y=5)
        attend_event_button = Button(self.window, text="Change Topic",
                                     width=12, height=3, command=self.changeTopic)
        attend_event_button.place(x=242, y=5)
        view_organizer_button = Button(self.window, text="List Speakers",
                                       width=12, height=3 , command=self.listSpeakers)
        view_organizer_button.place(x=362, y=5)
        add_speaker_button = Button(self.window, text="Add Speaker",
                                       width=12, height=3, command=self.addSpeaker)
        add_speaker_button.place(x=482, y=5)

    def listEvents(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("""SELECT SpeakerView.*, Venue.venue_name, Venue.address
                  FROM SpeakerView
                  LEFT JOIN Venue ON SpeakerView.venue_id = Venue.venue_id""")

        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def attend_event(self):
        ent=CancelEventDialog(1)
    def changeTopic(self):
        ent = CancelEventDialog(2)
    def addSpeaker(self):
        ent = CancelEventDialog(3)
    def listSpeakers(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM Speaker")
        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
class Organizer_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.columnconfigure(0, weight=1)
        self.window.config(background="#9BABB8")
        self.window.title("Organizer")  # Pencere ismi

        self.entries = []
        create_event_button = Button(self.window, text="Create Event",
                                    width=12, height=3, command=self.createEvent)
        create_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="Edit Event",
                                    width=12, height=3, command=self.editEvent)
        view_event_details_button.place(x=122, y=5)
        edit_event_details_button = Button(self.window, text="Cancel Event",
                                           width=12, height=3, command=self.cancelEvent)
        edit_event_details_button.place(x=242, y=5)
        list_event_button = Button(self.window, text="List Events",
                                   width=12, height=3, command=self.listEvents)
        list_event_button.place(x=362, y=5)
        invite_speaker_button = Button(self.window, text="List Speakers",
                                    width=12, height=3 , command=self.listSpeakers)
        invite_speaker_button.place(x=482, y=5)
        invite_speaker_button = Button(self.window, text="List Venues",
                                       width=12, height=3, command=self.listVenues)
        invite_speaker_button.place(x=602, y=5)
        invite_speaker_button = Button(self.window, text="See Report",
                                       width=12, height=3, command=self.seeReport)
        invite_speaker_button.place(x=722, y=5)
        invite_speaker_button = Button(self.window, text="Add Report",
                                       width=12, height=3, command=self.addReport)
        invite_speaker_button.place(x=842, y=5)
    
    def seeReport(self):
       eny = ReportDialog(0)
    def addReport(self):
       eny = ReportDialog(1)
       
    def cancelEvent(self):
       eny = CancelEventDialog(0)
    def listEvents(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("""SELECT * FROM Event LEFT JOIN Venue ON Event.venue_id = Venue.venue_id
                  UNION
                  SELECT * FROM Event RIGHT JOIN Venue ON Event.venue_id = Venue.venue_id
                  WHERE Event.event_id IS NOT NULL""")
        
        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j),y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def listVenues(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM Venue")
        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def listSpeakers(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM SpeakerInfo")
        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def editEvent(self):
        ent=EventDialog(1)
    def createEvent(self):
        evnt=EventDialog(0)
class Attendee_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Attendee")  # Pencere ismi
        self.entries = []
        list_event_button = Button(self.window, text="List Events",
                                   width=12, height=3, command=self.listEvents)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="Buy Ticket",
                                           width=12, height=3, command=self.buyTicket)
        view_event_details_button.place(x=122, y=5)
        list_Ticket_details_button = Button(self.window, text="List All Ticket",
                                           width=12, height=3, command=self.listAllTicket)
        list_Ticket_details_button.place(x=242, y=5)
        cancel_ticket_details_button = Button(self.window, text="Cancel Ticket",
                                           width=12, height=3, command=self.cancelTicket)
        cancel_ticket_details_button.place(x=362, y=5)
        attend_event_button = Button(self.window, text="List Attendees",
                                     width=12, height=3, command=self.listAttendees)
        attend_event_button.place(x=482, y=5)
        view_organizer_button = Button(self.window, text="Add Attendee",
                                       width=12, height=3, command=self.addAttendee)
        view_organizer_button.place(x=602, y=5)

    def listEvents(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("""SELECT AttendeeView.*,Speaker.speaker_name, Speaker.topic
                  FROM AttendeeView
                  RIGHT JOIN Speaker ON AttendeeView.speaker_id = Speaker.speaker_id
                  WHERE AttendeeView.event_id IS NOT NULL""")
        
        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j),y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def listAttendees(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT DISTINCT * FROM Attendee")
        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def listAllTicket(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM TicketView")
        column_names = [desc[0] for desc in cursor.description]
        # Print the column names
        for j, column_name in enumerate(column_names):
            self.entries.append(Entry(self.window, width=10, fg='black'))
            self.entries[j].place(x=(90*(j)), y=80)
            self.entries[j].insert(END, column_name)
        i = 1
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=10, fg='black'))
                self.entries[i*len(event)+j].place(x=(90*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    def addAttendee(self):
        evnt=AttendeeDialog(0)  
    def buyTicket(self):
        evnt = AttendeeDialog(2)
    def cancelTicket(self):
        evnt = AttendeeDialog(3)
class EventDialog:
    def __init__(self,type):
        self.root = Tk()
        if type==0:
            self.root.title("Create Event")
        else:
            self.root.title("Edit Event")
            event_id_label = Label(self.root, text="Event ID:")
            event_id_label.pack()
            self.event_id_entry = Entry(self.root)
            self.event_id_entry.pack()
        
        event_name_label = Label(self.root, text="Event Name:")
        event_name_label.pack()
        self.event_name_entry = Entry(self.root)
        self.event_name_entry.pack()

        venue_name_label = Label(self.root, text="Venue ID:")
        venue_name_label.pack()
        self.venue_name_entry = Entry(self.root)
        self.venue_name_entry.pack()

        organizer_name_label = Label(self.root, text="Organizer ID:")
        organizer_name_label.pack()
        self.organizer_name_entry = Entry(self.root)
        self.organizer_name_entry.pack()

        speaker_name_label = Label(self.root, text="Speaker ID:")
        speaker_name_label.pack()
        self.speaker_name_entry = Entry(self.root)
        self.speaker_name_entry.pack()

        ticket_quantity_label = Label(self.root, text="Ticket Quantity:")
        ticket_quantity_label.pack()
        self.ticket_quantity_entry = Entry(self.root)
        self.ticket_quantity_entry.pack()
        
        staff_quantity_label = Label(self.root, text="Staff Quantity:")
        staff_quantity_label.pack()
        self.staff_quantity_entry = Entry(self.root)
        self.staff_quantity_entry.pack()
        if type==1:
            report_id_label = Label(self.root, text="Report ID:")
            report_id_label.pack()
            self.report_id_entry = Entry(self.root)
            self.report_id_entry.pack()

        event_date_label = Label(self.root, text="Event Date:")
        event_date_label.pack()
        self.event_date_entry = Entry(self.root)
        self.event_date_entry.pack()

        txt = "Create Event"
        cmd = self.create_event
        if type==1:
            txt="Update Event"
            cmd=self.update_event
        create_event_button = Button(
            self.root, text=txt, command=cmd)
        create_event_button.pack()

    def create_event(self):
        event_name = self.event_name_entry.get()
        venue_id = self.venue_name_entry.get()
        organizer_id = self.organizer_name_entry.get()
        speaker_id = self.speaker_name_entry.get()
        ticket_quantity = int(self.ticket_quantity_entry.get())
        staff_quantity = int(self.staff_quantity_entry.get())
        event_date = self.event_date_entry.get()

        global cursor, mydb
        try:
            if not mydb.in_transaction:
                mydb.start_transaction()
            cursor.execute("""INSERT INTO Event(event_name,
                       organizer_id,venue_id,ticket_quantity,staff_quantity,
                       speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s,%s)""",
                       (event_name,organizer_id,venue_id,ticket_quantity,staff_quantity,speaker_id,None,event_date))
            cursor.execute("SELECT event_id FROM Event ORDER BY event_id DESC LIMIT 1")
            last_id = cursor.fetchone()[0]
            cursor.execute(
                "UPDATE Speaker SET event_id=%s WHERE speaker_id=%s", (last_id, speaker_id))
            mydb.commit()
        except mysql.connector.Error as err:
            show_warning(err.msg)
            mydb.rollback()
            
        self.root.destroy()
        
    def update_event(self):
        event_id = self.event_id_entry.get()
        event_name = self.event_name_entry.get()
        venue_id = self.venue_name_entry.get()
        organizer_id = self.organizer_name_entry.get()
        speaker_id = self.speaker_name_entry.get()
        ticket_quantity = int(self.ticket_quantity_entry.get())
        staff_quantity = int(self.staff_quantity_entry.get())
        report_id = self.report_id_entry.get()
        event_date = self.event_date_entry.get()

        global cursor, mydb
        try:
            cursor.execute("""UPDATE Event
                            SET event_name = %s,organizer_id=%s,venue_id=%s,ticket_quantity=%s,
                            staff_quantity=%s,speaker_id=%s,report_id=%s,date = %s
                            WHERE event_id = %s """,
                           (event_name, organizer_id, venue_id, ticket_quantity,staff_quantity, speaker_id, report_id, event_date,event_id))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()

        self.root.destroy()
class CancelEventDialog:
    def __init__(self,type):
        self.root = Tk()
        title = "Cancel Event"
        cmd = self.cancel_event
        if type==1:
            title="Attend Event"
            cmd = self.attend_event
        elif type==2:
            title = "Change Topic"
            cmd = self.change_topic
        elif type == 3:
            title = "Add Speaker"
            cmd = self.add_speaker
            
        self.root.title(title)
        if type == 1 or type ==2:
            speaker_id_label = Label(self.root, text="Speaker ID:")
            speaker_id_label.pack()
            self.speaker_id_entry = Entry(self.root)
            self.speaker_id_entry.pack()
        if type == 1 or type == 0:
            event_name_label = Label(self.root, text="Event ID:")
            event_name_label.pack()
            self.event_name_entry = Entry(self.root)
            self.event_name_entry.pack()
        if type == 3:
            name_label = Label(self.root, text="Name:")
            name_label.pack()
            self.name_entry = Entry(self.root)
            self.name_entry.pack()
        if type == 2 or type==3:
            topic_label = Label(self.root, text="Topic:")
            topic_label.pack()
            self.topic_entry = Entry(self.root)
            self.topic_entry.pack()

        create_event_button = Button(
            self.root, text=title, command=cmd)
        create_event_button.pack()

    def cancel_event(self):
        event_id = self.event_name_entry.get()

        global cursor, mydb
        try:
            cursor.execute("DELETE FROM Event WHERE event_id=%s",
                           (event_id,))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()
    def attend_event(self):
        event_id = self.event_name_entry.get()
        speaker_id = self.speaker_id_entry.get()

        global cursor, mydb
        try:
            if not mydb.in_transaction:
                mydb.start_transaction()
            cursor.execute("UPDATE Event SET speaker_id= %s WHERE event_id= %s",
                           (speaker_id, event_id))
            cursor.execute("UPDATE Speaker SET event_id = %s WHERE speaker_id = %s",
                           (event_id,speaker_id))
            mydb.commit()
        except mysql.connector.Error as err:
            show_warning(err.msg)
            mydb.rollback()

        self.root.destroy()
    def change_topic(self):
        topic = self.topic_entry.get()
        speaker_id = self.speaker_id_entry.get()

        global cursor, mydb
        try:
            cursor.execute("UPDATE Speaker SET topic= %s WHERE speaker_id= %s",
                           (topic, speaker_id,))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()
    def add_speaker(self):
        topic = self.topic_entry.get()
        name = self.name_entry.get()

        global cursor, mydb
        try:
            cursor.execute("""INSERT INTO Speaker(speaker_name,event_id,topic) values(%s,%s,%s)""",
                           (name,None,topic))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()
class AttendeeDialog:
    def __init__(self, type):
        self.root = Tk()
        title = "Add Attendee"
        cmd = self.create_attendee
        if type == 1:
            title = "Edit Attendee"
            cmd = self.update_attendee
        elif type == 2:
            title = "Buy Ticket"
            cmd = self.buy_ticket
        elif type == 3:
            title = "Cancel Ticket"
            cmd = self.cancel_ticket
            
        self.root.title(title)
        
        if type==1 or type==2 or type==3:
            attendee_id_label = Label(self.root, text="Attendee ID:")
            attendee_id_label.pack()
            self.attendee_id_entry = Entry(self.root)
            self.attendee_id_entry.pack()
        if type==0 or type==1:
            attendee_name_label = Label(self.root, text="Attendee Name:")
            attendee_name_label.pack()
            self.attendee_name_entry = Entry(self.root)
            self.attendee_name_entry.pack()

            age_label = Label(self.root, text="Age:")
            age_label.pack()
            self.age_entry = Entry(self.root)
            self.age_entry.pack()
        if type==2:
            event_id_label = Label(self.root, text="Event ID:")
            event_id_label.pack()
            self.event_id_entry = Entry(self.root)
            self.event_id_entry.pack()
        if type == 3:
            ticket_id_label = Label(self.root, text="Ticket ID:")
            ticket_id_label.pack()
            self.ticket_id_entry = Entry(self.root)
            self.ticket_id_entry.pack()
        
        create_attendee_button = Button(
            self.root, text=title, command=cmd)
        create_attendee_button.pack()

    def create_attendee(self):
        attendee_name = self.attendee_name_entry.get()
        age = self.age_entry.get()

        global cursor, mydb
        try:
            cursor.execute("""INSERT INTO Attendee(attendee_name,age,ticket_quantity)values(%s,%s,%s)""",
                           (attendee_name,age,None))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()
    def update_attendee(self):
        attendee_id = self.attendee_id_entry.get()
        attendee_name = self.attendee_name_entry.get()
        age = self.age_entry.get()

        global cursor, mydb
        try:
            cursor.execute("UPDATE Attendee SET attendee_name = %s,age=%s WHERE attendee_id = %s",
                           (attendee_name, age, attendee_id))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()
    def buy_ticket(self):
        attendee_id = self.attendee_id_entry.get()
        event_id = self.event_id_entry.get()

        global cursor, mydb
        try:
            if not mydb.in_transaction:
                mydb.start_transaction()
            cursor.execute("SELECT event_name, date, venue_id FROM Event WHERE event_id= %s",(event_id,))
            event_details = cursor.fetchone()
            if event_details is not None:
                event_name, event_date, venue_id = event_details
                cursor.execute("SELECT venue_name FROM Venue WHERE venue_id= %s", (venue_id,))
                venue_name = cursor.fetchone()
                cursor.execute("""INSERT INTO Ticket(event_id,event_name,event_date,
                                    venue_id,venue_name,attendee_id) values(%s,%s,%s,%s,%s,%s)""",
                            (event_id,event_name,event_date,venue_id,venue_name[0],attendee_id))
                cursor.execute("UPDATE Event SET ticket_quantity = ticket_quantity -1 WHERE event_id=%s",
                               (event_id,))
                cursor.execute("UPDATE Attendee SET ticket_quantity = ticket_quantity +1 WHERE attendee_id=%s",
                               (attendee_id,))
            mydb.commit()
        except mysql.connector.Error as err:
            show_warning(err.msg)
            mydb.rollback()

        self.root.destroy()
    def cancel_ticket(self):
        attendee_id = self.attendee_id_entry.get()
        ticket_id = self.ticket_id_entry.get()

        global cursor, mydb
        try:
            if not mydb.in_transaction:
                mydb.start_transaction()
            cursor.execute("SELECT event_id FROM Ticket WHERE ticket_id= %s", (ticket_id,))
            event_id = cursor.fetchone()
            cursor.execute("UPDATE EVENT SET ticket_quantity= ticket_quantity+1 WHERE event_id= %s",
                           (event_id[0],))
            cursor.execute("DELETE FROM Ticket WHERE ticket_id= %s AND attendee_id=%s ",
                           (ticket_id,attendee_id))
            cursor.execute("UPDATE Attendee SET ticket_quantity = ticket_quantity -1 WHERE attendee_id=%s",
                           (attendee_id,))
            mydb.commit()   
        except mysql.connector.Error as err:
            mydb.rollback()
            show_warning(err.msg)
            
        self.root.destroy()
class StaffDialog:
    def __init__(self, type):
        self.root = Tk()
        title = "Add Staff"
        cmd = self.create_staff
        if type == 1:
            title = "Edit Staff"
            cmd = self.update_staff
        elif type == 2:
            title = "Remove Staff"
            cmd = self.remove_staff
        elif type == 3:
            title = "Volunteer"
            cmd = self.be_volunteer

        self.root.title(title)

        if type == 1 or type == 2 or type == 3:
            staff_id_label = Label(self.root, text="Staff ID:")
            staff_id_label.pack()
            self.staff_id_entry = Entry(self.root)
            self.staff_id_entry.pack()
        if type == 0 or type == 1:
            staff_name_label = Label(self.root, text="Staff Name:")
            staff_name_label.pack()
            self.staff_name_entry = Entry(self.root)
            self.staff_name_entry.pack()

            age_label = Label(self.root, text="Age:")
            age_label.pack()
            self.age_entry = Entry(self.root)
            self.age_entry.pack()
        if type == 3:
            event_id_label = Label(self.root, text="Event ID:")
            event_id_label.pack()
            self.event_id_entry = Entry(self.root)
            self.event_id_entry.pack()

        create_attendee_button = Button(
            self.root, text=title, command=cmd)
        create_attendee_button.pack()

    def create_staff(self):
        staff_name = self.staff_name_entry.get()
        age = self.age_entry.get()

        global cursor, mydb
        try:
            cursor.execute("INSERT INTO Staff(staff_name,age)values(%s,%s)",(staff_name, age))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()
    def update_staff(self):
        staff_id = self.staff_id_entry.get()
        staff_name = self.staff_name_entry.get()
        age = self.age_entry.get()

        global cursor, mydb
        try:
            cursor.execute("UPDATE Staff SET staff_name = %s,age=%s WHERE staff_id = %s",
                           (staff_name, age, staff_id))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()
    def be_volunteer(self):
        global cursor, mydb
        staff_id = self.staff_id_entry.get()
        event_id = self.event_id_entry.get()

        try:
            if not mydb.in_transaction:
                mydb.start_transaction()
            cursor.execute("UPDATE Staff SET event_id=%s WHERE staff_id= %s", (event_id,staff_id,))
            cursor.execute("UPDATE Event SET staff_quantity=staff_quantity-1 WHERE event_id= %s", (event_id,))
            mydb.commit()
        except mysql.connector.Error as err:
            show_warning(err.msg)
            mydb.rollback()

        self.root.destroy()
    def remove_staff(self):
        staff_id = self.staff_id_entry.get()
        global cursor, mydb
        try:
            cursor.execute("DELETE FROM Staff WHERE staff_id= %s",(staff_id,))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()

class ReportDialog:
    def __init__(self, type):
        self.root = Tk()
        title = "See Report"
        cmd = self.see_report
        if type == 1:
            title = "Add Report"
            cmd = self.add_report

        self.root.title(title)
        if type == 0:
            report_id_label = Label(self.root, text="Report ID:")
            report_id_label.pack()
            self.report_id_entry = Entry(self.root)
            self.report_id_entry.pack()
        if type == 1:
            event_id_label = Label(self.root, text="Event ID:")
            event_id_label.pack()
            self.event_id_entry = Entry(self.root)
            self.event_id_entry.pack()
            
            info_label = Label(self.root, text="Information:")
            info_label.pack()
            self.info_entry = Entry(self.root)
            self.info_entry.pack()

        create_event_button = Button(
            self.root, text=title, command=cmd)
        create_event_button.pack()

    def see_report(self):
        report_id = self.report_id_entry.get()
        global cursor, mydb
        try:
            cursor.execute("SELECT details FROM Report WHERE report_id= %s",
                           (report_id ,))
            info=cursor.fetchone()[0]
            messagebox.showinfo("Report",str(info))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()

    def add_report(self):
        event_id = self.event_id_entry.get()
        info=self.info_entry.get()

        global cursor, mydb
        try:
            cursor.callproc("AddReport", [info])
            cursor.execute(
                "SELECT report_id FROM Report ORDER BY report_id DESC LIMIT 1")
            last_id = cursor.fetchone()[0]
            cursor.execute(
                "UPDATE Event SET report_id=%s WHERE event_id=%s", (last_id,event_id))
        except mysql.connector.Error as err:
            show_warning(err.msg)

        mydb.commit()
        self.root.destroy()


def clearEntries(entries):
    k=len(entries)
    for i in range(k):
        entries.pop().delete(0,END)
        
def show_warning(txt):
    messagebox.showwarning("Warning", txt)

if __name__ == "__main__":
    main_app = Main_App()
    main_app.window.mainloop()
