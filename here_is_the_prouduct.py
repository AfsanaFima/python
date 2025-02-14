import tkinter as tk

def multiply_numbers():
    """Multiplies two numbers and displays the result"""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product:.2f}")
    except ValueError:
        result_label.config(text="Invalid Input")


window = tk.Tk()
window.title("Multiplication Calculator")
window.resizable(False, False)


frame = tk.Frame(window)
tk.Label(frame, text="Number 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(frame, width=10)
entry_num1.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Number 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(frame, width=10)
entry_num2.grid(row=1, column=1, padx=5)


multiply_button = tk.Button(window, text="Multiply", command=multiply_numbers)
result_label = tk.Label(window, text="Enter numbers", font=("Arial", 12, "bold"))


frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
multiply_button.grid(row=1, column=0, pady=10)
result_label.grid(row=2, column=0, pady=10)


window.mainloop()
