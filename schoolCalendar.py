# Import Required Library
from __future__ import print_function
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from quickstart import *
from datetime import datetime
import pandas as pd

# Create Objects
root = Tk()
root.update_idletasks()
today = date.today()
# Set geometry
root.geometry("400x400")

# Add Calendar


cal = Calendar(root, selectmode='day',
               year=today.year, month=today.month,
               day=today.day)

cal.pack(pady=20)
test = calendarEvents()
for event in calendarEvents():

    start = event['start'].get('dateTime', event['start'].get('date'))
    date_time_obj = pd.to_datetime(start).date()
    date = cal.datetime.today()
    cal.calevent_create(date_time_obj, event['summary'], 'reminder')

cal.tag_config('reminder', background='red', foreground='yellow')

eventHeader = Label(root, text="Millard North Events : " + cal.get_date())
cal.pack(fill="both", expand=True)
eventHeader.pack(pady=20)

# Execute Tkinter
root.mainloop()
