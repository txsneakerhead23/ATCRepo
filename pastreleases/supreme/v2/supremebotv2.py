#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import datetime, pause, pickle, time, requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from threading import Thread
from config import *


now = datetime.datetime.now()
tenam = now.replace(hour=10, minute=59, second=00, microsecond=0)
elevenam = now.replace(hour=11, minute=0, second=3, microsecond=0)

print "It is now %s" % now
print "I will start at %s (assuming you say no to test mode). But first, some questions:" % tenam

testmode = raw_input("testmode(WARNING: saying 'no' to this question will prompt the bot to checkout with anything in your cart and with the info autofilled on the checkout page.)?:")
items = raw_input("How many items?:")
kword1 = raw_input("First Keyword for item one:")
kword2 = raw_input("Second Keyword for item one:")
cat1 = raw_input("Category of item one?:")
color1 = raw_input("Color of item one?:")
checksizeone = raw_input("Sized product for item one?:")
if str(checksizeone) == "yes":
    size1 = raw_input("What size?:")
else:
    pass

if int(items) != 1:
    kword3 = raw_input("First Keyword for item two:")
    kword4 = raw_input("Second keyword for item two:")
    cat2 = raw_input("Category of item two?:")
    color2 = raw_input("Color of item two?:")
    checksizetwo = raw_input("Is this a sized product?:")
    if str(checksizetwo) == "yes":
        size2 = raw_input("What size?:")
    else:
        pass

else:
    pass
options = Options()
if str(operatingsystem) == "Linux" or "Mac":
    datadir = "--user-data-dir=" + str(path)
else:
    datadir = "user-data-dir=" + str(path)

datadir.replace('Default', '')
    

options.add_argument(datadir)
raw_input("Press <enter> to start")
driver = webdriver.Chrome(chrome_options=options)

if testmode == "no":
    pause.until(tenam)
else:
    pass


def waitfunction():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop" or str(driver.current_url) == "http://www.supremenewyork.com/index":
        itemone()
        return
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'container')))
def waitfunctioncart():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop" or str(driver.current_url) == "http://www.supremenewyork.com/index":
        itemone()
        return
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'continue')))
def waitfunctioncheckout():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop" or str(driver.current_url) == "http://www.supremenewyork.com/index":
        itemone()
        return
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button')))
def refreshfunc():
    driver.refresh()

def itemone():
    counter = 0
    driver.get("http://www.supremenewyork.com/shop/all/" + str(cat1))
    global start_time
    start_time = time.time()
    while True:
        print "Trying to find item one"
        current_time = datetime.datetime.now()
        if current_time < elevenam:
            refreshfunc()
            waitfunction()
            try:
                driver.implicitly_wait(1)
                driver.find_element_by_partial_link_text(kword1).click()
                counter += 1
                break
            except:
                pass

        else:
            try:
                waitfunction()
                driver.implicitly_wait(3)
                driver.find_element_by_partial_link_text(kword1).click()
                counter += 1
                break
            except NoSuchElementException:
                try:
                    driver.implicitly_wait(.5)
                    driver.find_element_by_partial_link_text(kword2).click()
                    counter += 1
                    break
                except NoSuchElementException:
                    counter += 2
                    break
                except (StaleElementReferenceException, ElementNotVisibleException):
                    refreshfunc()
            except (StaleElementReferenceException, ElementNotVisibleException):
                refreshfunc()
    if int(counter) == 1:
        itemonecolor()
    elif int(counter) == 2 and int(items) == 2:
        itemtwo()
    elif int(counter) == 2 and int(items) != 2:
        refreshfunc()
    else:
        pass

def itemonecolor():
    waitfunctioncart()
    if str(driver.current_url) == "http://www.supremenewyork.com/shop" or str(driver.current_url) == "http://www.supremenewyork.com/index":
        itemone()
        return
    try:
        driver.implicitly_wait(2)
        driver.find_element_by_xpath(str("//a[@data-style-name=" + str("'") + str(color1) + str("'") + str("]"))).click()
    except:
        print "color selection failed for item one, getting default color"
    if checksizeone == "yes":
        try:
            driver.implicitly_wait(.25)
            thing = Select(driver.find_element_by_id("size"))
            thing.select_by_visible_text(size1)
        except:
            try:
                driver.implicitly_wait(.25)
                thing = Select(driver.find_element_by_id("size"))
                thing.select_by_visible_text(size1)
            except:
                print "getting default size(small)"
    else:
        pass


    addtocart(1)
    try:
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    except WebDriverException:
        print "cookie loading failed"
    if int(items) == 1:
        checkout()
        return
    elif str(items) == "1":
        checkout()
        return
    else:
        itemtwo()


