import threading
import time
import queue
import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass, asdict

@dataclass
class BotStats:

    total: int = 0
    clicks: int = 0
    types: int = 0
    errors: int = 0
    running: bool = False

class QueueObserver:
    def __init__(self, ui_queue:queue.Queue, stats: BotStats):
        self.ui_queue = ui_queue
        self.stats = stats
        self._lock = threading.Lock()
    
    def update(self, event:dict):
        with self._lock:
            et = event.get("type", "unknown")
            if et == "click":
                self.stats.clicks += 1
            elif et == "type":
                self.stats.types += 1
            elif et == "error":
                self.stats.errors +=1 
            self.stats.total += 1
            self.ui_queue.put(("stats", asdict(self.stats)))
    
class BotWorker:
    def __init__(self, observer, stop_event):
        self.observer = observer
        self.stop_event = stop_event
    
    def run(self):
        self.observer.stats.running = True
        self.observer.ui_queue.put(("status", "Bot:running"))
        actions = ["open", "click", "type", "click", "type", "click"]
        for a in actions:
            if self.stop_event.is_set():
                break
        time.sleep(0.6)
        if a == "click":
            self.observer.update({"type":"click"})
        elif a == "type":
            self.observer.update({"type":"type"})
        else:
            self.observer.update({"type":a})