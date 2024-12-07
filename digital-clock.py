import tkinter as tk
from time import strftime
from tkinter import messagebox

def update_time():
    current_time = strftime("%H:%M:%S")
    label_time.config(text=current_time)
    label_time.after(1000, update_time)

def set_alarm():
    alarm_time = entry_alarm.get()
    current_time = strftime("%H:%M:%S")
    if current_time == alarm_time:
        messagebox.showinfo("Alarm", "Time's up!")
    label_alarm.config(text=f"Alarm set for: {alarm_time}")
    
def toggle_theme():
    if root.option_get('theme', 'light') == 'light':
        root.tk_setPalette(background='#2e2e2e', foreground='#f0f0f0')
        root.option_add('*TButton.background', '#4a4a4a')
        root.option_add('*TButton.foreground', '#ffffff')
        root.option_add('*TButton.highlightColor', '#7f7f7f')
        root.option_add('*Label.background', '#2e2e2e')
        root.option_add('*Label.foreground', '#ffffff')
        root.option_add('theme', 'dark')
    else:
        root.tk_setPalette(background='#f0f0f0', foreground='#000000')
        root.option_add('*TButton.background', '#d0d0d0')
        root.option_add('*TButton.foreground', '#000000')
        root.option_add('*Label.background', '#f0f0f0')
        root.option_add('*Label.foreground', '#000000')
        root.option_add('theme', 'light')

root = tk.Tk()
root.title("Advanced Digital Clock")

label_time = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
label_time.pack(pady=20)

label_alarm = tk.Label(root, font=("Helvetica", 14), fg="gray")
label_alarm.pack(pady=5)

# Alarm input and set button
entry_alarm = tk.Entry(root, font=("Helvetica", 14))
entry_alarm.pack(pady=5)

btn_set_alarm = tk.Button(root, text="Set Alarm", font=("Helvetica", 14), command=set_alarm)
btn_set_alarm.pack(pady=5)

# Theme toggle button
btn_toggle_theme = tk.Button(root, text="Toggle Theme", font=("Helvetica", 14), command=toggle_theme)
btn_toggle_theme.pack(pady=10)

update_time()
root.mainloop()
