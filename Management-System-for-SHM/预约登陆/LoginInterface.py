from User import *
from tkinter import *
from Manager import *


class LoginInterface(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (250, 300))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page).grid(row=1, stick=W)
        Label(self.page).grid(row=2, stick=W)
        Button(self.page, text='管理员', command=self.change_2).grid(row=3, column=1)
        Label(self.page).grid(row=4, stick=W)
        Button(self.page, text='讲解员', command=self.change_1).grid(row=5, column=1)
        Label(self.page).grid(row=6, stick=W)
        Button(self.page, text='退出', command=self.page.quit).grid(column=1)

    # 讲解员登录界面
    def change_1(self):
        self.page.destroy()
        User(self.root)

    # 管理员登录界面
    def change_2(self):
        self.page.destroy()
        Manager(self.root)
