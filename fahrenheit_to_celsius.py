import tkinter as tk

def fahrenheit_to_celsius():
    """Converts fahrenheit to celsius"""
    fahrenheit = temp_entry.get()
    try:
        celsius = (float(fahrenheit) - 32) * (5/9)
        result_label["text"] = f"{celsius:.2f}°C"
    except ValueError:
        result_label["text"] = "Invalid Input"

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(False, False)

fr_entry = tk.Frame(master=window)
temp_entry = tk.Entry(master=fr_entry, width=10)
temp_label = tk.Label(master=fr_entry, text="°F")

temp_entry.grid(row=0, column=0, sticky="e")
temp_label.grid(row=0, column=1, sticky="w")  # Fixed column alignment

button_converter = tk.Button(master=window, text="Convert", command=fahrenheit_to_celsius)
result_label = tk.Label(master=window, text="°C")

fr_entry.grid(row=0, column=0, padx=10, pady=10)  # Added pady for better alignment
button_converter.grid(row=0, column=1, pady=10)
result_label.grid(row=0, column=2, padx=10)

window.mainloop()
