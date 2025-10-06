from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import exepected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")