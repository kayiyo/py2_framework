# coding=utf-8
import time
import unittest
import ConfigParser
import os.path
from framework.browser_engine import BrowserEngine
from pageobjects.order_base import orderBase


class OrderNew(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_order_new(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config_order.ini'
        config.read(file_path)

        user = config.get("orderNew", "user")
        password = config.get("orderNew", "pw")

        orderbase = orderBase(self.driver)
        orderbase.send_username(user)
        orderbase.send_password(password)
        orderbase.login()
        time.sleep(2)
        orderbase.click("xpath=>//*[@id='sider']/div/div/div[2]/ul/li[2]/a")
        time.sleep(2)
        orderbase.click("partial_link_text=>新建")
        time.sleep(2)
        orderbase.order_execute("orderNew")
        orderbase.logout()
        time.sleep(2)
        # homepage.type_search('selenium')  # 调用页面对象中的方法
        # homepage.send_submit_btn()     #调用页面对象类中的点击搜索按钮方法
        # time.sleep(2)
        # homepage.get_windows_img()  # 调用基类截图方法
        # try:
        #     assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
        #     print ('Test Pass.')
        # except Exception as e:
        #     print ('Test Fail.', format(e))

if __name__ == '__main__':
    unittest.main()
