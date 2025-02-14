import  tkinter as tk

def fahrenheit_to_celsius():
    """Converts fahrenheit to celsius"""
    fahrenheit = temp_entry.get()
    celsius = (float(fahrenheit)-32) * (5/9) 
    result_label["text"] = f"{celsius}°C"

window=  tk.Tk()
window.title("Tempareture Converter")
window.resizable(False,False)

fr_entry = tk.Frame(master=window)
temp_entry = tk.Entry(master=fr_entry,width=10)
temp_label= tk.Label(master=fr_entry,text="°F")

temp_entry.grid(row =0,column=0,sticky="e")
temp_label.grid(row=0,column=0,sticky="w")

button_converter = tk.Button(master=window ,text ="Convert" ,command= fahrenheit_to_celsius)
result_label = tk.Label(master=window ,text = "°C" )

fr_entry.grid(row=0,column=0,padx=10)
button_converter.grid(row=0,column=1,pady=10)
result_label.grid(row=0,column=2,padx=10)

window.mainloop()
