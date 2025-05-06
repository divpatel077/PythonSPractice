
#Light Report
def report(payload):
    with open("../Report/Level1.txt", "a") as file:
        file.write(f'\n{payload}')