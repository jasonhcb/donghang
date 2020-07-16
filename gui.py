#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time
import sys
from splinter import Browser
from tkinter import messagebox
import threading

LOG_LINE_NUM = 0


class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        self.fl = 1

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("东航随心飞刷票")           #窗口名
        self.init_window_name.geometry('860x320+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        # self.init_window_name.geometry('1068x681+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="URL:")
        self.init_data_label.grid(row=0, column=1)
        self.result_data_label = Label(self.init_window_name, text="航班")
        self.result_data_label.grid(row=2, column=1)

        # #文本框
        self.init_data_Text = Text(self.init_window_name, width=100,height=1,background='#e4e6f1')  #原始数据录入框
        self.init_data_Text.grid(row=0, column=3, rowspan=2, columnspan=1)
        self.result_data_Text = Text(self.init_window_name, width=100,height=1,background='#e4e6f1')  #处理结果展示
        self.result_data_Text.grid(row=2, column=3, rowspan=2, columnspan=1)
        self.log_data_Text = Text(self.init_window_name, width=100, height=9)  # 日志框
        self.log_data_Text.grid(row=10, column=0, columnspan=10)

        # #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="开始", bg="lightblue", width=10,command=self.start_to_filght)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=4, column=3)
        self.stop_btn = Button(self.init_window_name, text="停止", bg="lightblue", width=10,command=self.stop)  # 调用内部方法  加()为直接调用
        self.stop_btn.grid(row=5, column=3)

    def stop(self):
        self.fl = 0
        self.str_trans_to_md5_button.config(state='normal')

    #功能函数
    def start_to_filght(self):
        self.fl = 1
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","")
        hb = self.result_data_Text.get(1.0,END).strip().replace("\n","")
        # print("src =",src)
        # print("hb =",hb)
        if src:
            try:
                self.str_trans_to_md5_button.config(state=DISABLED)
                self.t = threading.Thread(target=self.lunxun, args=(src,hb))
                self.t.start()
                #print(myMd5_Digest)
                #输出到界面
            except OSError as err:
                self.log_data_Text.delete(1.0,END)
                self.log_data_Text.insert(1.0,err)


    def lunxun(self,url,flight):
        res = True
        while res:
            if(self.fl == 0):
                break

            res = self.donghang(url,flight)
            print(res)
            if(res == False):
                messagebox.showinfo('提示','赶紧去买票')
            else:
                time.sleep(10)

    # 抢票
    def donghang(self,url,flight):
        browser = Browser('chrome',headless=True) # defaults to firefox
        browser.visit(url)
        # browser.visit('http://www.ceair.com/booking/sha-adnh-200724_CNY.html')
        # browser.find_by_name('search').click()

        # search_results_xpath = '//*[@class="flight"]/a'  # simple, right?
        search_results = browser.find_by_css('.flight')

        now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

        for search_result in search_results:
            str = search_result.text
            sp_str = str.split('\n')
            # print(sp_str[0])
            if(sp_str[0].find(flight) != -1):
                price = search_result.find_by_css('.economy').text
                if(price.find('￥') != -1):
                    return False
                else:
                    # self.log_data_Text.delete(1.0,END)
                    self.log_data_Text.insert(1.0,now+'暂时没票\n')
                    return True
        browser.quit()
        # self.log_data_Text.delete(1.0,END)
        
        self.log_data_Text.insert(1.0,now+'暂时没票\n')
        return True



def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()