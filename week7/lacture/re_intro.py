import re

url = input("URL: ")

pattern = r"^(?:https?://)?(?:www\.)?twitter\.com/(?P<username>[a-z0-9_]+)$"
if match := re.search(pattern, url, re.IGNORECASE):
    print(f"Username: {match.group("username")}")
print(url)    


def main():
    email_address = input("Email: ")
    # pattern = r"^[a-z.]{1,12}@[a-z0-9.]+\.com$"
    pattern = r"^(\w+(\w|\.)*)@((\w+\.)?\w+\.com)$"
    # correct_email = re.search(pattern, email_address, re.IGNORECASE)

    if correct_email := re.search(pattern, email_address, re.IGNORECASE):
        print("valid email")
        print(f"username: {correct_email.group(4)}")
        print(f"domain: {correct_email.group(2)}")
    else:
        print("Invalid email address.")    


if __name__ == "__main__":
    ...

