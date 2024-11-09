import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x200")

label = tk.Label(window, text="Enter two numbers to add:")
label.pack(pady=10)

entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)