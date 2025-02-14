from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    """Printing the character associated to the key pressed """
    print(event.char)

window.bind("<Key>",handle_keypress)
  
def handle_click(event):
    print("Buttton is clickedd!!!")

button = Button(text="Click mee!!!!")
button.pack()

window.bind("<Button-1>",handle_click)

window.mainloop()
