import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Simple Form")
window.geometry("300x250")

name_label = tk.Label(window, text="Name:")
name_label.pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)