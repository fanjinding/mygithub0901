"""
@project: FM
@author: fanjinding
@time: 2020/1/9 10:03
"""
from Utils.getyaml import readyml
from Common.request_method import RunMethod
import allure

@allure.feature('计划系统测试用例')
class TestGetLatestTime():
    """
    项目计划
    """
    @allure.story('查询下一次发单时间-单次设置')
    def test_case1(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "C860608c3bda24fe9a8238a745fb4b196",
            "start_time": "20200110104430"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('查询下一次发单时间-日频次')
    def test_case2(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "Cc91884bd08c3436b835ef3f43cee0487",
            "start_time": "20200108104430"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('查询下一次发单时间-周频次')
    def test_case3(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "C4b6e496a30b94e9fb30b39602d6342d8",
            "start_time": "20200202152100"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('查询下一次发单时间-月频次')
    def test_case4(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "Cc35dbedac02043c4a9f7303a14e88736",
            "start_time": "20200201000000"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('查询下一次发单时间-年频次')
    def test_case5(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "C68ee2ebd4d6b4158815a766765e67fb8",
            "start_time": "20200201000000"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)
    """
    集团计划
    """
    @allure.story('JT-查询下一次发单时间-单次设置')
    def test_jt_case1(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "Cf3bf6f46e7104dc09ac1f91e3fc7ad54",
            "start_time": "20200110104430"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('JT-查询下一次发单时间-日频次')
    def test_jt_case2(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "Cae3c4cb58fb446ebbd003e0def2b3aec",
            "start_time": "20200120104430"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('JT-查询下一次发单时间-周频次')
    def test_jt_case3(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "Cb497734acc5d459a98a6715889c8130c",
            "start_time": "20200202152100"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('JT-查询下一次发单时间-月频次')
    def test_jt_case4(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "C4e1ef54b088148429ec5f8de8f5793ed",
            "start_time": "20220201000000"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)

    @allure.story('JT-查询下一次发单时间-年频次')
    def test_jt_case5(self):
        runmethod = RunMethod()
        yamlPath = "D:/python_workspace/pytest_1231/Params/param/plan_getLatestTime.yaml"
        params = readyml(yamlPath)
        data = {
            "user_id": "58a612614e1f430bb35bef96a90b77b8",
            "pd": "systemId",
            "cell_id": "Cc86df55bf96b410a80882c1ead3b15ca",
            "start_time": "20210101000000"
        }
        for i in range(0, 1):
            runmethod.post_main(url=params[i]['url'], headers=params[i]['header'], data=data)
if __name__ == '__main__':
    testcase = TestGetLatestTime()
    testcase.test_case1()
    testcase.test_case2()
    testcase.test_case3()
    testcase.test_case4()
    testcase.test_case5()
    testcase.test_jt_case1()
    testcase.test_jt_case2()
    testcase.test_jt_case3()
    testcase.test_jt_case4()
    testcase.test_jt_case5()