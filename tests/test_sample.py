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
    country="Italy",
    buy_price=11_500,
    max_min_bid=1_000,
    loop_round=1000,
    rest_time=50,
)

run_buy_and_store_loop(
    driver=driver,
    quality="Gold",
    rarity="Rare",
    chemistry="Shadow",
    position="Defenders",
    buy_price=900,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)

run_buy_and_store_loop(
    driver=driver,
    quality="Gold",
    rarity="Rare",
    country="England",
    position="GK",
    league="Premier League (ENG 1)",
    buy_price=800,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)


run_buy_and_store_loop(
    driver=driver,
    name="Barella",
    quality="Gold",
    rarity="Rare",
    chemistry="Shadow",
    buy_price=17_500,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)


run_buy_and_store_loop(
    driver=driver,
    name="Stegen",
    quality="Gold",
    rarity="Rare",
    # chemistry="Shadow",
    buy_price=6_700,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)



run_buy_and_store_loop(
    driver=driver,
    name="Buhl",
    quality="Gold",
    rarity="Rare",
    # chemistry="Shadow",
    buy_price=6_700,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)