"""
@project: FM
@author: fanjinding
@time: 2019/12/31 11:43
"""
import os
import yaml

def readyml(yamlPath):
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确： %s" % yamlPath)
    # open 方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    #将其转化为字典形式
    """
    d = yaml.load(cfg)YAML 5.1版本后弃用了yaml.load(file)这个用法，
    因为觉得很不安全，5.1版本之后就修改了需要指定Loader，
    通过默认加载​​器（FullLoader）禁止执行任意函数，该load函数也变得更加安全
    """
    d = yaml.load(cfg,Loader=yaml.FullLoader)
    # print(type(d))
    # print("读取的测试文件数据： %s" %d)
    return d
if __name__ == '__main__':
    yamlPath = "D:/python_workspace/pytest_1231/Params/param/person_service.yaml"
    d = readyml(yamlPath)
    print(d[0]["title"])
    print(d[0]["url"])
    print(d[0]["data"])
    print(d[0]["header"])

