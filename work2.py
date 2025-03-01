'''
This is a program that calculates and displays the amount earned based on the user input
hours worked and the rate per hour
'''

import tkinter as tk
from tkinter import messagebox

def calculate_earnings():
    try:
        name = name_entry.get()
        hours = float(hours_entry.get())
        rate = float(rate_entry.get())

        earnings = hours * rate
        
        messagebox.showinfo("Earnings", f"Hello, {name}\nYou have earned: ${earnings:.2f}\nThank you and have a nice day.\nGood bye!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for hours and rate.")

window = tk.Tk()
window.title("Earnings Calculator")

greeting_label = tk.Label(window, text="Welcome to my program.\nThis program will calculate the amount earned based on hours worked and rate per hour.")
greeting_label.pack(pady=10)

name_label = tk.Label(window, text="Please enter your full name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

hours_label = tk.Label(window, text="Enter the number of hours worked:")
hours_label.pack()
hours_entry = tk.Entry(window)
hours_entry.pack(pady=5)

rate_label = tk.Label(window, text="Enter the rate per hour:")
rate_label.pack()
rate_entry = tk.Entry(window)
rate_entry.pack(pady=5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_earnings)
calculate_button.pack(pady=10)

window.mainloop()
