import json
import logging

from httpx import Client, post, get, Timeout

from .time_tools import *

class AuthData:
    def __init__(self, ip, login, password, storage_idx, proxy=None):
        self.ip = ip
        self.login = login
        self.password = password
        self.storage_idx = storage_idx
        self.proxy = proxy

    @classmethod
    def from_config(cls, config):
        store_creds = config["General"]["store_creds"]
        if store_creds in ["TRUE","True", "true", "YES", "Yes", "yes"]:
            ip = config["AuthData"]["ip"]
            login = config["AuthData"]["login"]
            password = config["AuthData"]["password"]
            storage_idx = config["AuthData"]["storage_idx"]
        else:
            ip = input("Enter PT NAD IP:")
            login = input("Enter PT NAD Login:")
            password = input("Enter PT NAD Password:")
            storage_idx = input("Enter PT NAD Storage Index:")

        use_proxy = config["General"]["use_proxy"]
        if use_proxy in ["TRUE","True", "true", "YES", "Yes", "yes"]:
            proxy_type = config["Proxy"]["type"]
            proxy_ip = config["Proxy"]["ip"]
            proxy_port = config["Proxy"]["port"]
            proxy = dict(http =F'{proxy_type}://{proxy_ip}:{proxy_port}',
                         https=F'{proxy_type}://{proxy_ip}:{proxy_port}')
            return cls(ip, login, password, storage_idx, proxy)

        return cls(ip, login, password, storage_idx)

class NADDataProvider():
    def __init__(self, auth_data, logger=None):
        self.auth_data = auth_data
        self.session = Client(http2=True, verify=False, proxies=self.auth_data.proxy, timeout=Timeout(10.0, read=60.0))
        if logger is None:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger

    def __del__(self):
        self.session.close()

    def execute_query(self, bql):
        bql_query = bql.get_query()

        url = 'https://' + self.auth_data.ip + '/api/v2/bql?source=' + str(self.auth_data.storage_idx)
        post_headers = {
            "Host": self.auth_data.ip,
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Content-Type": "text/plain;charset=UTF-8",
            "Cache-Control": "no-cache"}

        rsp = self.session.post(url, auth=(self.auth_data.login, self.auth_data.password),
                    headers=post_headers, data=bql_query)
        if rsp.is_error:
            self.logger.debug("[-] Server error:" + str(rsp.status_code) + "\n" + rsp.text + "\n\nBQL Query:\n" + bql_query)
            raise Exception("Server error")

        result = json.loads(rsp.text)
        if result['total'] == 0:
            self.logger.debug("[-] Empty result: " + rsp.text + "\nBQL Query:\n" + bql_query)
            raise Exception("Empty result")

        return result['result']

    def check_status(self, intercept_if_red=False):        
            url = 'https://' + self.auth_data.ip + '/api/v2/monitoring/status' 
            get_headers = {
                "Host": self.auth_data.ip,
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cache-Control": "no-cache"
            }
            rsp = self.session.get(url, auth=(self.auth_data.login, self.auth_data.password),
                        headers=get_headers)

            if rsp.is_error:
                message = "Server error:" + str(rsp.status_code) + "\n" + rsp.text
                self.logger.debug(message)
                raise Exception(message)

            result = json.loads(rsp.text)
            
            self.logger.info(f"PT NAD status: {result['status']}")
            if result['status'] == 'green':
                return
            problems = []
            red_problems = False
            for p in result['problems']:
                problems.append(p['status'] + ": " + p['template'].format(**p['vars']))
                if p['status'] == 'red':
                    red_problems = True
            message = f"PT NAD is available, but it has some problems ({len(result['problems'])}): \n\t" + "\n\t".join(problems)
            self.logger.debug(message)
            if red_problems and intercept_if_red:
                raise Exception(message)