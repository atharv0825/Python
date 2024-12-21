import tkinter as tk

root = tk.Tk()
root.title("login Appilication")
root.geometry('400x400')

userName_Label = tk.Label("Enter Username : ")
userName_Label.pack(pady=5)

userName_entry = tk.Entry(root)
userName_entry.pack(pady=5)

password_label = tk.Label("Enter Password : ")
password_label.pack(pady=5)

password_entry =  tk.E