def itemtwo():
    cookies = pickle.load(open("cookies.pkl", "rb"))
    try:
        for cookie in cookies:
            driver.add_cookie(cookie)
    except WebDriverException:
        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
        except WebDriverException:
            print "cookie loading failed"
    driver.get("http://www.supremenewyork.com/shop/all/" + str(cat2))
    if str(driver.current_url) == "http://www.supremenewyork.com/shop" or str(driver.current_url) == "http://www.supremenewyork.com/index":
        itemtwo()
        return
    waitfunction()
    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_partial_link_text(kword3).click()
        print "found item two, trying to add it to your cart"
        itemtwocolor()
    except:
        try:
            driver.implicitly_wait(.25)
            driver.find_element_by_partial_link_text(kword4).click()
            print "found item two, trying to add it to your cart"
            itemtwocolor()
        except:
            checkout()


def itemtwocolor():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop" or str(driver.current_url) == "http://www.supremenewyork.com/index":
        itemtwo()
        return
    waitfunctioncart()
    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_xpath(str("//a[@data-style-name=" + str("'") + str(color2) + str("'") + str("]"))).click()
    except:
        print "color selection failed for item two, getting default color"
    if checksizetwo == "yes":

        try:
            print "trying to get requested size"
            driver.implicitly_wait(.5)
            thing = Select(driver.find_element_by_id("size"))
            thing.select_by_visible_text(size2)
        except:
            try:
                driver.implicitly_wait(1)
                thing = Select(driver.find_element_by_id("size"))
                thing.select_by_visible_text(size2)
            except:
                print "Could not find requested size-getting default size"
    else:
        pass
    addtocart(2)
    checkout()

def addtocart(cart):
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return
    waitfunctioncart()
    while True:
        if str(items) == "1" or int(items) == 1:
            try:
                driver.implicitly_wait(.25)
                driver.find_element_by_css_selector('input.button').click()
                break
            except (ElementNotVisibleException, StaleElementReferenceException):
                driver.implicitly_wait(5)
                driver.find_element_by_css_selector('input.button').click()
                break
            except NoSuchElementException:
                refreshfunc()

        else:
            try:
                driver.implicitly_wait(2)
                driver.find_element_by_id("cart")
                try:
                    driver.implicitly_wait(2)
                    driver.find_element_by_css_selector('input.button').click()
                except:
                    break


            except:
                if int(cart) == 2:
                    try:
                        driver.implicitly_wait(1)
                        driver.find_element_by_css_selector('input.button').click()
                    except:
                        refreshfunc()
                if int(cart) == 1:
                    try:
                        driver.implicitly_wait(3)
                        driver.find_element_by_css_selector('input.button').click()
                    except:
                        break


def checkout():
    print "starting checkout process"
    cookies = pickle.load(open("cookies.pkl", "rb"))
    try:
        for cookie in cookies:
            driver.add_cookie(cookie)
    except WebDriverException:
        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
        except WebDriverException:
            print "cookie loading failed"
    driver.get("http://supremenewyork.com/checkout")
    waitfunctioncheckout()
    if str(driver.current_url) == "http://www.supremenewyork.com/shop" or str(driver.current_url) == "http://www.supremenewyork.com/index":
        itemone()
        return
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
    print "--- %s seconds ---" % (time.time() - start_time)


token_list = []
def getcaptcha_token():
    print "Getting captcha token"
    r  = requests.post("http://api.captchasolutions.com/solve", data={'p':'nocaptcha', 'googlekey':'6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz', 'pageurl':'https://www.supremenewyork.com/checkout', 'key':key, 'secret':secret, 'out':'text'})
    print "Doing well"
    txt = r.text
    token = str(txt)
    print token
    if "03" not in token:
        print "First time getting token failed. Trying again."
        getcaptcha_token()
    else:
        print "Extracted captcha token successfully. CAPTCHA token: %s" % token
        token_list.append(token)

def keepcaptchatoken():
    print "THREADING WORKS"
    while True:
        print "Getting captcha token"
        r  = requests.post("http://api.captchasolutions.com/solve", data={'p':'nocaptcha', 'googlekey':'6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz', 'pageurl':'https://www.supremenewyork.com/checkout', 'key':key, 'secret':secret, 'out':'text'})
        txt = r.text
        token = str(txt)
        if "03" not in token:
            print "First timege tting token failed. Trying again."
            pass
        else:
            print "Extracted captcha token successfully. CAPTCHA token: %s" % token
            token_list.append(token)

def injectionpayload():
    driver.implicitly_wait(3)
    driver.execute_script("document.getElementById('g-recaptcha-response').style.display = 'unset';")
    driver.implicitly_wait(3)
    driver.find_element_by_tag_name("textarea").send_keys(token_list[-1])
    driver.implicitly_wait(3)


getcaptcha_token()

if __name__ == '__main__':
    Thread(target = itemone).start()
    Thread(target = keepcaptchatoken).start()
