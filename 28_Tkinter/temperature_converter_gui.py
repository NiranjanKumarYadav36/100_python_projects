import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Fahrenheit to Celsius Converter")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

fahrenheit_label = ttk.Label(frame, text="Enter temperature in fahrenheit: ")
fahrenheit_label.grid(row=0, column=0, sticky=(tk.W))

fahrenheit_input = ttk.Entry(frame, width=15)
fahrenheit_input.grid(row=0, column=1, sticky=(tk.W), pady=2)

result_label = ttk.Label(frame)
result_label.grid(row=2, column=0, sticky=(tk.W))


def convert():
    temperature = float(fahrenheit_input.get())
    celsius = (temperature - 32) * 9/5
    result_label.config(text=f"Temperature in celsius is: {celsius}")


calculate_button = ttk.Button(frame, text="Convert", command=convert)
calculate_button.grid(row=1, column=0, columnspan=2, sticky=(tk.W))

root.mainloop()
