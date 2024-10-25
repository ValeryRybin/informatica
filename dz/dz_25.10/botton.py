from tkinter import *

root = Tk()
root.title("запускядергхки")

frame = Frame(root, bg="gray", width=750, height=750)
frame.pack()

button = Button(frame, text="КРАСНАЯ КНОПКА!!!")
button.config(cursor="hand2")
button.pack(pady=10)

canvas = Canvas(frame, width=500, height=500, bg="white")
canvas.pack(pady=10)

def draw_boom():
    canvas.create_oval(25, 65, 475, 245, fill="yellow")  
    canvas.create_oval(115, 115, 385, 275, fill="red")  
    canvas.create_arc(20, 60, 480, 250, start=-15, extent=210, style="arc")
    canvas.create_arc(100, 100, 400, 290, start=0, extent=180, style="arc")
    canvas.create_arc(200, 20, 150, 400, start=18, extent=-100, style="arc")
    canvas.create_arc(300, 20, 350, 400, start=-100, extent=-100, style="arc")

button.config(command=draw_boom)

root.mainloop()