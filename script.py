import requests

print('Hello VENV')

req = requests.get("https://google.com")
print(req.status_code)
print(req.ok)
