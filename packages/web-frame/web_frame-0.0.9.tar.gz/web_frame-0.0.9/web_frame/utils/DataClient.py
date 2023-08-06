# coding:utf-8
import json

import requests


class DataClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def request(self, method, url, params, **kwargs):
        if not kwargs.get("no_base", False):
            url = f"{self.base_url}/{url}"
        if "no_base" in kwargs:
            del kwargs["no_base"]
        req = method(url, params, **kwargs)
        if req and req.status_code == 200:
            if len(str(req.content)) != "":
                return req.json()
            return ""
        else:
            raise Exception(f"数据获取异常：{req.text}")

    def post(self, url, params, **kwargs):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = self.token
        if "headers" not in kwargs.keys():
            kwargs["headers"] = headers
        if isinstance(params, str):
            params = json.loads(params)
        return self.request(requests.post, url, json.dumps(params), **kwargs)

    def get(self, url, params, **kwargs):
        if isinstance(params, str):
            params = json.loads(params)
        if self.token:
            if "headers" not in kwargs:
                kwargs["headers"] = {"Authorization": self.token}
            else:
                kwargs["headers"]["Authorization"] = self.token
        return self.request(requests.get, url, params, **kwargs)
