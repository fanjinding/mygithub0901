"""
@project: FM
@author: fanjinding
@time: 2020/1/14 11:29
"""
import pytest

@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app

def test_something_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_method(self):
        pass

if __name__ == "__main__":
    # mark标记
    # pytest.main(["-s", "test_server.py", "-m=webtest"])
    # -v 指定的函数节点id
    pytest.main(["-v", "test_server.py::TestClass::test_method"])
    # -k 匹配用例名称
    # pytest - v - k http