from re import search

import requests

from ScriptPrcatice.Acunetix.XSS.xss_config import *
from ScriptPrcatice.Utility.Config import *


def XSS():
    for payload in Xsspayloads:
        print(f"[*] Testing payload: {payload}")
        data={
            "search" : payload
        }
        try:
            response = requests.post(url=Url,data=data)
            rcode = response.status_code
            response_body = response.text

            print(f"Response Code: {rcode}")
            print("-" * 40)

        except Exception as e:
            print(f"Not supported {str(e)}")

