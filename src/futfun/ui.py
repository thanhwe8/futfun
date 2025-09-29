import tkinter as tk
from tkinter import ttk

BG = "#0f3d2e"  # window / frame background (dark green)
FG = "#e8f5e9"  # text color (very light green)
ENTRY_BG = "#165a45"  # entry background (medium green)
ACCENT = "#2ecc71"  # accent green for button hover/focus

root = tk.Tk()
root.title("FUT FUN")
root.geometry("360x200")
root.configure(bg=BG)

style = ttk.Style(root)
style.theme_use("clam")

style.configure("Green.TLabel", background=BG, foreground=FG, font=("Segoe UI", 11))
style.configure("Green.TEntry", fieldbackground=ENTRY_BG, foreground=FG, insertcolor=FG)

style.configure("Green.TButton", foreground="white", padding=6)

style.map(
    "Green.TButton",
    background=[("!disabled", ACCENT), ("active", "#27ae60")],
    relief=[("pressed", "sunken"), ("!pressed", "raised")],
)

frame = ttk.Frame(root, style="Green.TFrame", padding=20)
frame.pack(fill="both", expand=True)

lbl1 = ttk.Label(frame, text="First Name", style="Green.TLabel")
ent1 = ttk.Entry(frame, style="Green.TEntry", width=28)

lbl2 = ttk.Label(frame, text="Email", style="Green.TLabel")
ent2 = ttk.Entry(frame, style="Green.TEntry", width=28)

btn  = ttk.Button(frame, text="Submit", style="Green.TButton")
lbl1.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(0, 8))
ent1.grid(row=0, column=1, sticky="ew", pady=(0, 8))

lbl2.grid(row=1, column=0, sticky="w", padx=(0, 10))
ent2.grid(row=1, column=1, sticky="ew")

btn.grid(row=2, column=0, columnspan=2, pady=16)
frame.columnconfigure(1, weight=1)




root = tk.Tk()
root.geometry("300x100")

# Two labels side by side
lbl1 = tk.Label(root, text="Left", bg="lightblue")
lbl2 = tk.Label(root, text="Right", bg="lightgreen")

lbl1.grid(row=0, column=0, sticky="nsew")
lbl2.grid(row=0, column=1, sticky="nsew")

# Configure how columns expand
root.columnconfigure(0, weight=1)  # left column expands
root.columnconfigure(1, weight=2)  # right column expands twice as much





