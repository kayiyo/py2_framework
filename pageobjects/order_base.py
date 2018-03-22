# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from framework.base_page import BasePage


class orderBase(BasePage):
    # input_box = "id=>kw"
    # search_submit_btn = "xpath=>//*[@id='su']"
    # # 百度新闻入口
    # news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"
    #
    # def type_search(self, text):
    #     self.type(self.input_box, text)
    #
    # def send_submit_btn(self):
    #     self.click(self.search_submit_btn)
    #
    # def click_news(self):
    #     self.click(self.news_link)
    #     self.sleep(2)

    input_username = "xpath=>//*[@id='username']"
    input_password = "xpath=>//*[@id='password']"
    button_login = "partial_link_text=>登"
    button_logout = "partial_link_text=>退"

    def send_username(self, text):
        self.type(self.input_username, text)

    def send_password(self, text):
        self.type(self.input_password, text)

    def login(self):
        self.click(self.button_login)
        self.sleep(1)

    def logout(self):
        self.click(self.button_logout)
        self.sleep(1)
