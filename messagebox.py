from tkinter import *
from tkinter import messagebox

#showing the information
def show_info():
    messagebox.showinfo("information", "You have logged in successfully!")

def ask_question():
    response = messagebox.askquestion("question","Do you want to save it?")
    if response == "yes":
        messagebox.showinfo("response","saved successfully")
    else:
        messagebox.showinfo("response","Messages was not saved successfully")


window = Tk()
window.geometry("500x500")
Button(window, text = "show_info", command = show_info).pack()
Button(window, text = "ask_question", command = ask_question).pack()

window.mainloop()