# Version 1.0
# Created by StormTrooper720 on GitHub
from time import strftime
from tkinter import Label, Tk


def dark():
    window = Tk()
    window.title("Clock")
    window.geometry("380x100")
    window.configure(bg="#383838")

    clock_label = Label(window, bg="#383838", fg="white", font=("Times", 30), relief='flat')
    clock_label.place(x=20, y=20)


def light():
    window = Tk()
    window.title("Clock")
    window.geometry("380x100")
    window.configure(bg="white")

    clock_label = Label(window, bg="white", fg="black", font=("Times", 30), relief='flat')
    clock_label.place(x=20, y=20)


def update_label():
    current_time = strftime('%D: %H: %M: %S')
    clock_label.configure(text=current_time)
    clock_label.after(100, update_label)


def some():
    dark_mode = None
    try:
        dark_mode = str(input("Would you like dark mode? Enter true are false:"))
    except ValueError:
        some()
        dark_mode = f"{dark_mode.title()}"
    if dark_mode == "Yes":
        dark()
    elif dark_mode == "Yes":
        light()


update_label()
window.mainloop()
