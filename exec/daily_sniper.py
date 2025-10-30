import pytest
from futfun.models.tools import *

driver = webdriver.Chrome()
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")

run_buy_and_sell_loop(
    driver=driver,
    name="Cristiano Ronaldo",
    quality="Gold",
    rarity="Rare",
    chemistry="Hunter",
    buy_price=4_500,
    sell_price=4_900,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)





