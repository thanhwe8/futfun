import tkinter as tk
from tkinter import ttk
import random

def random_dict():
    """Return a random dictionary with the given keys."""
    return {
        "search": random.randint(0, 100),
        "bought": random.randint(0, 100),
        "missed": random.randint(0, 100),
        "spent": random.randint(0, 100),
    }

def update_values():
    """Generate new random values and update the label."""
    data = random_dict()
    # Make a pretty string for display
    text = "\n".join(f"{k}: {v}" for k, v in data.items())
    label_var.set(text)

root = tk.Tk()
root.title("Random Dictionary Updater")

label_var = tk.StringVar(value="Click the button to generate values")
label = ttk.Label(root, textvariable=label_var, font=("TkDefaultFont", 11), justify="left")
label.pack(padx=20, pady=15)

button = ttk.Button(root, text="Generate Random Dictionary", command=update_values)
button.pack(padx=20, pady=10)

root.mainloop()

