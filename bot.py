from selenium import webdriver
import selenium.webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)

siteurl = "https://www.amazon.com/gp/product/B00CHEIO6Y/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00CHEIO6Y&linkCode=as2&tag=nomadayt-20&linkId=QXWQ4LH4DUQ5S3ZN"

dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 "
"(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")


def convertHeadless(driver, url):
    cookies = driver.get_cookies()
    driver.quit()
    driver = webdriver.Firefox()
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url)
    return driver

driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.set_window_size(700,500)
driver.get(siteurl)

driver.find_element_by_id("add-to-cart-button").click()
print"it worked "