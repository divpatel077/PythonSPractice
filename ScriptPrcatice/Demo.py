
import requests
from ScriptPrcatice.myrandom import *
import json


#Base Url
Base_Url="https://gorest.co.in"

#AuthToken
Auth="Bearer 265d95d186c5f9e0dc559827a31e06cfce607d25b646b8413ec1d26197539a89"



#Get request
def GetRequest():
    print("get started............")
    print("get started............")
    url = Base_Url+"/public/v2/users"
    header = {"Authorization":Auth}
    response = requests.get(url,headers=header)
    json_raw = response.json()
    Rcode=response.status_code
    res_body=json.dumps(json_raw,indent=4)

    print("Response Code: "+str(Rcode) +"\nResponse Body:\n"+res_body)
    print("get closed.......")
    print("get closed.......")
#Post Request
def PostRequest():

    print("post Started...........")
    print("post Started...........")
    url = Base_Url + "/public/v2/users"
    header = {"Authorization": Auth}
    data = {
        "name": "Ta",
        "email": randomEmail(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url,json=data, headers=header)
    json_raw = response.json()
    Rcode = response.status_code
    res_body = json.dumps(json_raw, indent=4)

    user_id = json_raw["id"]

    print("Response Code: " + str(Rcode) + "\nResponse Body:\n" + res_body)
    print("post ENDed...........")
    print("post ENDed...........")

    return user_id
#Put Request
def putRequest(userid):

    print("Put Started......")
    print("Put Started........")
    url = Base_Url + f"/public/v2/users/{userid}"
    header = {"Authorization": Auth}
    data = {
        "name": "Taco123",
        "gender": "male",
        "status": "active"
    }
    response = requests.put(url, json=data, headers=header)
    json_raw = response.json()
    Rcode = response.status_code
    res_body = json.dumps(json_raw, indent=4)
    print("Response Code: " + str(Rcode) + "\nResponse Body:\n" + res_body)
    print("Put ended")


# #Delete User
def deleteRequest(userid):
    print("delete started")
    url = Base_Url + f"/public/v2/users/{userid}"
    header = {"Authorization": Auth}
    response = requests.delete(url,headers=header)
    Rcode = response.status_code
#    res_body = json.dumps(json_raw, indent=4)
    print("Response Code: " + str(Rcode) + "\nResponse Body:\n" )
    print("Delete ended")
