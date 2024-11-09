import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Simple Form")
window.geometry("300x250")

name_label = tk.Label(window, text="Name:")
name_label.pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

age_label = tk.Label(window, text="Age:")
age_label.pack(pady=5)
age_entry = tk.Entry(window)
age_entry.pack(pady=5)

email_label = tk.Label(window, text="Email:")
email_label.pack(pady=5)
email_entry = tk.Entry(window)
email_entry.pack(pady=5)

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    if not name or not age or not email:
        messagebox.showerror("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nEmail: {email}")

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack(pady=20)

window.mainloop()