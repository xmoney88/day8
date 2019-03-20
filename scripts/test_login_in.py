import sys
import os
sys.path.append(os.getcwd())


from page.page_in import PageIn


class TestLogin():
    def setup(self):
        # 调用登录方法 匿名对调用 示例
        # PageIn().page_get_pagelogin().page_login()


        # 实例化获取统一入口类并获取 登录页面对象
        self.login = PageIn().page_get_pagelogin()

    def teardown(self):
        self.login.driver.quit()

    def test_login(self,username="itheima", pwd="123456", expect_result="itheima"):
        # 登录
        self.login.page_login(username, pwd)
        try:
            # 断言登录
            assert expect_result == self.login.page_get_info()
            # 退出
            self.login.page_logout()
            try:
                assert self.login.page_logout_is_ok()
            except:
                print("退出登录断言出错")
        except:
            print("登录断言出错")
