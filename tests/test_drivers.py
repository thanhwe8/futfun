"""
This file is not supposed to be tested with pytest but rather than UI test
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")


def click_left_navigation(driver:webdriver.chrome.webdriver.WebDriver, item_name:str) -> None:
    ITEM_LOOKUP = {
        'Home':1,
        'Squads':2,
        'Transfers':3,
        'Store':4,
        'Club':5,
        'SBC':6,
        'Stadium':7,
        'Leaderboards':8,
        'Settings':9
    }
    index = ITEM_LOOKUP.get(item_name)
    if index is None:
        logging.critical("Cannot found item_name, please input other")
        return
    else:
        driver.find_element(by=By.XPATH, value=f'/html/body/main/section/nav/button[{index}]').click()

def click_from_transfers(driver:webdriver.chrome.webdriver.WebDriver, item_name:str) -> None:
    ITEM_LOOKUP = {
        'Search':2,
        'Transfer List':3,
        'Transfer Targets':4
    }
    index = ITEM_LOOKUP.get(item_name)
    if index is None:
        logging.critical("Cannot found item_name, please input other")
        return
    else:
        driver.find_element(by=By.XPATH, value=f'/html/body/main/section/section/div[2]/div/div/div[{index}]').click()

def get_coin_having(driver):
    coin_having = driver.find_element(By.XPATH, '/html/body/main/section/section/div[1]/div[1]/div[1]').text
    coin_having = str(coin_having)
    if "," in coin_having:
        coin_having = coin_having.replace(",", "")
    return int(coin_having)

def fill_player_name_in_search(driver:webdriver.chrome.webdriver.WebDriver, player_name:str="Ronaldo", index_position:int=1) -> None:
    player_name_xpath = '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/input'
    player_name_selection_xpath = f'/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/ul/button[{index_position}]'
    driver.find_element(By.XPATH, player_name_xpath).clear()
    driver.find_element(By.XPATH, player_name_xpath).click()
    driver.find_element(By.XPATH, player_name_xpath).send_keys(player_name)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, player_name_selection_xpath)))
    driver.find_element(By.XPATH, player_name_selection_xpath).click()

def select_input_in_search(driver:webdriver.chrome.webdriver.WebDriver, input_key:str="Quality", input_value:str="Gold") -> None:
    INPUT_KEY_LOOKUP = {
        "Quality":3,
        "Rarity":5,
        "Position":6,
        "Chemistry":7,
        "Country":8,
        "League":9,
        "Club":10,
        "PlayStyles":11
    }
    input_index = INPUT_KEY_LOOKUP[input_key]
    if input_index is None:
        logging.critical(f"Cannot found input_key, please try again with following selection {INPUT_KEY_LOOKUP}")
        return
    input_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div"
    list_of_options_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div/ul/li"
    driver.find_element(By.XPATH, input_xpath).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
    list_of_options = driver.find_elements(By.XPATH, list_of_options_xpath)
    for i in range(1, len(list_of_options)+1):
        current_element = driver.find_element(By.XPATH, list_of_options_xpath + f'[{i}]')
        value_found = current_element.text
        print(value_found)
        if value_found == input_value:
            print(f"Value Found for: {input_value}")
            current_element.click()
            break

def extract_all_filters_in_search(driver:webdriver.chrome.webdriver.WebDriver):
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
        "Quality":3,
        "Rarity":5,
        "Position":6,
        "Chemistry":7,
        "Country":8,
        "League":9,
        "Club":10,
        "PlayStyles":11
    }
    output = {}
    for key, input_index in INPUT_KEY_LOOKUP.items():
        input_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div"
        list_of_options_xpath = f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{input_index}]/div/ul/li"
        driver.find_element(By.XPATH, input_xpath).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
        list_of_options = driver.find_elements(By.XPATH, list_of_options_xpath)
        filter_list = []
        for i in range(1, len(list_of_options)+1):
            current_element = driver.find_element(By.XPATH, list_of_options_xpath + f'[{i}]')
            value_found = current_element.text
            filter_list.append(value_found)
        output[key] = filter_list
    return output


# Price action
def set_min_bid(driver, buy_price:int, max_min_bid:int = 1000) -> None:
    """
    >>> set_min_bid(driver, buy_price=800)
    """
    min_bid_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/input"
    plus_element_xpath = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]"
    min_bid_element = driver.find_element(By.XPATH, min_bid_xpath)
    plus_element = driver.find_element(By.XPATH, plus_element_xpath)
    min_bid = min_bid_element.get_attribute('value')
    min_bid = min_bid.replace(",", "")
    if min_bid == "":
        min_bid_element.send_keys("150")
    elif (int(min_bid) <= max_min_bid) & (int(min_bid) < buy_price):
        plus_element.click()
    else:
        min_bid_element.clear()



def buy_and_store_without_filter(driver, buy_price:int=400.0, max_min_bid_config:int=1000, first_only:bool = True) -> None:
    pass



driver.execute_script("document.body.style.zoom='80%'")

