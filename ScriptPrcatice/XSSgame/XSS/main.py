from selenium import *
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from ScriptPrcatice.XSSgame.Utility.URLs import *;

def XSSgame():
    print("starting")

    payload = "<script>alert(1)</script>"

    URL = f"{Base_Url}?query={payload}"
    driver = webdriver.Chrome()