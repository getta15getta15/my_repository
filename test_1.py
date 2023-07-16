import requests
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_1(get_browser, get_url):
    if get_browser == "chrome":
        browser = webdriver.Chrome()
    elif get_browser == "ie":
        browser = webdriver.Ie()
    elif get_browser == "firefox":
        browser = webdriver.Firefox()
    browser.get(get_url)
    browser.close()
    assert 1 == 1
    
def test_main_1():
    browser = webdriver.Chrome()
    browser.get('https://www.opencart.com/')
    try:
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "support")))
        assert 1 == 1
    except:
        assert 1 == 0

def test_main_2():
    browser = webdriver.Chrome()
    browser.get('https://www.opencart.com/')
    try:
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "newsletter")))
        assert 1 == 1
    except:
        assert 1 == 0

def test_admin_1():
    browser = webdriver.Chrome()
    browser.get('https://demo.opencart.com/admin/')
    try:
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "input-username")))
        element.send_keys('admin')
        assert 1 == 1
    except:
        assert 1 == 0
                

def test_market_1():
    browser = webdriver.Chrome()
    browser.get('https://www.opencart.com/index.php?route=marketplace/extension')
    try:
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "input-sort")))
        element.click()
        assert 1 == 1
    except:
        assert 1 == 0
        
def test_register_1():
    browser = webdriver.Chrome()
    browser.get('https://www.opencart.com/index.php?route=account/register')
    try:
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "input-username")))
        element.send_keys('admin')
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "button-register")))
        element.click()
        assert 1 == 1
    except:
        assert 1 == 0
        
