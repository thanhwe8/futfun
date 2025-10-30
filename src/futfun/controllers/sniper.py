from futfun.views.sniper import *
from futfun.models.tools import *

class Sniper:
    def __init__(self,view):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")
        self.view = view
        self.bind_view()

    def click_submit(self):
        entries_values = self.view.get_entries()
        entries_values['driver'] = self.driver
        run_buy_and_sell_loop(**entries_values)
    
    def bind_view(self):
        self.view.buttons["submit"].config(command=self.click_submit)