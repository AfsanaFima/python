import tkinter as tk
from datetime import datetime

def calculate_age():
    """Calculates the current age based on the entered DOB"""
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        dob = datetime(year, month, day)
        today = datetime.today()
        
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your Age: {age} years")
    except ValueError:
        result_label.config(text="Invalid Input")


window = tk.Tk()
window.title("Age Calculator")
window.resizable(False, False)


frame = tk.Frame(window)
tk.Label(frame, text="Day:").grid(row=0, column=0)
entry_day = tk.Entry(frame, width=5)
entry_day.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Month:").grid(row=0, column=2)
entry_month = tk.Entry(frame, width=5)
entry_month.grid(row=0, column=3, padx=5)

tk.Label(frame, text="Year:").grid(row=0, column=4)
entry_year = tk.Entry(frame, width=6)
entry_year.grid(row=0, column=5, padx=5)


calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
result_label = tk.Label(window, text="Enter your DOB", font=("Arial", 12, "bold"))


frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
calculate_button.grid(row=1, column=0, pady=10)
result_label.grid(row=2, column=0, pady=10)


window.mainloop()
