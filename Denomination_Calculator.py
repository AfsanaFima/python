from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk ()
window.title("Denomination Calculator")
window.geometry("600x600")
window.configure(bg="light blue")

upload = Image.open("app_img.jpg")
upload = upload.resize((300,300))
image =ImageTk.PhotoImage(upload)
label = Label (window ,image = image,bg = "light pink")
label.place(x = 100, y = 50)

label1 = Label(window ,text = "Hey user , welcome to the Denominator calculator  !! " , font=("Arial" ,15) , bg ="teal")

label1.place(relx = 0.5 ,y = 350 ,anchor= CENTER)

def msg ():
    msgbox = messagebox.showinfo("Alert ", "Do you want to start yje calculation ?")

    if msgbox == "ok" :
        topwin()

button1 = Button(window , text = "Let's start ",command=msg , bg="black" , fg ="white" , font=("Arial" ,15))

button1.place(x = 250 , y= 370)

def topwin():
    top = Toplevel() 
    top.title("Denominator Calculator")
    top.configure(bg="light grey")  
    top.geometry("600x400")   

    label = Label(top, text="Enter total amount", bg="light grey")    
    entry = Entry(top)

    lbl = Label(top, text="Here are the number of notes of each denomination", bg="light grey")  

    l1 = Label(top, text="1000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="200", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculation():
        try:
            global amount 
            amount = int (entry.get())
            note1000 = amount //1000
            amount = amount % 1000
            note500 = amount // 500
            amount = amount % 500
            note200 = amount //200


        

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note200))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")    

    btn = Button(top, text="Calculate", command=calculation, bg="brown", fg="white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()
window.mainloop()    


