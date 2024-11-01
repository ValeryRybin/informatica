from tkinter import *
from tkcalendar import Calendar
from datetime import *
import requests

root = Tk()
root.title("EZHEDNEVNIK")

def get():
    labelnc['text']=ent.get("1.0",'end-1c')

frame1 = Frame(root, bg="gray", width=300, height=300)
frame1.pack(side=LEFT,fill="both", expand=True)
frame2 = Frame(root, bg="grey", width=300, height=300)
frame2.pack(side=LEFT,fill="both", expand=True)
frame3 = Frame(root, bg="grey", width=300, height=300)
frame3.pack(side=LEFT,fill="both", expand=True)

a1="погода"
a2="ощущается"
city = 'Долгопрудный'
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=2e446065206cfc6d7bafbb82078c86f5'
# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url).json()
# получаем данные о температуре и о том, как она ощущается
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
# выводим значения на экран
#print('Сейчас в городе', city, str(temperature), '°C')
#print('Ощущается как', str(temperature_feels), '°C')
a1='Сейчас в городе '+ city+ " "+ str(temperature) + '°C'
a2='Ощущается как '+ str(temperature_feels) +'°C'

labelwth1 = Label(frame3, text=a1, font=("Arial", 14), fg="red", bg="#FBFB32")
labelwth1.pack(pady=10)
labelwth1 = Label(frame3, text=a2, font=("Arial", 14), fg="red", bg="#FBFB32")
labelwth1.pack(pady=10)

canvas = Canvas(frame3, width=100, height=100)
canvas.pack(fill="both", expand=True, pady = 10)
weatherim = PhotoImage(file="C:\\Users\\valer\programming\\1kurs\\dz\\dz_01.11\\weather.png")
canvas.create_image(0,0,anchor=NW,image=weatherim)

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
    label.config(text = "Выбранная дата:  " + cal.get_date())
 
cal.bind("<<CalendarSelected>>", updateLabel)
 
label = Label(frame2, text = "Выбранная дата: -")
label.pack()


labelnotice = Label(frame2,text = "Заметки")
labelnotice.pack()

button = Button(frame2,font='Arial 15', text="сохранить", command=get)
button.pack()

ent = Text(frame2, width=20, height=2)
ent.pack(fill="both", expand=False, pady = 10)

labelnc=Label(frame2,fg='black',bg='white')
labelnc.pack(fill="both")

root.mainloop()