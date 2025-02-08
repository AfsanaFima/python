from tkinter import *

window = Tk()
window.title("Number Pad")
window.geometry("400x400")

frame = Frame(master=window , height = 300 , width = 350 , bg= "pink")


lbl1 = Label(master = frame , text = "Username ", bg ="lavender", font = ("Arial",18))
lbl2 = Label(master = frame , text = "Email", bg ="lavender" ,font = ("Arial",18))
lbl3 = Label(master = frame , text = "Password ", bg ="lavender", font = ("Arial",18))

name_entry = Entry(master = frame , width = 50)
email_entry = Entry(master = frame , width = 50)
password_entry = Entry(master = frame , width = 50 , show  = '*')

text_box = Text(bg = "blue", fg = "black",font = ("Arial",12), height=5 , width=40)

def display ():
    name = name_entry.get()
    greet = "Hello",name
    message = "\n login successful"
    text_box.insert(END,greet)
    text_box.insert(END,message)


btn =  Button(text = "Login",command=display , height=2 ,width=25 ,  bg = "teal", fg = "brown")


frame.place (x = 20,y=0)
lbl1.place (x = 20,y=20)
name_entry.place (x = 25,y=50)
lbl2.place (x = 20,y=80)
email_entry.place (x = 25,y=110)
lbl3.place (x = 20,y=140)
password_entry.place (x = 25,y=175)
btn.place (x = 100,y=200)
text_box.place (x = 20,y=250)

window.mainloop()
