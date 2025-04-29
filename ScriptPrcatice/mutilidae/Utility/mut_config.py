
#Base URL
Base_Url1 = "http://localhost/mutillidae/src/index.php?page=login.php"

#mutilidae
Base_Url_owasp = "http://localhost"
login_endpoint = "/mutillidae/src/index.php?page=login.php"

#Sqli
owasp_target_SQLi_1 = "You are logged in as admin"

#Payload read
with open("/home/taco/PycharmProjects/PythonSPractice/ScriptPrcatice/Endpoints.txt","r") as f:
    payloads = [line.strip() for line in f if line.strip()]


#Report Generation
def report(payload):
    with open("../../report.txt", "a") as file:
        file.write(payload)