from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Main Window")

def topwindow ():
    top = Tk()
    top.geometry("200x100")
    top.title("Top window")

    top_label = Label(top ,text = "this is top window")
    top_label.pack()
    top.mainloop()

l1 = Label(window,text = "This is the main window")
btn =  Button(window,text = "Click here ",command= topwindow)

l1.pack()
btn.pack()
window.mainloop()