import page
from base.base import Base


class PageLogin(Base):
    # 点击 我 封装
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击 已有账号，去登录
    def page_click_username_link(self):
        self.base_click(page.login_username_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取登录后的信息
    def page_get_info(self):
        # 注意：必须返回获取的信息
        return self.base_get_text(page.login_nickname)

    # 点击设置
    def page_click_setting(self):
        self.base_click(page.login_setting)

    # 拖拽 消息推送 修改密码
    def page_drag_and_drop(self):
        # 获取消息推送 元素
        el1 = self.base_find_element(page.login_send_msg)
        # 获取修改密码 元素
        el2 = self.base_find_element(page.login_update_pwd)
        # 调用拖拽方法
        self.base_drag_and_drop(el1,el2)

    # 点击退出
    def page_click_logout_btn(self):
        self.base_click(page.login_logout_btn)

    # 确认退出
    def page_click_logout_btn_ok(self):
        self.base_click(page.login_logout_btn_ok)

    # 组装业务方法
    def page_login(self, username, pwd):
        # 点击我
        self.page_click_me()
        # 点击已有账号去登录
        self.page_click_username_link()
        # 输入用户名
        self.page_input_username(username)
        # 输入密码
        self.page_input_pwd(pwd)
        # 点击登录
        self.page_click_login_btn()

    # 退出方法 组装
    def page_logout(self):
        # 点击设置
        self.page_click_setting()
        # 拖拽
        self.page_drag_and_drop()
        # 点击退出按钮
        self.page_click_logout_btn()
        # 确认退出
        self.page_click_logout_btn_ok()

    # 断言判断是否退出成功
    def page_logout_is_ok(self):
        try:
            self.base_find_element(page.login_me, timeout=3)
            return True
        except:
            return False