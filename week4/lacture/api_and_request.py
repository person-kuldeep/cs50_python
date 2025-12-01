import requests
import sys

response = requests.get("https://jsonplaceholder.typicode.com/photos/1")
print(response)
print("Python executable path: ", sys.executable)
if response.status_code == 200:
    post = response.json()
    print(post)

    