from tkinter import *
import mysql.connector
from database import *

#mydb, cursor = initialize_connection()

class Main_App:
	def __init__(self):
		self.window = Tk()
		self.window.geometry("400x290")  # Screen Size(yatay x dikey)
		self.window.resizable(0, 0)
		self.window.config(background="#9BABB8")
		self.window.title("EVENT MANAGEMENT SYSTEM")  # Pencere ismi

		organizer_button = Button(self.window, text="Event Organizer View", width=46,height=3)
		organizer_button.place(x=2, y=5)
  
		speaker_button = Button(self.window, text="Speaker View", width=46, height=3)
		speaker_button.place(x=2, y=75)
		attendee_button = Button(self.window, text="Attendee View", width=46, height=3)
		attendee_button.place(x=2, y=145)
		staff_button = Button(self.window, text="Staff/Volunteer View", width=46, height=3, command=Staff_App)
		staff_button.place(x=2, y=215)


class Staff_App:
	def __init__(self):
		self.window = Tk()
		self.window.geometry("800x600")  # Screen Size(yatay x dikey)
		self.window.resizable(0, 0)
		self.window.config(background="#9BABB8")
		self.window.title("Staff-Volunteer View")  # Pencere ismi
  
		list_event_button = Button(self.window, text="List Events",
		                      width=25, height=3)#, command=Staff_App)
		list_event_button.place(x=2, y=5)
		view_event_details_button = Button(self.window, text="View Event Details",
                             width=25, height=3)  # , command=Staff_App)
		view_event_details_button.place(x=2, y=75)
		volunteer_button = Button(self.window, text="Be Volunteer",
								width=25, height=3)  # , command=Staff_App)
		volunteer_button.place(x=2, y=145)
		


        
# print(mydb)
# mycursor = mydb.cursor()
# #mycursor.execute("DROP DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
  
if __name__=="__main__":
    main_app = Main_App()
    main_app.window.mainloop()
