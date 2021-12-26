# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date

# Create Object
root = Tk()
today = date.today()
# Set geometry
root.geometry("400x400")

# Add Calendar


cal = Calendar(root, selectmode='day',
               year=today.year, month=today.month,
               day=today.day)

cal.pack(pady=20)

cal.pack(fill="both", expand=True)

eventHeader = Label(root, text="Millard North Events : " + cal.get_date())
eventHeader.pack(pady=20)

# Execute Tkinter
root.mainloop()

