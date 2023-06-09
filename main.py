from tkinter import *
from database_connection import *

#mydb, cursor = initialize_connection()

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

        list_event_button = Button(self.window, text="List Events",
                                   width=25, height=3)  # , command=Staff_App)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="View Event Details",
                                           width=25, height=3)  # , command=Staff_App)
        view_event_details_button.place(x=2, y=75)
        volunteer_button = Button(self.window, text="Be Volunteer",
                                  width=25, height=3)  # , command=Staff_App)
        volunteer_button.place(x=2, y=145)


class Speaker_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Speaker")  # Pencere ismi

        list_event_button = Button(self.window, text="List Events",
                                   width=25, height=3)  # , command=Staff_App)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="View Event Details",
                                           width=25, height=3)  # , command=Staff_App)
        view_event_details_button.place(x=2, y=75)
        attend_event_button = Button(self.window, text="Attend Event",
                                     width=25, height=3)  # , command=Staff_App)
        attend_event_button.place(x=2, y=145)
        view_organizer_button = Button(self.window, text="Get Organizer Info",
                                       width=25, height=3)  # , command=Staff_App)
        view_organizer_button.place(x=2, y=215)


class Organizer_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Organizer")  # Pencere ismi

        create_event_button = Button(self.window, text="Create Events",
                                     width=25, height=3)  # , command=Staff_App)
        create_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="View Event Details",
                                           width=25, height=3)  # , command=Staff_App)
        view_event_details_button.place(x=2, y=75)
        list_event_button = Button(self.window, text="List Events",
                                   width=25, height=3)  # , command=Staff_App)
        list_event_button.place(x=2, y=145)
        invite_speaker_button = Button(self.window, text="Invite Speaker",
                                       width=25, height=3)  # , command=Staff_App)
        invite_speaker_button.place(x=2, y=215)


class Attendee_App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")  # Screen Size(yatay x dikey)
        self.window.resizable(0, 0)
        self.window.config(background="#9BABB8")
        self.window.title("Attendee")  # Pencere ismi

        list_event_button = Button(self.window, text="List Events",
                                   width=25, height=3)  # , command=Staff_App)
        list_event_button.place(x=2, y=5)
        view_event_details_button = Button(self.window, text="View Event Details",
                                           width=25, height=3)  # , command=Staff_App)
        view_event_details_button.place(x=2, y=75)
        attend_event_button = Button(self.window, text="Attend Event",
                                     width=25, height=3)  # , command=Staff_App)
        attend_event_button.place(x=2, y=145)
        view_organizer_button = Button(self.window, text="Get Organizer Info",
                                       width=25, height=3)  # , command=Staff_App)
        view_organizer_button.place(x=2, y=215)
# print(mydb)
# mycursor = mydb.cursor()
# #mycursor.execute("DROP DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


if __name__ == "__main__":
    main_app = Main_App()
    main_app.window.mainloop()
