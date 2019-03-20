from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 获取driver
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 拖拽方法
    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 获取文本方法封装
    def base_get_text(self, loc):
        # 注意：一定更要返回获取的文本
        return self.base_find_element(loc).text

    # 输入元素方法封装
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # 清空操作
        el.clear()
        # 输入操作
        el.send_keys(value)