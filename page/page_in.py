"""
    目标：统一入口类
    操作：
        1. 新建侧类 PageIn
            # 获取页面对象方法

"""
from base.get_driver import get_driver
from page.page_address import PageAddress
from page.page_login import PageLogin
from page.page_order import PageOrder

driver = get_driver()


class PageIn:
    # 获取登录页面对象方法
    def page_get_pagelogin(self):
        return PageLogin(driver)

    # 获取订单对象方法
    def page_get_pageorder(self):
        return PageOrder(driver)

    # 获取地址管理方法
    def page_get_pageaddress(self):
        return PageAddress(driver)
