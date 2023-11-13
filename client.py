import requests

data = requests.get("http://localhost:8000/users/profile/")
print(data.json())
