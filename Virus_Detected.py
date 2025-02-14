from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus Detected !!!!!")
window.geometry("400x400")

messagebox.showinfo("info","Check for virus!!")

def msg ():
    messagebox.showwarning("Messege box ","Virus Detected !")

button = Button(text = "Click me !!",command= msg)
button.place(x= 150 ,y=150)

window.mainloop()