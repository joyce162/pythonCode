import requests
from common.recordLog import log
from common.readYaml import ReadYaml


class SendRequests(object):
    def __init__(self):
        self.read = ReadYaml()


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
            res = requests.post(url, data, headers=headers, verify=False)
        return res

    def run_send(self, url, data, headers, method):
        res = None
        if method.upper() == 'GET':
            res = self.send_get(url, data, headers)
        elif method.upper() == 'POST':
            res = self.send_post(url, data, headers)
        return res

    def send_request(self, **kwargs):
        session = requests.session()
        cookie = {}
        try:
            result = session.request(**kwargs)
            set_cookie = requests.utils.dict_from_cookiejar(result.cookies)
            if set_cookie:
                cookie['cookie'] = set_cookie
                log.info(f'cookie: {set_cookie}')
                self.read.write_Yaml_data(set_cookie)
            log.info('result: %s' % result.text if result.text else result)
        except requests.exceptions.ConnectionError:
            log.error('连接异常')
        except requests.exceptions.HTTPError:
            log.error('Http异常')
        except requests.exceptions.RequestException as e:
            log.error(e)
        return result

    def run_main(self, case_name, url, headers, method, cookie=None, filename=None, verify=False, **kwargs):

        log.info(f'用例名称：{case_name}')
        log.info(f'用例url：{url}')
        log.info(f'用例headers：{headers}')
        log.info(f'用例method：{method}')
        log.info(f'用例cookie：{cookie}')
        log.info(f'用例参数：{kwargs}')

        res = self.send_request(
            case_name=case_name,
            url=url,
            headers=headers,
            method=method,
            cookie=cookie,
            filename=filename,
            verify=False,
            **kwargs)

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
    print(res.text)
    # print(res.headers)
