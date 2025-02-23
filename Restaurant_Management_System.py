import tkinter as tk
from tkinter import ttk ,messagebox

class RestaurantOrderManagement :
    def __init__(self,window):
        self.window = window
        self.window.title ("Restaurant Management App")
        self.menu_items = {"Fried meal " : 2 , "Lunch meal " : 3 , "Burger " : 4 ,"Drinks " : 3 ,"Ice - cream " : 5}
        self.exchange_rate = 121.53
        self.setup_ui()


    def setup_ui(self):
        frame = ttk.Frame(self.window)
        frame.place(relx= 0.5 ,rely = 0.5 , anchor = tk.CENTER)
        ttk.Label(frame,text = "Restaurant  Order Management " ,font=("Arial ",20,"bold")).grid(row=0 ,columnspan =3 ,pady = 10 )

        self.menu_quantities = {}
        for i ,(items,price) in enumerate(self.menu_items.items(),1):
            ttk.Label(frame,text = f"{items} (${price}) :" , font = ("Arial ",12)).grid(row = i,column =0,padx =10,pady =5)
            self.menu_quantities[items] = ttk.Entry(frame , width =5)
            self.menu_quantities[items].grid(row = i ,column = 1 , padx = 10 ,pady =5)

        
        self.currency_var = tk.StringVar(value = 'USD')
        ttk.Label(frame,text = "Currency :" , font =("Arial" ,12)).grid(row = len(self.menu_items)+1,column = 0 , padx = 10 ,pady =5)
        currency_dropdown = ttk.Combobox(frame,textvariable=self.currency_var,state="readonly" ,values = ('USD' ,'BDT'))

        currency_dropdown.grid(row = len(self.menu_items)+ 1 ,column =1,pady = 5)
        currency_dropdown.bind("<<ComboboxSelected>>" ,self.update_prices)

        ttk.Button(frame,text = "Place order" , command=self.place_order).grid(row = len(self.menu_items) +2 ,columnspan=3 , pady = 10)


    def update_prices(self, _):
        symbol, rate = ("৳", self.exchange_rate) if self.currency_var.get() == "BDT" else ("$", 1)
        for i, (item, price) in enumerate(self.menu_items.items(), 1):
            self.window.grid_slaves(row=i, column=0)[0].config(text=f"{item} ({symbol}{price * rate}):")
    
    def place_order(self):
        total_cost, order_summary, currency = 0, "Order Summary:\n", self.currency_var.get()
        symbol, rate = ("৳", self.exchange_rate) if currency == "BDT" else ("$", 1)
        
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit() and (qty := int(quantity)) > 0:
                cost = qty * self.menu_items[item] * rate
                total_cost += cost
                order_summary += f"{item}: {qty} x {symbol}{self.menu_items[item] * rate} = {symbol}{cost}\n"
        
        messagebox.showinfo("Order Placed", order_summary + f"\n\nTotal Cost: {symbol}{total_cost}" if total_cost else "Please order at least one item.")

if __name__ == "__main__":
    window = tk.Tk()
    app = RestaurantOrderManagement(window)
    window.geometry("600x500")
    window.mainloop()









        