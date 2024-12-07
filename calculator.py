import tkinter as tk
from math import sqrt, exp

def calculate():
    try:
        result = eval(entry.get())
        history_listbox.insert(tk.END, f"{entry.get()} = {result}")
        label_result.config(text=f"Result: {result}")
    except Exception as e:
        label_result.config(text="Error")

def clear_history():
    history_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Enhanced Calculator")

# Entry for input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons for operations
btn_calc = tk.Button(root, text="Calculate", command=calculate)
btn_calc.pack(pady=5)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

# History of calculations
history_label = tk.Label(root, text="History:")
history_label.pack(pady=5)

history_listbox = tk.Listbox(root, width=40, height=5)
history_listbox.pack(pady=5)

# Clear history button
btn_clear_history = tk.Button(root, text="Clear History", command=clear_history)
btn_clear_history.pack(pady=5)

root.mainloop()
