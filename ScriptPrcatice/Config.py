# Demo
Base_Url1 = "http://localhost/mutillidae/src/index.php?page=login.php"
Base_Url2 = "http://testphp.vulnweb.com"
User_endpoint = "public/v2/users"
Post_endpoint = "public/v2/posts"
Comments_endpoint = "public/v2/comments"
Todo_endpoint = "public/v2/todos"
Userinfo = "/userinfo.php"
target = "Logout test"

#mutilidae
Base_Url_owasp = "http://localhost"
login_endpoint = "/mutillidae/src/index.php?page=login.php"

#Sqli
owasp_target_SQLi_1 = "You are logged in as admin"


#Endpoint read
with open("/home/taco/PycharmProjects/PythonSPractice/ScriptPrcatice/Endpoints.txt","r") as f:
    payloads = [line.strip() for line in f if line.strip()]


#Report Generation
def report(payload):
    with open("report.txt","a") as file:
        file.write(payload)