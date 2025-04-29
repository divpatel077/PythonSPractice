# Demo
Base_Url1 = "http://localhost/mutillidae/src/index.php?page=login.php"
Base_Url2 = "https://83ry5kh39iijeemnly536lir8n8qbxxp.codingame-app.com"
User_endpoint = "public/v2/users"
Post_endpoint = "public/v2/posts"
Comments_endpoint = "public/v2/comments"
Todo_endpoint = "public/v2/todos"
Userinfo = "/login"
target = "App Administrator"

#Payload read
with open("../Payloads/Endpoints.txt", "r") as f:
    payloads = [line.strip() for line in f if line.strip()]


#Report Generation
def report(payload):
    with open("../report.txt", "a") as file:
        file.write(f'\n{payload}')

#Payload read
with open("../Payloads/Endpoints.txt", "r") as f:
    Xsspayloads = [line.strip() for line in f if line.strip()]


#Report Generation
def report(payload):
    with open("../report.txt", "a") as file:
        file.write(f'\n{Xsspayload}')