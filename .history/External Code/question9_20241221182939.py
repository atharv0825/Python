import tkinter as tk
from tkinter import messagebox


def login() :
    username = userName_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "123":
        messagebox.showinfo("lo")

root = tk.Tk()
root.title("login Appilication")
root.geometry('400x400')

userName_Label = tk.Label(root,text="Enter Username : ")
userName_Label.pack(pady=5)

userName_entry = tk.Entry(root)
userName_entry.pack(pady=5)

password_label = tk.Label(root,text="Enter Password : ")
password_label.pack(pady=5)

password_entry =  tk.Entry(root, show = "*")
password_entry.pack(pady=5)

login_button = tk.Button(root,text="login")
login_button.pack(pady=10)

root.mainloop()