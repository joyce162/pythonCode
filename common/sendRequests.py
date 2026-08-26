import requests


class SendRequests(object):
    def __init__(self):
        pass

    def send_get(self, url, params, headers):
        res = None
        if headers == 'None':
            res = requests.get(url, params, verify=False)
        else:
            res = requests.get(url=url, params=params, headers=headers, verify=False)
        return res

    def send_post(self, url, data, headers):
        if headers == 'None':
            res = requests.post(url, data, verify=False)
        else:
            res = requests.get(url, data, headers=headers, verify=False)
        return res

    def run_send(self, url, data, headers, method):
        res = None
        if method.upper() == 'GET':
            res = self.send_get(url, data, headers)
        elif method.upper() == 'POST':
            res = self.send_post(url, data, headers)
        return res


if __name__ == '__main__':
    url = 'http://127.0.0.1:8787/dar/user/login'
    data = {
        "user_name": "test01",
        "passwd": "admin123"
    }
    header = None
    method = 'post'
    res = SendRequests().run_send(url, data, header, method)
    print(res.json())
    print(res.headers)
