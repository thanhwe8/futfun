"""
This file contains many utilities that can work indepdently on scripting level to do sniping or bidding with parameters.
The functions should work as pure functional programming approach (of course there are some intermediate variables within some
functions that need to be refactored!)
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from futfun.utils.rng import quick_sleep_gen


def click_left_navigation(
    driver: webdriver.chrome.webdriver.WebDriver, item_name: str
) -> None:
    ITEM_LOOKUP = {
        "Home": 1,
        "Squads": 2,
        "Transfers": 3,
        "Store": 4,
        "Club": 5,
        "SBC": 6,
        "Stadium": 7,
        "Leaderboards": 8,
        "Settings": 9,
    }
    index = ITEM_LOOKUP.get(item_name)
    if index is None:
        logging.critical("Cannot found item_name, please input other")
        return
    else:
        driver.find_element(
            by=By.XPATH, value=f"/html/body/main/section/nav/button[{index}]"
        ).click()


def click_from_transfers(
    driver: webdriver.chrome.webdriver.WebDriver, item_name: str
) -> None:
    ITEM_LOOKUP = {"Search": 2, "Transfer List": 3, "Transfer Targets": 4}
    index = ITEM_LOOKUP.get(item_name)
    if index is None:
        logging.critical("Cannot found item_name, please input other")
        return
    else:
        driver.find_element(
            by=By.XPATH,
            value=f"/html/body/main/section/section/div[2]/div/div/div[{index}]",
        ).click()


def get_coin_having(driver):
    coin_having = driver.find_element(
        By.XPATH, "/html/body/main/section/section/div[1]/div[1]/div[1]"
    ).text
    coin_having = str(coin_having)
    if "," in coin_having:
        coin_having = coin_having.replace(",", "")
    return int(coin_having)


def fill_player_name_in_search(
    driver: webdriver.chrome.webdriver.WebDriver,
    player_name: str = "Ronaldo",
    index_position: int = 1,
) -> None:
    player_name_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/input"
    player_name_selection_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/ul/button[{index_position}]"
    driver.find_element(By.XPATH, player_name_xpath).clear()
    driver.find_element(By.XPATH, player_name_xpath).click()
    driver.find_element(By.XPATH, player_name_xpath).send_keys(player_name)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, player_name_selection_xpath))
    )
    driver.find_element(By.XPATH, player_name_selection_xpath).click()


def select_input_in_search(
    driver: webdriver.chrome.webdriver.WebDriver,
    input_key: str = "Quality",
    input_value: str = "Gold",
) -> None:
    INPUT_KEY_LOOKUP = {
        "Quality": 3,
        "Rarity": 5,
        "Position": 6,
        "Chemistry": 7,
        "Country": 8,
        "League": 9,
        "Club": 10,
        "PlayStyles": 11,
    }
    input_index = INPUT_KEY_LOOKUP[input_key]
    if input_index is None:
        logging.critical(
            f"Cannot found input_key, please try again with following selection {INPUT_KEY_LOOKUP}"
        )
        return
    input_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div"
    list_of_options_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div/ul/li"
    driver.find_element(By.XPATH, input_xpath).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, input_xpath))
    )
    list_of_options = driver.find_elements(By.XPATH, list_of_options_xpath)
    for i in range(1, len(list_of_options) + 1):
        current_element = driver.find_element(
            By.XPATH, list_of_options_xpath + f"[{i}]"
        )
        value_found = current_element.text
        print(value_found)
        if value_found == input_value:
            print(f"Value Found for: {input_value}")
            current_element.click()
            break


def extract_all_filters_in_search(driver: webdriver.chrome.webdriver.WebDriver):
    """
    >>> output = extract_all_filters_in_search(driver)
    >>> container = {}
    >>> for key, value in output.items():
    >>>     if value is not None:
    >>>         df = pd.DataFrame({key:value})
    >>>         container[key] = df
    >>> with pd.ExcelWriter("all_filters.xlsx", engine='xlsxwriter') as writer:
    >>>     for key, value in container.items():
    >>>         value.to_excel(writer, sheet_name=key, index=False)
    """
    INPUT_KEY_LOOKUP = {
        "Quality": 3,
        "Rarity": 5,
        "Position": 6,
        "Chemistry": 7,
        "Country": 8,
        "League": 9,
        "Club": 10,
        "PlayStyles": 11,
    }
    output = {}
    for key, input_index in INPUT_KEY_LOOKUP.items():
        input_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div"
        list_of_options_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div/ul/li"
        driver.find_element(By.XPATH, input_xpath).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_xpath))
        )
        list_of_options = driver.find_elements(By.XPATH, list_of_options_xpath)
        filter_list = []
        for i in range(1, len(list_of_options) + 1):
            current_element = driver.find_element(
                By.XPATH, list_of_options_xpath + f"[{i}]"
            )
            value_found = current_element.text
            filter_list.append(value_found)
        output[key] = filter_list
    return output


# buy and sell interaction
def click_search(driver):
    search_button_xpath = (
        "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]"
    )
    search_button_element = driver.find_element(By.XPATH, search_button_xpath)
    search_button_element.click()


def click_reset(driver):
    reset_button_xpath = (
        "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[1]"
    )
    reset_button_element = driver.find_element(By.XPATH, reset_button_xpath)
    reset_button_element.click()


def set_min_bid(
    driver: webdriver.chrome.webdriver.WebDriver,
    buy_price: int,
    max_min_bid: int = 1000,
) -> None:
    """
    >>> set_min_bid(driver, buy_price=800)
    """
    min_bid_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/input"
    plus_element_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]"
    min_bid_element = driver.find_element(By.XPATH, min_bid_xpath)
    plus_element = driver.find_element(By.XPATH, plus_element_xpath)
    min_bid = min_bid_element.get_attribute("value")
    min_bid = min_bid.replace(",", "")
    if min_bid == "":
        min_bid_element.send_keys("150")
    elif (int(min_bid) < max_min_bid) & (int(min_bid) < buy_price):
        plus_element.click()
    else:
        min_bid_element.clear()


def run_buy_and_store_raw(
    driver: webdriver.chrome.webdriver.WebDriver,
    buy_price: int = 400,
    max_min_bid: int = 1_000,
    first_only: bool = True,
) -> None:
    """
    For 1 snipe
    >>> run_buy_and_store_raw(driver, buy_price=200, max_min_bid=150)

    For buying in bulk:
    >>> for i in range(1,100):
    >>>     if i % 10 == 0:
    >>>         quick_sleep_gen(30.0)
    >>>     else:
    >>>         run_buy_and_store_raw(driver, buy_price=10_000, max_min_bid=150)
    >>>         quick_sleep_gen(3.0)

    """
    min_bid_input_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/input"
    max_bid_input_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/input"
    min_buy_now_input_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/div[1]/div[2]/input"
    max_buy_now_input_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[2]/input"

    max_bid_element = driver.find_element(By.XPATH, max_bid_input_xpath)
    min_buy_now_element = driver.find_element(By.XPATH, min_buy_now_input_xpath)
    max_buy_now_element = driver.find_element(By.XPATH, max_buy_now_input_xpath)

    max_bid_element.clear()
    min_buy_now_element.clear()
    max_buy_now_element.clear()

    set_min_bid(driver=driver, buy_price=buy_price, max_min_bid=max_min_bid)
    max_buy_now_element.send_keys(buy_price)

    reset_button_xpath = (
        "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[1]"
    )
    reset_button_element = driver.find_element(By.XPATH, reset_button_xpath)

    search_button_xpath = (
        "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]"
    )
    search_button_element = driver.find_element(By.XPATH, search_button_xpath)
    search_button_element.click()

    quick_sleep_gen(1.0)

    list_of_cards_xpath = (
        "/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li"
    )
    list_of_cards_element = driver.find_elements(By.XPATH, list_of_cards_xpath)
    total_cards_found = len(list_of_cards_element)

    back_button_xpath = "/html/body/main/section/section/div[1]/button"
    back_button_element = driver.find_element(By.XPATH, back_button_xpath)

    if total_cards_found == 0:
        logging.critical("Nothing found, please-retry")
        quick_sleep_gen(0.5)
        back_button_element.click()
    else:
        for i in range(1, total_cards_found + 1):
            current_card_xpath = f"/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]"
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, current_card_xpath))
            )
            driver.find_element(By.XPATH, current_card_xpath).click()

            # Extract information from current card
            quoted_buy_now_xpath = current_card_xpath + "/div/div[2]/div[3]/span[2]"
            quoted_buy_now_element = driver.find_element(By.XPATH, quoted_buy_now_xpath)
            quoted_buy_now_price = int(quoted_buy_now_element.text.replace(",", ""))
            print(quoted_buy_now_price)

            # Get current available coin
            available_coin_xpath = (
                "/html/body/main/section/section/div[1]/div[1]/div[1]"
            )
            available_coin_element = driver.find_element(By.XPATH, available_coin_xpath)
            available_coin = int(available_coin_element.text.replace(",", ""))

            if available_coin > quoted_buy_now_price:
                # Very important filter to make sure we dont buy ridiculous price due to some ops
                if quoted_buy_now_price <= buy_price:
                    # Click "Buy Now for {coin}"
                    driver.find_element(
                        By.XPATH,
                        "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]",
                    ).click()
                    # Click "OK" from pop up window
                    driver.find_element(
                        By.XPATH, "/html/body/div[4]/section/div/div/button[1]/span[1]"
                    ).click()
                    WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                f"/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]",
                            )
                        )
                    )
                    quick_sleep_gen(1.0)
                    status = driver.find_element(
                        By.XPATH,
                        f"/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]",
                    ).get_attribute("class")
                    print(status)
                    if "won" in status:
                        # "Click Send To Transfer List"
                        driver.find_element(
                            By.XPATH,
                            "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[9]",
                        ).click()
                        print("Card stored successfully")
                        break
                    else:
                        print("Failed to buy the card")
            else:
                print(f"Available coin is not enough: {available_coin}")

            if first_only is True:
                break

        quick_sleep_gen(2)
        back_button_element.click()


def run_buy_and_store_loop(
    driver: webdriver.chrome.webdriver.WebDriver,
    quality: str = None,
    rarity: str = None,
    name: str = None,
    chemistry: str = None,
    position: str = None,
    loop_round: int = 100,
    rest_time: int = 40,
    wait_time: int = 4,
    buy_price: int = 400,
    max_min_bid: int = 1_000,
    first_only: bool = True,
) -> None:
    """
    >>> run_buy_and_store_loop(driver = driver, quality = "Gold", rarity = "Rare", chemistry = "Shadow", position = "Defenders", buy_price = 1_000,max_min_bid = 900)
    """
    click_reset(driver)
    if quality is not None:
        select_input_in_search(driver, "Quality", quality)
    if rarity is not None:
        select_input_in_search(driver, "Rarity", rarity)
    if chemistry is not None:
        select_input_in_search(driver, "Chemistry", chemistry)
    if position is not None:
        select_input_in_search(driver, "Position", position)
    for i in range(1, loop_round):
        if i % 40 == 0:
            quick_sleep_gen(rest_time)
        else:
            run_buy_and_store_raw(driver, buy_price=buy_price, max_min_bid=max_min_bid, first_only=first_only)
            quick_sleep_gen(wait_time)




run_buy_and_store_loop(driver = driver, quality = "Gold", rarity = "Rare", chemistry = "Shadow", position = "Defenders", buy_price = 1_000,max_min_bid = 900)