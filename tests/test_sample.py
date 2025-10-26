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
    buy_price=6300,
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
    buy_price=6_100,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50,
)

# Cristiano Ronaldo
run_buy_and_store_loop(
    driver=driver,
    name="Cristiano Ronaldo",
    quality="Gold",
    rarity="Rare",
    chemistry="Hunter",
    buy_price=5_000,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50
)

run_buy_and_store_loop(
    driver=driver,
    name="Cristiano Ronaldo",
    quality="Gold",
    rarity="Rare",
    chemistry="Hunter",
    buy_price=4200,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50
)

run_buy_and_store_loop(
    driver=driver,
    name="Antoine Griezmann",
    quality="Gold",
    rarity="Rare",
    chemistry="Hunter",
    buy_price=3_800,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50
)

run_buy_and_store_loop(
    driver=driver,
    name="Bryan Mbeumo",
    quality="Gold",
    rarity="Rare",
    chemistry="Hunter",
    buy_price=4600,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50
)




run_buy_and_store_loop(
    driver=driver,
    name="Dumfries",
    quality="Gold",
    rarity="Rare",
    chemistry="Shadow",
    buy_price=1500,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50
)


run_buy_and_store_loop(
    driver=driver,
    name="Sam Kerr",
    quality="Gold",
    rarity="Rare",
    buy_price=12_500,
    max_min_bid=600,
    loop_round=100,
    rest_time=50
)


run_buy_and_sell_loop(
    driver=driver,
    name="Dumfries",
    quality="Gold",
    rarity="Rare",
    chemistry="Shadow",
    buy_price=1500,
    max_min_bid=600,
    loop_round=1000,
    rest_time=50
)