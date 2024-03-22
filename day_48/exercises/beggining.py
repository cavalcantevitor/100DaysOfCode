from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li a")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")

events = {}
for i in range(len(event_names)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }

print(events)