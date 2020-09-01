"""
@project: FM
@author: fanjinding
@time: 2019/12/31 11:14
"""
import requests
import json
from Log.logger import MyLog

class RunMethod:
    def post_main(self,url,data,headers):
        mylog = MyLog()
        if headers!=None:
            if headers=={'Content-Type': 'application/json'}:
                res=requests.post(url=url,json=data,headers=headers)
                if res.status_code == 200:
                    text = json.loads(res.text)
                    if(text['Result']=='success'):
                        print('测试通过，返回结果如下：' + str(text))
                        mylog.warning('测试通过，返回结果如下：' + str(text))
                        return text
                    else:
                        print('测试失败，返回结果如下：' + str(text))
                        mylog.warning('测试通过，返回结果如下：' + str(text))
                else:
                    print(res)
            elif headers=={"Content-Type": 'application/x-www-form-urlencoded'}:
                #因为str()方法默认是单引号''包裹的，想到解决办法是通过replace()转成双引号""
                data = "jsonString="+str(data).replace("'", '"')
                res = requests.post(url=url, data=data, headers=headers)
                if res.status_code == 200:
                    text = json.loads(res.text)
                    #assert text['result'] is not 'success',mylog.warning("测试失败，返回结果："+str(text))
                    if (text['result'] == 'success'):
                        print('登录成功')
                        mylog.warning('测试通过，返回结果如下：' + str(text))
                        return text
                    else:
                        print('测试失败，返回结果如下：' + str(text))
                        mylog.warning('测试通过，返回结果如下：' + str(text))
                else:
                    print(res)
        else:
            print("请检查配置文件是否正确")
            mylog.warning("请检查配置文件是否正确")

if __name__ == '__main__':
    runmethod = RunMethod()
    url = "http://192.168.100.222:8081/EMS_SaaS_Web/Spring/MVC/entrance/unifier/loginUserService"
    data = {"password": "qwe123",
            "loginDevice": "PC",
            "loginName": "fjd"}
    #data = data2.replace("'", '"')
    headers = {"Content-Type": 'application/x-www-form-urlencoded'}
    #data = {}
    runmethod.post_main(url=url, headers=headers, data=data)