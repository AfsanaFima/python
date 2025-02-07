from tkinter import *
from datetime import date

window = Tk()

window.title("Welcome to likeGeekss app")
window.geometry('350x200')

lb1 = Label(master=window,text= "Hey there !", fg = "white",bg = "black" , height = 1 , width = 100)



name_lb1 = Label(master=window,text= "Full name ", fg = "white",bg = "black" )
name_entry = Entry()

text_box = Text(height=4)

def display() :
    name = name_entry.get()


    global message
    message = "Welcome to my app !!! \nToday's date is  :"+ str(date.today())
    greet = "Hello " + name +"\n"


    text_box.insert(END,greet)
    text_box.insert(END,message)


btn = Button(master=window,text = 'Submit' , command=display ,height = 1 , bg="Lavender",fg = "black")

lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()


