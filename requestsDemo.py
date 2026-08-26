import requests

url = 'http://127.0.0.1:8787/dar/user/login'

data = {
    "user_name": "test01",
    "passwd": "admin123"
    }

res = requests.post(url=url,data=data)
print(res.text)