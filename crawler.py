from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import pandas as pd
from selenium.webdriver.common.keys import Keys
xpath = {
    'google_search':'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input',
    'next_google_search':'//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input',
    'google_map_search':'//*[@id="searchboxinput"]',
    'map_result':'section-result-content'

}
google_map_url = 'https://www.google.com/maps'
browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
browser.get('https://google.com')
time.sleep(2)
google_search_input = browser.find_element_by_xpath(xpath['google_search'])
google_search_input.send_keys('Hello World')
google_search_input.send_keys(Keys.ENTER)
time.sleep(5)
google_search_input = browser.find_element_by_xpath(xpath['next_google_search'])
google_search_input.clear()
google_search_input.send_keys('World')
google_search_input.send_keys(Keys.ENTER)
browser.execute_script("window.open('');")
browser.switch_to_window(browser.window_handles[-1])
browser.get(google_map_url)
google_map_search_input = browser.find_element_by_xpath(xpath['google_map_search'])
google_map_search_input.send_keys('Burgur shop near me')
google_map_search_input.send_keys(Keys.ENTER)
time.sleep(10)
result_divs = browser.find_elements_by_class_name(xpath['map_result'])
print(len(result_divs))
result_divs[1].click()

# browser.close()
