import tkinter as tk
from tkinter import messagebox

# Dummy username and password for validation
VALID_USERNAME = "user"
VALID_PASSWORD = "password123"

def toggle_password():
    if entry_password.cget('show') == '':
        entry_password.config(show="*")
    else:
        entry_password.config(show="")

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = tk.Tk()
root.title("Enhanced Login Form")

entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(pady=5)

btn_toggle_password = tk.Button(root, text="Toggle Password", command=toggle_password)
btn_toggle_password.pack(pady=5)

btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=10)

root.mainloop()
