import logging
from datetime import datetime
from pathlib import Path

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog

BIG_FONT = ("Helvetica", "30")
SMALL_FONT = ("Helvetica", "15")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOG_DIR = BASE_DIR / "logging"
LOG_DIR.mkdir(exist_ok=True)

today_str = datetime.now().strftime("%Y%m%d")
log_filename = LOG_DIR / f"{today_str}_futfun.app"


# Setup logger for view
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler (append mode set)
file_handler = logging.FileHandler(log_filename, mode="a")
file_handler.setLevel(logging.INFO)

# Console handler (print out terminal console)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


class QuickSnipe(tk.Frame):

    def __init__(self, master=None):

        self.labels = {}
        self.entries = {}
        self.buttons = {}

        super().__init__(master)
        self.master = master
        self.grid(padx=20, pady=20, sticky="nsew")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.create_widgets()
        self._enable_copy_paste()

    def create_widgets(self):
        label_entry_map = {
            "Player Name": ["name","Cristiano Ronaldo"],
            "Quality": ["quality", "Gold"],
            "Rarity": ["rarity", "Rare"],
            "Chemistry": ["chemistry", ""],
            "Position": ["position", ""],
            "Country": ["country", ""],
            "Buy Now Price": ["buy_price", ""],
            "Sell Price": ["sell_price", ""],
            "Max Min Price": ["max_min_price", 1000],
            "Number of iterations": ["loop_round",500],
            "Rest in Seconds": ["rest_time",4]
        }


        for i, (label, entry) in enumerate(label_entry_map.items()):
            # Create labels
            lbl = ttk.Label(self, text=label)
            lbl.grid(row=i, column=0, stick="w", padx=5, pady=5)
            self.labels[label] = lbl

            # Create entries
            etr = ttk.Entry(self)
            etr.grid(row=i, column=1, sticky="ew", padx=5, pady=5)
            etr.insert(0, str(entry[1]))
            self.entries[entry[0]] = etr

        self.buttons["submit"] = ttk.Button(self, text="Submit")
        self.buttons["submit"].grid(
            row=len(label_entry_map), column=0, sticky="ew", padx=5, pady=(10, 5)
        )

        self.buttons["clear"] = ttk.Button(
            self, text="Clear", command=self.clear_entries
        )
        self.buttons["clear"].grid(
            row=len(label_entry_map), column=1, sticky="ew", padx=5, pady=(10, 5)
        )

    def _enable_copy_paste(self):
        for entry in self.entries.values():
            # macOS bindings
            entry.bind("<Command-a>", lambda e: entry.select_range(0, 'end'))
            entry.bind("<Command-c>", lambda e: entry.event_generate("<<Copy>>"))
            entry.bind("<Command-v>", lambda e: entry.event_generate("<<Paste>>"))
            entry.bind("<Command-x>", lambda e: entry.event_generate("<<Cut>>"))

            # Windows/Linux bindings
            entry.bind("<Control-a>", lambda e: entry.select_range(0, 'end'))
            entry.bind("<Control-c>", lambda e: entry.event_generate("<<Copy>>"))
            entry.bind("<Control-v>", lambda e: entry.event_generate("<<Paste>>"))
            entry.bind("<Control-x>", lambda e: entry.event_generate("<<Cut>>"))


    def clear_entries(self):
        for entry in self.entries.values():
            # logger.info(entry.get() +  " deleted")  # Only include when needed
            entry.delete(0, tk.END)

    def get_entries(self):
        result = {}
        for key, entry in self.entries.items():
            value = entry.get()
            result[key] = value if value != "" else None
        logging.info(result)
        return result
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snipe View Example")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = QuickSnipe(master=root)
    print(app.entries)
    print(app.labels)
    print(app.buttons)
    root.mainloop()
