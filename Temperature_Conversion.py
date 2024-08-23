import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature():
    try:
        value = float(entry_value.get())
        unit = unit_var.get()
        if unit == 'Celsius':
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            result.set(f"{value}°Celsius is {fahrenheit:.2f}°Fahrenheit and {kelvin:.2f} Kelvin")
        elif unit == 'Fahrenheit':
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            result.set(f"{value}°Fahrenheit is {celsius:.2f}°Celsius and {kelvin:.2f} Kelvin")
        elif unit == 'Kelvin':
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            result.set(f"{value} Kelvin is {celsius:.2f}°Celsius and {fahrenheit:.2f}°Fahrenheit")
        else:
            messagebox.showerror("Error", "Invalid unit. Please use 'Celsius', 'Fahrenheit', or 'Kelvin'.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a numerical temperature value.")

def clear():
    entry_value.set('')
    result.set('')
    unit_combobox.set('Celsius')

root = tk.Tk()
root.title("Temperature Converter")

style = ttk.Style(root)
style.theme_use('clam')

style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TCombobox', font=('Helvetica', 12), padding=5)

header_frame = ttk.Frame(root, padding="10")
header_frame.pack(fill=tk.X)

header_label = ttk.Label(header_frame, text="Temperature Converter", font=('Helvetica', 16, 'bold'))
header_label.pack()

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

ttk.Label(main_frame, text="Enter the temperature value:").grid(row=0, column=0, sticky=tk.W, pady=10)
entry_value = tk.StringVar()
entry = ttk.Entry(main_frame, textvariable=entry_value, width=40)
entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=10)

ttk.Label(main_frame, text="Select the unit of the temperature:").grid(row=1, column=0, sticky=tk.W, pady=10)
unit_var = tk.StringVar(value='Celsius')
unit_combobox = ttk.Combobox(main_frame, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=37)
unit_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=10)

convert_button = ttk.Button(main_frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10) 
result = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result, font=('Helvetica', 12, 'bold'), wraplength=500)
result_label.grid(row=3, column=0, columnspan=2, pady=15)

clear_button = ttk.Button(main_frame, text="Clear", command=clear)
clear_button.grid(row=4, column=0, columnspan=2, pady=10) 

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(4, weight=1)

root.geometry("700x400")  

root.mainloop()