import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Your Fixer.io API key
ACCESS_KEY = "d2b6b9768b720969433c76032b3d7ae9"
API_URL = f"http://data.fixer.io/api/latest?access_key={ACCESS_KEY}"

# Fetch exchange rates
def fetch_rates():
    try:
        response = requests.get(API_URL)
        data = json.loads(response.text)
        if not data.get("success", False):
            raise Exception(data.get("error", {}).get("info", "Unknown error"))
        return data["rates"]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch rates:\n{e}")
        return {}

# Convert currency
def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get().upper()
        to_curr = combo_to.get().upper()

        if from_curr not in rates or to_curr not in rates:
            raise ValueError("Currency not supported")

        rate = rates[to_curr] / rates[from_curr]
        converted = round(amount * rate, 2)

        result_label.config(text=f"{amount} {from_curr} = {converted} {to_curr}", fg="green")
    except ValueError:
        result_label.config(text="Invalid input or currency", fg="red")

# Show list of currencies
def show_currencies():
    messagebox.showinfo("Supported Currencies", "\n".join(sorted(rates.keys())))

# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x320")import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Your Fixer.io API key
ACCESS_KEY = "d2b6b9768b720969433c76032b3d7ae9"
API_URL = f"http://data.fixer.io/api/latest?access_key={ACCESS_KEY}"

# Fetch exchange rates
def fetch_rates():
    try:
        response = requests.get(API_URL)
        data = json.loads(response.text)
        if not data.get("success", False):
            raise Exception(data.get("error", {}).get("info", "Unknown error"))
        return data["rates"]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch rates:\n{e}")
        return {}

# Convert currency
def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get().upper()
        to_curr = combo_to.get().upper()

        if from_curr not in rates or to_curr not in rates:
            raise ValueError("Currency not supported")

        rate = rates[to_curr] / rates[from_curr]
        converted = round(amount * rate, 2)

        result_label.config(text=f"{amount} {from_curr} = {converted} {to_curr}", fg="green")
    except ValueError:
        result_label.config(text="Invalid input or currency", fg="red")

# Show list of currencies
def show_currencies():
    messagebox.showinfo("Supported Currencies", "\n".join(sorted(rates.keys())))

# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x320")
root.resizable(False, False)

rates = fetch_rates()
currency_codes = sorted(rates.keys()) if rates else []

tk.Label(root, text="Amount:").pack(pady=5)
entry_amount = tk.Entry(root, justify="center")
entry_amount.pack(pady=5)

tk.Label(root, text="From Currency:").pack(pady=5)
combo_from = ttk.Combobox(root, values=currency_codes, state="readonly")
combo_from.set("USD")
combo_from.pack()

tk.Label(root, text="To Currency:").pack(pady=5)
combo_to = ttk.Combobox(root, values=currency_codes, state="readonly")
combo_to.set("INR")
combo_to.pack()

tk.Button(root, text="Convert", command=convert, bg="#cce5ff").pack(pady=10)
tk.Button(root, text="Show Currencies", command=show_currencies).pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=15)

root.mainloop()

root.resizable(False, False)

rates = fetch_rates()
currency_codes = sorted(rates.keys()) if rates else []

tk.Label(root, text="Amount:").pack(pady=5)
entry_amount = tk.Entry(root, justify="center")
entry_amount.pack(pady=5)

tk.Label(root, text="From Currency:").pack(pady=5)
combo_from = ttk.Combobox(root, values=currency_codes, state="readonly")
combo_from.set("USD")
combo_from.pack()

tk.Label(root, text="To Currency:").pack(pady=5)
combo_to = ttk.Combobox(root, values=currency_codes, state="readonly")
combo_to.set("INR")
combo_to.pack()

tk.Button(root, text="Convert", command=convert, bg="#cce5ff").pack(pady=10)
tk.Button(root, text="Show Currencies", command=show_currencies).pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=15)

root.mainloop()
