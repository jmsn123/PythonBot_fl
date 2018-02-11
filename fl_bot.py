from selenium.webdriver.support import ui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
from pprint import pprint

def get_page(model, sku):
    url = "https://www.footlocker.com/product/model:"+str(model)+"/sku:"+ str(sku)+"/"
    return url

data = json.load(open('info.json'))

browser = webdriver.Firefox()

page=browser.get(get_page(277097,"8448001"))

browser.find_element_by_xpath("//*[@id='pdp_size_select_mask']").click()

shoesize = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.grid_size:nth-child(8)')))

shoesize.click()

browser.find_element_by_xpath("//*[@id='pdp_addtocart_button']").click()

browser.get('https://www.footlocker.com/shoppingcart/default.cfm?sku=')

browser.find_element_by_css_selector('#cart_checkout_button').click()
'''
ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='billFirstName']")))

add = browser.find_element_by_xpath("//input[@id='billFirstName']").click()
print(add.is_displayed());


'''


for info, value in data.items():
    ele = ui.WebDriverWait(browser, 90).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='"+info+"']")))
    print(info)
    #ele.click()
    #ele.clear()
    #ele.send_keys(value)
'''
ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='billAdress1']")))
browser.find_element_by_xpath("//input[@id='billAdress1']").click()
browser.find_element_by_xpath("//input[@id='billAdress1']").clear()
browser.find_element_by_xpath("//input[@id='billAdress1']").send_keys("user_first_name")
#ui.WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "billFirstName")))
'''
#browser.find_element_by_id("#billFirstName").send_keys(Keys.RETURN)

#firstname = browser.find_element_by_id('#billFirstName')

#ui.WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "#billFirstName")))

#browser.find_element_by_id("#billFirstName").send_keys(" and some", Keys.ARROW_DOWN)


#finish this code and getting json
 