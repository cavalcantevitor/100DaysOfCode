import time
from selenium import webdriver
from selenium.webdriver.common.by import By

timeout = 300
starting_time = time.time()
ending_time = starting_time + timeout
execution_counter = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
prices = driver.find_elements(By.CSS_SELECTOR, value="#store div b")

item_id_list = []
for item in items:
    item_id = item.get_attribute("id")
    item_id_list.append(item_id)

price_list = []
for price in prices:
    if price.text != "":
        price_text = price.text
        simple_price_text = price_text.replace(",", "")
        split_price_text = simple_price_text.split()
        price_list.append(int(split_price_text[-1]))


def check_balance():
    money = driver.find_element(By.ID, value="money").text
    simple_money_text = money.replace(",", "")
    return int(simple_money_text)


def buy_upgrade():
    current_money = check_balance()
    affordable_items = []
    for item_price in price_list:
        if current_money > item_price:
            affordable_items.append(item_price)

    if len(affordable_items) > 0:
        affordable = max(affordable_items)
        price_index = price_list.index(affordable)
        driver.find_element(By.ID, value=item_id_list[price_index]).click()


while time.time() < ending_time:
    # Check if 5 seconds have passed since the last function execution
    if time.time() >= starting_time + execution_counter * 5:
        buy_upgrade()

        execution_counter += 1
    cookie.click()

print(driver.find_element(By.ID, value="cps").text)
driver.quit()