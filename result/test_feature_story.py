import pytest
import allure

@allure.feature("登陆模块")
class TestLogin():
    @allure.story("登陆成功")
    def test_login_success(self):
        print("这是登陆： 测试用例 ，登陆成功")
        pass

    @allure.story("登陆失败")
    def test_login_success_a(self):
        print("这是登陆： 测试用例 ，登陆成功")
        pass

    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_failure(self):
        # 标注测试步骤
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登陆")
        with allure.step("点击登陆之后登陆失败"):
            assert '1' == 1
            print("登陆失败")

        pass

    @allure.story("登陆失败")
    def test_login_failure_a(self):
        print("这是登陆： 测试用例 ，登陆失败")
        pass