import requests
from ScriptPrcatice.Utility.Config import *  # assuming your config variables


# POST Request Function
def PostRequest():
    print("POST attack started...........")

    url = Base_Url2 + Userinfo
    # headers = {
    #     "Content-Type": "application/json"
    #     # "Authorization": Auth   # Uncomment if auth is needed
    # }

    for payload in payloads:
        print(f"[*] Testing payload: {payload}")

        data = {
            "username": payload,
            "pass": "admin"
        }

        try:
            response = requests.post(url, data=data)
            rcode = response.status_code
            response_body = response.text

            print(f"Response Code: {rcode}")

            if target in response_body:
                report(payload)
                print("present")
            else:
                print("absent")

            # print(f"Response Body:\n{response_body}")
            print("-" * 40)

        except Exception as e:
            print(f"Request failed: {str(e)}")

        print("POST attack ended...........")

if __name__ == "__main__":
    PostRequest()