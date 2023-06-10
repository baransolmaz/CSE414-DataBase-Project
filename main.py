from tkinter import *
from tkinter import messagebox
from database_connection import *

mydb, cursor = initialize_connection()
#dropAllDB()

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
                                   width=15, height=3)  # , command=Staff_App)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="View Event Details",
                                           width=15, height=3)  # , command=Staff_App)
        view_event_details_button.place(x=152, y=5)
        volunteer_button = Button(self.window, text="Be Volunteer",
                                  width=15, height=3)  # , command=Staff_App)
        volunteer_button.place(x=302, y=5)


class Speaker_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Speaker")  # Pencere ismi
        self.entries = []
        list_event_button = Button(self.window, text="List Events",
                                   width=15, height=3)  # , command=Staff_App)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="View Event Details",
                                           width=15, height=3)  # , command=Staff_App)
        view_event_details_button.place(x=152, y=5)
        attend_event_button = Button(self.window, text="Attend Event",
                                     width=15, height=3)  # , command=Staff_App)
        attend_event_button.place(x=302, y=5)
        view_organizer_button = Button(self.window, text="Get Organizer Info",
                                       width=15, height=3)  # , command=Staff_App)
        view_organizer_button.place(x=452, y=5)


class Organizer_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
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
    
    def cancelEvent(self):
       eny = CancelEventDialog()

    def listEvents(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM Event")
        i = 0
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=12, fg='black'))
                self.entries[i*len(event)+j].place(x=(100*j),y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1

    def listVenues(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM Venue")
        i = 0
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=12, fg='black'))
                self.entries[i*len(event)+j].place(x=(100*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1

    def listSpeakers(self):
        global cursor
        clearEntries(self.entries)
        cursor.execute("SELECT * FROM Speaker")
        i = 0
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=12, fg='black'))
                self.entries[i*len(event)+j].place(x=(100*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1

    def editEvent(self):
        global cursor
        clearEntries(self.entries)
        
        cursor.execute("SELECT * FROM Event")
        i = 0
        for event in cursor:
            for j in range(len(event)):
                self.entries.append(Entry(self.window, width=12, fg='black'))
                self.entries[i*len(event)+j].place(x=(100*j), y=(25*i)+80)
                self.entries[i*len(event)+j].insert(END, str(event[j]))
            i = i+1
    
    def createEvent(self):
        evnt=CreateEventDialog()

class Attendee_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Attendee")  # Pencere ismi

        list_event_button = Button(self.window, text="List Events",
                                   width=15, height=3)  # , command=Staff_App)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="View Event Details",
                                           width=15, height=3)  # , command=Staff_App)
        view_event_details_button.place(x=152, y=5)
        attend_event_button = Button(self.window, text="Attend Event",
                                     width=15, height=3)  # , command=Staff_App)
        attend_event_button.place(x=302, y=5)
        view_organizer_button = Button(self.window, text="Get Organizer Info",
                                       width=15, height=3)  # , command=Staff_App)
        view_organizer_button.place(x=152, y=5)

class CreateEventDialog:
    def __init__(self):
        self.root = Tk()
        self.root.title("Create Event")

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

        event_date_label = Label(self.root, text="Event Date:")
        event_date_label.pack()
        self.event_date_entry = Entry(self.root)
        self.event_date_entry.pack()

        create_event_button = Button(
            self.root, text="Create Event", command=self.create_event)
        create_event_button.pack()

    def create_event(self):
        event_name = self.event_name_entry.get()
        venue_id = self.venue_name_entry.get()
        organizer_id = self.organizer_name_entry.get()
        speaker_id = self.speaker_name_entry.get()
        ticket_quantity = int(self.ticket_quantity_entry.get())
        event_date = self.event_date_entry.get()

        global cursor, mydb
        try:
            cursor.execute("""INSERT INTO Event(event_name,
                       organizer_id,venue_id,ticket_quantity,
                       speaker_id,report_id,date) values(%s,%s,%s,%s,%s,%s,%s)""",
                       (event_name,organizer_id,venue_id,ticket_quantity,speaker_id,None,event_date))
        except mysql.connector.Error as err:
            show_warning(err.msg)
            
        mydb.commit()

        self.root.destroy()

class CancelEventDialog:
    def __init__(self):
        self.root = Tk()
        self.root.title("Cancel Event")

        event_name_label = Label(self.root, text="Event ID:")
        event_name_label.pack()
        self.event_name_entry = Entry(self.root)
        self.event_name_entry.pack()

        create_event_button = Button(
            self.root, text="Cancel Event", command=self.cancel_event)
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

def clearEntries(entries):
    k=len(entries)
    for i in range(k):
        entries.pop().delete(0,END)
        

def show_warning(txt):
    messagebox.showwarning("Warning", txt)

if __name__ == "__main__":
    main_app = Main_App()
    main_app.window.mainloop()
