import tkinter as tk
import requests
from tkinter import messagebox

def get_exchange_rate():
    try:
        url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD"
        response = requests.get(url)
        data = response.json()
        return data['conversion_rates']
    except:
        messagebox.showerror("Error", "Failed to retrieve exchange rates.")

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = entry_from.get().upper()
        to_currency = entry_to.get().upper()
        
        rates = get_exchange_rate()
        if from_currency != "USD":
            amount = amount / rates[from_currency]  # Convert from base (USD)
        
        converted_amount = amount * rates[to_currency]
        label_result.config(text=f"{converted_amount:.2f} {to_currency}")
    except Exception as e:
        messagebox.showerror("Input Error", "Invalid input or conversion error.")

root = tk.Tk()
root.title("Currency Converter")

entry_amount = tk.Entry(root, width=30)
entry_amount.pack(pady=5)

entry_from = tk.Entry(root, width=10)
entry_from.pack(pady=5)

entry_to = tk.Entry(root, width=10)
entry_to.pack(pady=5)

btn_convert = tk.Button(root, text="Convert", command=convert_currency)
btn_convert.pack(pady=5)

label_result = tk.Label(root, text="Converted Amount: ", font=("Helvetica", 14))
label_result.pack(pady=10)

root.mainloop()
