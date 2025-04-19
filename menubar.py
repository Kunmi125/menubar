from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("500x500")
window.configure(background = "white")

#creating menu bar
mbar = Menu(window)

file = Menu(mbar, tearoff = 0)
mbar.add_cascade(label = "File", menu = file)
file.add_command(label = "New file", command = None)
file.add_command(label = "Open", command = None) 
file.add_command(label = "Save", command = None)
file.add_separator()
file.add_command(label = "Exit", command = window.destroy)

view = Menu(mbar, tearoff = 0)
mbar.add_cascade(label = "View", menu = view)


view2 = Menu(view, tearoff = 1)
view.add_cascade(label = "Zoom", menu = view2)
view2.add_command(label = "Zoom In", command = None)
view2.add_command(label = "Zoom Out", command = None)

view.add_command(label = "Run", command = None)


#display menu
window.config(menu = mbar)
window.mainloop()