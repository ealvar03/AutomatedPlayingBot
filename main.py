from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from functions import get_numbers
import time

# 1. Create connection with HTML code
# 2. Obtain all the available items and its price
#       - Create a function that generates a list with the buyable items and reverse it (more expensive > cheaper)
#       - Create dictionary from list with name of  items as keys, and prices as values
# 3. Create a loop to control the click on the screen with a while loop
# 4. Create two counters for time (time_check that check every 5 seconds; and stop_time for 5min)
# 5. Check if 5 seconds have passed (if time.time() > time_check), and if yes, then follow the purchaseable process
#



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

for item in items:
    items_list.append(item.text)
new_list = items_list[0].split("\n")
upgrade_list = [new_list[index] for index in range(len(new_list)) if index % 2 == 0]
for element in upgrade_list[::-1]:
    print(element.replace(",", "").split("-"))
    shopping_items = dict()

for item in upgrade_list[::-1]:
    prices.append(int(get_numbers(item)))

# while game_is_on:
#     cookie.click()
#     money = int(driver.find_element(By.ID, "money").text)

time_check = time.time() + 5
print(time_check)
print(time.time())
stop_time = time.time() + (60*5)



driver.quit()
