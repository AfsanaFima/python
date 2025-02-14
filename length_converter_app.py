import tkinter as tk

def inches_to_cm():
    """Converts inches to centimeters"""
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="Invalid Input")


window = tk.Tk()
window.title("Inches to Centimeters Converter")
window.resizable(False, False)


frame = tk.Frame(window)
entry = tk.Entry(frame, width=10)
label_inch = tk.Label(frame, text="inches")

entry.grid(row=0, column=0, padx=5)
label_inch.grid(row=0, column=1, padx=5)


convert_button = tk.Button(window, text="Convert", command=inches_to_cm)
result_label = tk.Label(window, text="cm", font=("Arial", 12, "bold"))


frame.grid(row=0, column=0, padx=10, pady=10)
convert_button.grid(row=0, column=1, padx=10, pady=10)
result_label.grid(row=0, column=2, padx=10, pady=10)


window.mainloop()

