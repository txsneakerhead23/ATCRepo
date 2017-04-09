#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pause, datetime, time, requests
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from threading import *
from config import *
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

print "Hello and Welcome to v3 of GSPreme Script!"
print "Starting..."
thechecker = 0

time.sleep(2)

testmode = raw_input("testmode?:")
items = 0
token_list = []
def tryagain():
    global items
    items = int(raw_input("How many items?:"))
    if items > 4:
        print "More that four items makes the bot run slower and decreases your chances of getting anything!"
        tryagain()
    else:
        pass
tryagain()

productdatalist = []


print "When answering the following questions, please input the most hyped item(s) first."

for i in xrange(items):
    counter = int(i) + 1
    datalist = []
    kword = "First Keyword for item %s :" % counter
    kword1 = "Second Keyword for item %s :" % counter
    keyword1 = raw_input(kword)
    keyword2 = raw_input(kword1)
    category = raw_input("Item category:")
    color = raw_input("Color:")
    size = raw_input("Size(If not applicable, please just say no):")
    datalist.append(keyword1)
    datalist.append(keyword2)
    datalist.append(color)
    datalist.append(category)
    datalist.append(size)
    if str(size) == "no" or str(size) == "No":
        datalist.pop()
    else:
        pass
    productdatalist.append(datalist)

datadir = "user-data-dir=" + str(path)

options = Options()
options.add_argument(datadir)

now = datetime.datetime.now()
tenam = now.replace(hour=10, minute=59, second=00, microsecond=0)
elevenam = now.replace(hour=11, minute=0, second=3, microsecond=0)
if testmode == "no":
    print "The bot will pause until %s, then an instance of Chrome will start; do not close the bot or your computer." % tenam
    pause.until(tenam)
else:
    pass

driver = webdriver.Chrome(chrome_options=options)
baseurl = "http://www.supremenewyork.com/shop/all/"
def waitfunction():
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'container')))
def waitfunctioncart():
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'continue')))
def waitfunctioncheckout():
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button')))
def refreshfunc():
    driver.refresh()
def find(item):
    driver.get(baseurl + str(item[3]))
    waitfunction()
    while True:
        waitfunction()
        now = datetime.datetime.now()
        if now < elevenam:
            try:
                driver.implicitly_wait(2)
                driver.find_element_by_partial_link_text(item[0]).click()
                finalize(item)
                break
            except NoSuchElementException:
                refreshfunc()
            except (ElementNotVisibleException, StaleElementReferenceException):
                try:
                    driver.implicitly_wait(3)
                    driver.find_element_by_partial_link_text(item[1]).click()
                    finalize(item)
                    break
                except (ElementNotVisibleException, StaleElementReferenceException, NoSuchElementException):
                    print "Cannot find item one, trying to find item two..."
                    break
        else:
            try:
                driver.implicitly_wait(2)
                driver.find_element_by_partial_link_text(item[0]).click()
                finalize(item)
                break
            except (StaleElementReferenceException, ElementNotVisibleException, NoSuchElementException):
                try:
                    driver.implicitly_wait(2)
                    driver.find_element_by_partial_link_text(item[1]).click()
                    finalize(item)
                    break
                except (StaleElementReferenceException, ElementNotVisibleException, NoSuchElementException):
                    print "Cannot find item one, trying to find item two..."
                    break

def finalize(item):
    checker()
    waitfunctioncart()
    try:
        driver.implicitly_wait(2)
        driver.find_element_by_xpath(str("//a[@data-style-name=" + str("'") + str(item[2]) + str("'") + str("]"))).click()
    except:
        print "color selection failed for item one, getting default color"
    if len(item) is 4:
        try:
            driver.implicitly_wait(.25)
            thing = Select(driver.find_element_by_id("size"))
            thing.select_by_visible_text(item[2])
        except:
            try:
                driver.implicitly_wait(.25)
                thing = Select(driver.find_element_by_id("size"))
                thing.select_by_visible_text(item[2])
            except:
                print "Getting available size"
    else:
        pass
    while True:
        try:
            driver.implicitly_wait(2)
            driver.find_element_by_css_selector('input.button').click()
            break
        except:
            if int(items) == 1:
                refreshfunc()
            else:
                try:
                    driver.implicitly_wait(3)
                    driver.find_element_by_css_selector('input.button').click()
                except:
                    print "Cannot add this item to cart, trying to get another item"
                    break

def checkout():
    driver.get("http://www.supremenewyork.com/checkout")
    checker()
    time.sleep(.1)
    if thechecker == 1:
        return
    else:
        pass
    waitfunctioncheckout()
    try:
        driver.implicitly_wait(2)
        elemen = driver.find_elements_by_class_name('iCheck-helper')
        for i in elemen:
            i.click()

    except NoSuchElementException:
        print "PLEASE AGREE TO TERMS AND CONDITIONS BY CLICKING THE CHECKBOX"
    if str(testmode) == "no":
        injectionpayload()
    else:
        pass
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("errors")
        backupcheckout()
        injectionpayload()
    except:
        print "Bot complete, enjoy your items!"
def backupcheckout():
    while True:
        driver.implicitly_wait(2)
        inputs = driver.find_elements_by_tag_name("input")
        inputs[2].clear()
        inputs[3].clear()
        inputs[4].clear()
        inputs[5].clear()
        inputs[7].clear()
        inputs[12].clear()
        inputs[13].clear()

        inputs[2].send_keys(name)
        inputs[3].send_keys(email)
        inputs[5].send_keys(address)
        inputs[7].send_keys(zipe)
        inputs[12].send_keys(ccnumber)
        inputs[12].clear()
        time.sleep(.5)
        inputs[12].send_keys(ccnumber)
        inputs[13].send_keys(cvv)
        try:
            driver.implicitly_wait(5)
            driver.find_element_by_class_name("errors")
            pass
        except:
            print "Checkout complete! Enjoy!"
            break

def captcha(num):
    while True:
        r  = requests.post("http://api.captchasolutions.com/solve", data={'p':'nocaptcha', 'googlekey':'6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz', 'pageurl':'https://www.supremenewyork.com/checkout', 'key':key, 'secret':secret, 'out':'text'})
        txt = r.text
        token = str(txt)
        if "03" not in token:
            print "First time getting token failed. Trying again."
            pass
        else:
            print "Extracted captcha token successfully. CAPTCHA token: %s" % token
            token_list.append(token)
            if num == 1:
                break
            else:
                pass

def injectionpayload():
    driver.implicitly_wait(3)
    driver.execute_script("document.getElementById('g-recaptcha-response').style.display = 'unset';")
    driver.implicitly_wait(3)
    driver.find_element_by_tag_name("textarea").send_keys(token_list[-1])
    driver.implicitly_wait(3)
    driver.execute_script("document.getElementById('checkout_form').submit()")

captcha(1)
def themain():
    global start_time
    start_time = time.time()
    for item in productdatalist:
        checker()
        time.sleep(.1)
        if thechecker == 1:
            return
        else:
            pass
        find(item)
    checkout()
    print "--- %s seconds ---" % (time.time() - start_time)
def checker():
    base = "http://www.supremenewyork.com"
    if driver.current_url == base + "/shop" or driver.current_url == base + "/index" or driver.current_url == base:
        thechecker += 1
        driver.get(base + "/shop/all")
        waitfunction()
        try:
            driver.implicitly_wait(2)
            driver.find_element_by_id("cart")
            checkout()
        except:
            themain()
    else:
        pass

if __name__ == "__main__":
    Thread(target=themain).start()
    Thread(target=captcha(2)).start()













