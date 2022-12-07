from tkinter import *

root = Tk()
root.title("AUTO SERVICE")
root.geometry("300x250+620+260")

root.minsize(200, 150)
root.maxsize(400, 300)

label = Label(text = "Добро пожаловать в наш сервис!")
label.pack()

root.mainloop()