from tkinter import *
from tkcalendar import Calendar
from datetime import *
import requests



root = Tk()

frame1 = Frame(root, bg="gray", width=300, height=300)
frame1.pack(side=LEFT,fill="both", expand=True)
frame2 = Frame(root, bg="grey", width=300, height=300)
frame2.pack(side=LEFT,fill="both", expand=True)




current_date = date.today()
current_date=str(current_date)

yearnow = int(current_date[0:4])
mounthnow = int(current_date[5:7])
daynow = int(current_date[8:10])

root.geometry('800x600')
cal = Calendar(frame1, font="Arial 14",
               selectmode = 'day',
               year = yearnow, month = mounthnow,
               day = daynow,
               locale='ru_RUSSIA')
 
cal.pack(fill="both", expand=True, pady = 10)
 
def updateLabel(event):
    label.config(text = "Selected Date is: " + cal.get_date())
 
cal.bind("<<CalendarSelected>>", updateLabel)
 
label = Label(frame2, text = "Selected Date: ")
label.pack()


root.mainloop()