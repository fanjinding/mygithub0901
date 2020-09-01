"""
@project: FM
@author: fanjinding
@time: 2020/1/8 11:31
"""

import pytest
import allure
from Common.request_method import *
from Utils.getyaml import *
from Utils.send_email import *

"""
在当前文件夹执行：
    生成测试数据
    pytest getreport.py --alluredir ./result
    生成测试报告
    allure generate ./result -o ./report --clean
    将allure报告作为一个可以远程连接的网站打开
    allure open -h 192.168.30.219 -p 8088 ./report/
"""


@allure.feature('测试用例功能')  # feature定义功能
class TestClass(object):

    @pytest.fixture(scope='function')
    def setup_function(request):
        def teardown_function():
            print("teardown_function called.")

        request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
        print('setup_function called.')

    @pytest.fixture(scope='module')
    def setup_module(request):
        def teardown_module():
            print("teardown_module called.")

        request.addfinalizer(teardown_module)
        print('setup_module called.')

    @allure.story('登录')
    @pytest.mark.website
    def test_one(setup_module):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/fmlogin.yaml"
        params = readyml(yamlPath)
        for i in range(0, len(params)):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=params[i]['data'])
    @allure.story('查询人员列表')
    @pytest.mark.website
    def test_two(setup_function):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/querypersonlist.yaml"
        params = readyml(yamlPath)
        for i in range(0, len(params)):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=params[i]['data'])

    @allure.story('查询人员数量')
    @pytest.mark.website
    def test_three(setup_function):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/querypersoncount.yaml"
        params = readyml(yamlPath)
        for i in range(0, len(params)):
            #print("开始执行>>>>>>>>>>>>>>>>>>>>" + params[i]['title'])
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=params[i]['data'])

if __name__ == '__main__':
    testclass = TestClass()
    testclass()
