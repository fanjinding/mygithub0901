"""
@project: FM
@author: fanjinding
@time: 2020/1/2 17:17
"""
from Utils.getyaml import readyml
from Common.request_method import RunMethod
import random
import allure
import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

@allure.feature('计划系统测试用例')
class TestCase():

    @allure.story('新建项目计划')
    def test_case1(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/planAddOrUpdate.yaml"
        params = readyml(yamlPath)
        a = random.randrange(1, 100)
        b = random.choice('abcdefghijklmnopqrstuvwsyz')
        c = str(a) + b
        data = {
            "project_id": "Pj1101081201",
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "200820e3227815ed1756a6b531e7e0d2",
            "person_id": "RY493fd4f7d44642f1aa73c8032ea57462",
            "plan_name": "调用post方法新建计划>>>" + c,
            "execute_dept_id": "BMa074df85c9d74dd590388f7196647dc3",
            "plan_from": "0",
            "plan_id": "",
            "group_plan_id": "",
            "creator_id": "RY493fd4f7d44642f1aa73c8032ea57462",
            "updator_id": ""
        }
        text = runmethod.post_main(url=params[0]['url'], headers=params[0]['header'], data=data)
        print(text)
        return text
    # 使用assert断言判断是否返回成功
    # def test_function(self):
    #     testcase = TestCase()
    #     assert 'success' in str(testcase.test_case1())
    # @allure.story('根据plan_id查询计划详情')
    # def test_case2(self):
    #     runmethod = RunMethod()
    #     testcase = TestCase()
    #     yamlPath = "D:/python_workspace/pytest_1231/Params/param/planAddOrUpdate.yaml"
    #     params = readyml(yamlPath)
    #     text = testcase.test_case1()
    #     plan_id = text['Item']['plan_id']
    #     # 由于python中的字符串默认是单引号包裹起来的，java中不识别单引号，所以使用replace()方法替换成双引号
    #     data = {
    #         "project_id":"Pj1101081201",
    #         "user_id":"58a612614e1f430bb35bef96a90b77b8",
    #         "pd":"200820e3227815ed1756a6b531e7e0d2",
    #         "person_id":"RY493fd4f7d44642f1aa73c8032ea57462",
    #         "plan_id":plan_id.replace("'", '"')
    #     }
    #     text = runmethod.post_main(url=params[1]['url'], headers=params[1]['header'], data=data)
    #     return text
    # @allure.story('根据plan_id查询计划监控详情')
    # def test_case3(self):
    #     runmethod = RunMethod()
    #     testcase = TestCase()
    #     yamlPath = "D:/python_workspace/pytest_1231/Params/param/planAddOrUpdate.yaml"
    #     params = readyml(yamlPath)
    #     text = testcase.test_case1()
    #     plan_id = text['Item']['plan_id']
    #     # 由于python中的字符串默认是单引号包裹起来的，java中不识别单引号，所以使用replace()方法替换成双引号
    #     data = {
    #         "project_id":"Pj1101081201",
    #         "user_id":"58a612614e1f430bb35bef96a90b77b8",
    #         "pd":"200820e3227815ed1756a6b531e7e0d2",
    #         "person_id":"RY493fd4f7d44642f1aa73c8032ea57462",
    #         "plan_id":plan_id.replace("'", '"'),
    #         "start_time":"20200101000000",
    #         "end_time":"20200131235959",
    #         "page":"1",
    #         "page_size":"10"
    #     }
    #     text = runmethod.post_main(url=params[2]['url'], headers=params[2]['header'], data=data)
    #     return text


if __name__ == '__main__':
    testcase = TestCase()
    testcase.test_case1()
    # testcase.test_case2()
    # testcase.test_case3()
    testcase.test_function()
