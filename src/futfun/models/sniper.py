import logging
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from futfun.models.tools import *
from futfun.utils.rng import quick_sleep_gen
from futfun.utils.logger_setup import get_logger
from futfun.utils.observer import SeleniumObserver


class SniperBot:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.ea.com/ea-sports-fc/ultimate-team/web-app/"
        self.logger = get_logger(self.__class__.__name__, log_prefix="SniperBot")
        self.observer = SeleniumObserver()

    def run_buy_and_store_single(self, buy_price=400, max_min_bid=1_000, first_only=True) -> None:
        driver = self.driver()
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

        reset_button_xpath = ("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[1]")
        reset_button_element = driver.find_element(By.XPATH, reset_button_xpath)

        search_button_xpath = ("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
        search_button_element = driver.find_element(By.XPATH, search_button_xpath)
        search_button_element.click()
        self.observer.update_search()
        quick_sleep_gen(1.0)

        list_of_cards_xpath = ("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li")
        list_of_cards_element = driver.find_elements(By.XPATH, list_of_cards_xpath)
        total_cards_found = len(list_of_cards_element)

        back_button_xpath = "/html/body/main/section/section/div[1]/button"
        back_button_element = driver.find_element(By.XPATH, back_button_xpath)

        if total_cards_found == 0:
            logger.critical("Nothing found, please-retry")
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
                        now = datetime.now()
                        current_time = now.strftime("%H_%M_%S")
                        current_time = str(current_time)
                        file_name = current_time + ".png"
                        driver.save_screenshot(r"./Output/{}".format(file_name))
                        saved_path = r"./Output/{}".format(file_name)
                        print(saved_path)
                        if "won" in status:
                            self.observer.update_bought()
                            # "Click Send To Transfer List"
                            driver.find_element(
                                By.XPATH,
                                "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[9]",
                            ).click()
                            self.logger.info("Card stored successfully")
                            break
                        else:
                            self.observer.update_missed()
                            print("Failed to buy the card")
                else:
                    self.logger.info(f"Available coin is not enough: {available_coin}")

                if first_only is True:
                    break



