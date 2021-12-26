# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
import quickstart
# p1 = MyClass()
a = quickstart.Events()
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


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
Button(root, text=" View Events: ",
       command=grad_date).pack(pady=20)

date = Label(root, text=""+ a.start)
date.pack(pady=20)

# Execute Tkinter
root.mainloop()
