from tkinter import *
from tkinter.filedialog import askopenfilename ,asksaveasfilename

window = Tk()
window.title("My Text Editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)


text_edit = Text(window)

def openFile():
    """OPen a file foe editing"""
    filepath = askopenfilename(
        filetypes=[("Text files","*.txt") ,("All files","*.*")]

    )

    if not filepath:
        return
    text_edit.delete(1.0,END)
    with open (filepath,"r") as input_file:
        text = input_file.read()

        text_edit.insert(END,text)
    window.title(f"Codingal's Text editer - {filepath}")


def saveFile():
   
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt") ,("All files","*.*")]

    )

    if not filepath:
        return
    
    with open (filepath,"w") as output_file:
        text = text_edit.get(1.0,END)

        output_file.write(text)
    window.title(f"Codingal's Text editer - {filepath}")

frame_button = Frame(window ,relief=RAISED, bd = 2)
btn_open = Button(frame_button,text ="Open ", command=openFile)
btn_save = Button(frame_button,text ="Save as", command=saveFile)

btn_open.grid(row=0,column=0,sticky="ew", padx=5 ,pady=5)
btn_save.grid(row=1,column=0,sticky="ew", padx=5 )

frame_button.grid(row=0 , column=0, sticky="ns")
text_edit.grid(row=0 , column=1, sticky="nsew")

window.mainloop()