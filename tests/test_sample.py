import pytest
from futfun.models.tools import *

driver = webdriver.Chrome()
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")

run_buy_and_store_loop(
    driver=driver,
    # quality="Gold",
    rarity="Cornerstones",
    chemistry="Shadow",
    position="Defenders",
    buy_price=11_000,
    max_min_bid=1_000,
    loop_round=1000,
    rest_time=50,
)

run_buy_and_store_loop(
    driver=driver,
    quality="Gold",
    rarity="Rare",
    chemistry="Shadow",
    position="RB",
    buy_price=1_000,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)