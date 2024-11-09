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

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

add_button = tk.Button(window, text="Add", command=add_numbers)
add_button.pack(pady=10)        