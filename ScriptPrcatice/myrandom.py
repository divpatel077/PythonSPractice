import myrandom
import string

#Random email
def randomEmail():
    domain = "taco.com"
    email_length=10
    random_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_str + "@" + domain
    return email