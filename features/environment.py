#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
#from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
import sys, locale
import logging
from datetime import datetime
import os


#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# wild and dirty hack for windows platform for setting valid locale encoding
if sys.platform in ['win32', 'cygwin']:
    def default_enc(*args, **kwargs):
        return "utf8"
    locale.getpreferredencoding = default_enc

today = datetime.today().strftime("_%d-%m-%y_%H%M%S_")
this_is_day = datetime.today().strftime("%d-%m-%y")

def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    
def before_all(context):
    pass
    #context.config.setup_logging(filename=today+".log", level=logging.INFO)#configfile="behave.ini"
    #filename=today+".log"
    #context.browser = webdriver.Chrome()
    
def before_feature(context, scenario):

    browser_name = os.getenv('BROWSER', 'chrome')
    if browser_name == 'chrome' and os.getenv('HEADLESS') == 'true':
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        browser = Chrome(chrome_options=options)
    else:
        browser = Chrome()

    # Initialize browser and add driver to global context
    context.browser = browser
    if (os.name != "nt"):
        context.browser.maximize_window()

def after_scenario(context, scenario):
    # Take screenshot if scenario fails

    if scenario.status == 'failed':
        
        scenario_error_dir = os.path.join(os.getcwd(), 'errors', this_is_day)
        try:  
            make_dir(scenario_error_dir)
        except OSError:  
            print ("Creation of the directory %s failed" % scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.name.replace(' ', '_').replace('"', '').replace(',', '').replace('@', '').replace('\\', '').replace('/', '')
            + '_' + today + '.png')
        context.browser.get_screenshot_as_file(scenario_file_path)
        webpos = scenario_file_path.find("errors")
        serv_link = 'http://jenkins-autotesting.gcpsoftware.com:8080/job/bacb_bdd/ws/bacb_bdd/'
        sc_name = scenario.name
        weblink = serv_link+scenario_file_path[webpos:]
        if (os.name != "nt"):
        #<a href=""><img src="avatar.png" alt="Avatar" style="width:40%"></a>
            print(f'</pre><p><img src="{weblink}" alt="{sc_name}" style="width:60%"><br><a href="{weblink}">{sc_name}</a></p><pre>')
        else:
            print(scenario_file_path)
    #context.browser.quit()

def after_feature(context, feature):
    #if feature.status == 'failed':
    #   do some action
    context.browser.quit()
       
def after_all(context):
    try:
        context.browser.quit()
    except:
        pass
    
