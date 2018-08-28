# import requests
# import json
#
# from base.runmethod import RunMethod
#
# data={
#     "name":"lljk",
#     "passwd":"123456"
# }
#
# data=json.dumps(data)
# headers={
# "Content-Type":"application/json"
# }
# url='http://127.0.0.1:5000/api/user/reg/'
#
# # res=requests.post(url,data,headers=headers)
# # print(res.json())
# #method,url,data=None,headers=None
# run=RunMethod()
# y=run.run_main('post',url,data,headers)
# print(y)
