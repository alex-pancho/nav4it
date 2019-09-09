from behave import step, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import datetime
import json
import logging
import requests
import xml.etree.ElementTree as ET
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

TEST = False
MUX = 1.0

dateday = datetime.today().strftime("%d.%m.%Y")
foolday = datetime.today().strftime("_%d.%m.%Y_%H%M%S_")


def et_print(et):
    i=0
    for child in et:
        print ('child:', i)
        print (child.text, child.attrib, child.tag)
        i = i+1
        
#find page item by xpath
def xp(c, path):
    try:
        element = c.browser.find_element(By.XPATH, path)
    except:
        element = None
    return element
    
#find list of page items by xpath      
def xxp(c, path):
    try:
        elements = c.browser.find_elements(By.XPATH, path)
    except:
        elements = None
    return elements

def be_de_xp(context, path, time_wait=5):
    time_wait = time_wait * MUX
    time_s= datetime.today()
    time_now = datetime.today()
    element = None
    while (time_now-time_s).seconds <= time_wait:
        try:
            element = context.browser.find_element(By.XPATH, path)
        except:
            pass
        if element is not None:
            try:
                element_attr= element.get_attribute("data-enabled")
            except:
                element_attr= "none"
            if element_attr == "true" or element_attr == "none" or element_attr is None:           
                break 
            else:
                element = None
        sleep(0.1)
        time_now = datetime.today()
    #print((time_now-time_s).seconds)
    return element         
        
#search for an item by xpath for a given time
def be_click_xp(context, path, time_wait=5):
    time_wait = time_wait * MUX
    try:
        element = WebDriverWait(context.browser, time_wait).until(
            EC.element_to_be_clickable((By.XPATH, path)))
    except:
        element = None
    return element
    
def is_vis_xp(context, path, time_wait=5):
    time_wait = time_wait * MUX
    try:
        element = WebDriverWait(context.browser, time_wait).until(
            EC.visibility_of_element_located((By.XPATH, path)))
    except:
        element = None
    return element
    
def is_pres_xp(context, path, time_wait=5):
    time_wait = time_wait * MUX
    try:
        element = WebDriverWait(context.browser, time_wait).until(
            EC.presence_of_element_located((By.XPATH, path)))
    except:
        element = None
    return element      
#search for an item by xpath for a given time (other way)
def time_xp(context, path, time_wait=5):
    time_wait = time_wait * MUX
    time_s= datetime.today()
    time_now = datetime.today()
    element = None
    while (time_now-time_s).seconds <= time_wait:
        try:
            element = context.browser.find_element(By.XPATH, path)
        except:
            pass
        if element is not None:
            #print(f"find by {path}")
            break
        sleep(0.1)
        time_now = datetime.today()
    #print((time_now-time_s).seconds)
    return element 

def set_global_header(c):
    hdr = ulogin(c.username, c.userpass, TU)
    print(hdr)
    return hdr

def _printWebObj(o):
    print("---"*8)
    try:
        print('text:', o.get_attribute('text')) #text
    except:
        pass
    try:
        print('innerText:', o.get_attribute('innerText'))
    except:
        pass
    try:
        print('textContent:', o.get_attribute('textContent'))
    except:
        pass
    try:
        print('is enabled:', o.is_enabled())#Enab or Disab
    except:
        pass
    try:
        print('placeholder:', o.get_attribute('placeholder'))#Attib
    except:
        pass
    print("---"*8)
#get any url
@given('open web {url}')
def open_u00(context, url):
    context.browser.get(url)
    context.browser.implicitly_wait(10)


@when('wait "{sec}"')
def open_u02(context, sec):
    try:
        sec = float(sec)
    except:
        sec = 5
    sec= sec*MUX
    sleep(sec)

@when('input "{fval}" in the "{fname}" field')
def open_u06(context, fname, fval, fnone=None):
    link_txt = None
    xpath = ''
    
    if fname == 'Email address':
        xpath = '//*[@id="email"]'
        lpath = '//label[@for="email"]'
    if fname == 'Password':
        xpath = '//*[@id="passwd"]'
        lpath = '//label[@for="passwd"]'
    if xpath != '':
        link = xp(context, xpath)
        link_txt = xp(context, lpath)
        if link_txt is not None:
            link_txt = link_txt.get_attribute('innerText')
        else:
            link_txt = "#&()??xx!!"

    into = fname.lower().find(link_txt.lower())
    if into == -1:
        into = link_txt.lower().find(fname.lower())
    assert into!=-1, 'field ' + fname + ' not found. Text '+link_txt
    link.clear()
    link.send_keys(fval)


@when('click "{button}" button')
def open_u09(context, button):
    link = None
    xpath = ''
    if button == 'Sign in':
        xpath = '//nav/div[@class="header_user_info"]/a'
    if button == 'Sign':
        xpath = '//*[@id="SubmitLogin"]'
    
    if xpath != '':
        link = xp(context, xpath)
        link.click()
        
    assert link is not None, f'button {button} not found. Get: %s' % (str(type(link)))
    
@then('the page url will be {url}')
def open_u10(context, url):
    current_url = context.browser.current_url
    assert current_url == url, 'url of the page does not match the expected. Received url:' + current_url




if __name__ == '__main__':
    from selenium import webdriver

    import os
    from time import sleep
    
        
    users = ['qa123456', 'testqa1@yopmail.com','testqa@yopmail.com']

    
    class cont():
        browser = webdriver.Chrome()
        
    
    cont.username = users[1]
    cont.userpass = users[0]
    cont.head = ''

    
    print ('login')


    print('... done!')