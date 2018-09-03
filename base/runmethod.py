import requests
import json
class RunMethod:
    def request_post(self,url,data,headers=None):
        res=None
        if headers !=None:
            res=requests.post(url=url,data=data,headers=headers)
        else:
            res=requests.post(url=url,data=data)

        return res.json()
    def request_get(self,url,data=None,headers=None):
        res=None
        if headers !=None:
            res=requests.get(url=url,params=data,headers=headers)
        else:
            res=requests.get(url=url,params=data)
        return res
    def run_main(self,method,url,data=None,headers=None):
        res=None
        if method.lower()=='post':
            res=self.request_post(url,data,headers)
        else:
            res=self.request_get(url,data,headers)
        return res
