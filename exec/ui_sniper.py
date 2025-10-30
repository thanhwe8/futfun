from futfun.controllers.sniper import *
from futfun.views.sniper import *
from futfun.models.tools import *

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MVC Sniper")

    sniper_view = QuickSnipe(master=root)
    sniper_controller = Sniper(view = sniper_view)
    
    root.mainloop()