from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog

BIG_FONT = ('Helvetica', '30')
SMALL_FONT = ('Helvetica', '15')

class QuickSnipe:

    def __init__(self, master, bootstyle):
        self.label = {}
        self.combo_boxes = {}
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky='NSEW')
    
    def gen_label_entry(self, master, entry_name, width=20):
        pass