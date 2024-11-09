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