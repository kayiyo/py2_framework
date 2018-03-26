# coding=utf-8
import time
# import pymysql
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from framework.base_page import BasePage


class orderBase(BasePage):

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

    def order_execute(self, db_table):
        order_time = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 所有用到的编号
        db = MySQLdb.connect(host='localhost', user='order', passwd='order',
                             db='orderdelivery', charset='utf8')
        cursor = db.cursor()
        sql = 'select * from ' + db_table
        cursor.execute(sql)
        db.close()
        results = cursor.fetchall()
        order_write_dict = {}
        order_read_dict = {}
        for row in results:
            order_id = row[0]
            order_name = row[1]
            order_type = row[2]
            order_key = row[3]
            order_xpath = row[4]
            order_search_area = row[5]
            order_move_point = row[6]
            # print("id = %s, name = %s, type = %s, key = %s,
            #      xpath= %s, search_area = %s, move_point = %s" %
            #       (order_id, order_name, order_type, order_key, order_xpath,
            #        order_search_area, order_move_point))
            if order_type == 'type_random' or order_type == 'Z':
                self.type(selector=order_xpath, text="%s%s" % (order_key, order_time))
            if order_type == 'type' or order_type == 'A':
                self.type(selector=order_xpath, text=order_key)
            elif order_type == 'select_random' or order_type == 'B':
                self.select_random(selector=order_xpath, count=int(order_key))
            elif order_type == 'select' or order_type == 'C':
                self.select(selector=order_xpath, count=int(order_key))
            elif order_type == 'date' or order_type == 'D':
                self.click(selector=order_xpath)
                self.keys_enter(selector=order_xpath)
            elif order_type == 'choose' or order_type == 'E':
                self.choose(search_button=order_xpath,
                            search_value=order_key,
                            search_bar=order_search_area,
                            move=order_move_point)
            else:
                pass
            # print('%s : %s' % (order_name, order.read_value(order_xpath)))
            order_write_dict[order_id] = self.get_value(order_xpath)
            order_read_dict[order_name] = self.get_value(order_xpath)
        # print(order_write_dict)
        # print(order_read_dict)
        # print(len(order_write_dict), len(order_read_dict))
        # print(order_write_dict[1])
        return order_write_dict[1]
