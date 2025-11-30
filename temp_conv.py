import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    try:
        temp_value = float(temp_input.get())
        original_unit = unit_selection.get()

        if not original_unit: # Check if a unit is selected
            messagebox.showerror("Input Error", "Please select an original unit.")
            return

        celsius_val = 0
        fahrenheit_val = 0
        kelvin_val = 0

        if original_unit == 'Celsius':
            celsius_val = temp_value
            fahrenheit_val = celsius_to_fahrenheit(celsius_val)
            kelvin_val = celsius_to_kelvin(celsius_val)
        elif original_unit == 'Fahrenheit':
            fahrenheit_val = temp_value
            celsius_val = fahrenheit_to_celsius(fahrenheit_val)
            kelvin_val = fahrenheit_to_kelvin(fahrenheit_val)
        elif original_unit == 'Kelvin':
            kelvin_val = temp_value
            celsius_val = kelvin_to_celsius(kelvin_val)
            fahrenheit_val = kelvin_to_fahrenheit(kelvin_val)

        # Update the result labels
        celsius_result_label.config(text=f"{celsius_val:.2f}°C")
        fahrenheit_result_label.config(text=f"{fahrenheit_val:.2f}°F")
        kelvin_result_label.config(text=f"{kelvin_val:.2f}K")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numerical value for temperature.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# --- Set up the main application window ---
root = tk.Tk()
root.title("Temperature Converter Dashboard")
root.geometry("400x350") # Set initial window size

# --- Input Frame ---
input_frame = ttk.LabelFrame(root, text="Input Temperature", padding="10")
input_frame.pack(padx=10, pady=10, fill="x")

ttk.Label(input_frame, text="Temperature Value:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
temp_input = ttk.Entry(input_frame)
temp_input.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Original Unit:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
unit_options = ['Celsius', 'Fahrenheit', 'Kelvin']
unit_selection = ttk.Combobox(input_frame, values=unit_options, state="readonly")
unit_selection.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
unit_selection.set('Celsius') # Default selection

convert_button = ttk.Button(input_frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Configure column weights for input_frame to make widgets expand
input_frame.grid_columnconfigure(1, weight=1)

# --- Results Frame ---
results_frame = ttk.LabelFrame(root, text="Converted Temperatures", padding="10")
results_frame.pack(padx=10, pady=10, fill="x")

ttk.Label(results_frame, text="Celsius:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
celsius_result_label = ttk.Label(results_frame, text="--.--°C", font=('Helvetica', 12, 'bold'))
celsius_result_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

ttk.Label(results_frame, text="Fahrenheit:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
fahrenheit_result_label = ttk.Label(results_frame, text="--.--°F", font=('Helvetica', 12, 'bold'))
fahrenheit_result_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

ttk.Label(results_frame, text="Kelvin:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
kelvin_result_label = ttk.Label(results_frame, text="--.--K", font=('Helvetica', 12, 'bold'))
kelvin_result_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# --- Start the GUI event loop ---
root.mainloop()