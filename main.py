from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

chrome_driver_path = "/Users/elenaalvarezortega/Desktop/Udemy/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

game_is_on = True
items = driver.find_elements(By.ID, "store")
cookie = driver.find_element(By.ID, "cookie")
items_list = []
prices = []

# Get a list with all the items that are able to purchase
for item in items:
    items_list.append(item.text)
new_list = items_list[0].split("\n")
upgrade_list = [new_list[index] for index in range(len(new_list)) if index % 2 == 0]
element_list = []

# Reverse the list so the most expensive items will be the first ones in the list and from there create a dictionary
# with the item name and its price
for element in upgrade_list[::-1]:
    element_list.append(element.replace(",", "").split("-"))
shopping_items = dict((x, y) for x, y in element_list)
print(shopping_items)

time_check = time.time() + 5
stop_time = time.time() + (60*5)

while game_is_on:
    cookie.click()
    money = int(driver.find_element(By.ID, "money").text)

    # Check every 5 second what items are available to purchase, getting the most expensive one over the other ones
    if time.time() > time_check:
        for key, value in shopping_items.items():
            if money >= int(value):
                print(money)
                affordable_item = str(key).replace(" ", "")
                print(affordable_item)
                new_buy = driver.find_element(By.ID, f"buy{affordable_item}")
                new_buy.click()

    # After 5 minutes of automatically running the game, return the 'cookies/second' data
    if time.time() > stop_time:
        cookies_per_sec = driver.find_element(By.ID, "cps").text
        print(cookies_per_sec)
        driver.quit()
