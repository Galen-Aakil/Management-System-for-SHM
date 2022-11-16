from tkinter import *
from ManagerPageView import *  # 菜单栏对应的各个子页面


class ManagerPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (1135, 600))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.inputPage.pack()  # 默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='数据录入', command=self.inputPage)
        self.root['menu'] = menubar  # 设置菜单栏

