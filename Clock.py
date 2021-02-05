# Version 1.0
# Created by StormTrooper720 on GitHub
from time import strftime
from tkinter import Label, Tk

# Creating the window
window = Tk()
window.title("Clock")
window.geometry("380x100")
window.configure(bg="#383838")

clock_label = Label(window, bg="#383838", fg="white", font=("Times", 30), relief='flat')
clock_label.place(x=20, y=20)


def update_label():
    current_time = strftime('%D: %H: %M: %S')
    clock_label.configure(text=current_time)
    clock_label.after(100, update_label)


update_label()
window.mainloop()
