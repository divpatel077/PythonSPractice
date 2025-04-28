Base_Url1 = "https://gorest.co.in/"
Base_Url2 = "http://testphp.vulnweb.com"
User_endpoint = "public/v2/users"
Post_endpoint = "public/v2/posts"
Comments_endpoint = "public/v2/comments"
Todo_endpoint = "public/v2/todos"
Userinfo = "/userinfo.php"
target = "Logout test"
with open("Endpoints.txt","r") as f:
    payloads = [line.strip() for line in f if line.strip()]

def report(payload):
    with open("report.txt","a") as file:
        file.write(payload)