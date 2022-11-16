from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import os



class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.l1 = StringVar()
        self.l2 = StringVar()
        self.l3 = StringVar()
        self.l4 = StringVar()
        self.l5 = StringVar()
        self.l6 = StringVar()
        self.l12 = list()
        self.createPage()

    def Input(self):
        self.l12.append([self.l1.get(), self.l2.get(), self.l3.get(), self.l4.get(), self.l5.get(), self.l6.get()])
        file = open(r'1.txt', 'a')
        for i in range(len(self.l12)):
            s = str(self.l12[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
            s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
            file.write(s)
        file.close()

        root2 = Toplevel()
        sw = root2.winfo_screenwidth()
        sh = root2.winfo_screenheight()
        ww = 300
        wh = 500
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        root2.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 标签
        L_success = Label(root2, text='录入成功！')
        L_success.config(font='宋体 -40 bold', fg='black')
        L_success.place(x=60, y=150)

        # 按钮
        B_success = Button(root2, text="确 定", width=5, height=1, command=sys.exit)
        B_success.config(font='宋体 -20', fg='black')
        B_success.place(x=120, y=300)

        mainloop()


    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='参观者身份').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.l1).grid(row=1, column=1, stick=E)
        Label(self, text='联系方式').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.l2).grid(row=2, column=1, stick=E)
        Label(self, text='参观日期').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.l3).grid(row=3, column=1, stick=E)
        Label(self, text='参观时间').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.l4).grid(row=4, column=1, stick=E)
        Label(self, text='参观时长').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.l5).grid(row=5, column=1, stick=E)
        Label(self, text='讲解员').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.l6).grid(row=6, column=1, stick=E)
        Button(self, text='录入', command=self.Input).grid(row=12, column=1, stick=E, pady=10)
