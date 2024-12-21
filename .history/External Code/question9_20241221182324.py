import tkinter as tk

root = tk.Tk()
root.title("login Appilication")
root.geometry('400x400')

userName_Label = tk.Label(root,"Enter Username : ")
userName_Label.pack(pady=5)

userName_entry = tk.Entry(root)
userName_entry.pack(pady=5)

password_label = tk.Label(root,"Enter Password : ")
password_label.pack(pady=5)

password_entry =  tk.Entry(root, show = "*")
password_entry.pack(pady=5)

login_button = tk.button("")