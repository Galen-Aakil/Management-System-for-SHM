from tkinter import *
from tkinter.ttk import Treeview
from data_info import *
class UserPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (1135, 600))  # 设置窗口大小
        self.l1 = StringVar()
        self.l2 = StringVar()
        self.l3 = StringVar()
        self.l4 = StringVar()
        self.l5 = StringVar()
        self.l6 = StringVar()
        self.createPage()

    def createPage(self):
        # Frame框架，将几个组件放在一起
        TopFrame = Frame(self.root, width=1135, height=150)
        TLFrame = Frame(TopFrame, width=985, height=150)
        TLTFrame = Frame(TLFrame, width=985, height=75)

        Label(TLTFrame, text="讲解任务统计", font=("宋体", 11)).pack(side=LEFT)
        # # StringVar跟踪变量的值的变化，以保证值的变更随时可以显示在界面上


        # 讲解任务信息展示
        ShowFrame = Frame(self.root, width=780, height=450, bg='pink')
        ShowFrame.pack(side=TOP)

        scrollBar = Scrollbar(ShowFrame)
        scrollBar.pack(side=RIGHT, fill=Y)
        tree = Treeview(ShowFrame,
                        columns=(
                        'c0', 'c1', 'c2', 'c3', 'c4', 'c5'),
                        show="headings",
                        height=540,
                        yscrollcommand=scrollBar.set)
        tree.column('c0', width=100, anchor='center')
        tree.column('c1', width=100, anchor='center')
        tree.column('c2', width=70, anchor='center')
        tree.column('c3', width=100, anchor='center')
        tree.column('c4', width=100, anchor='center')
        tree.column('c5', width=60, anchor='center')

        tree.heading('c0', text='参观者身份')
        tree.heading('c1', text='联系方式')
        tree.heading('c2', text='参观日期')
        tree.heading('c3', text='参观时间')
        tree.heading('c4', text='参观时长')
        tree.heading('c5', text='讲解员')
        tree.pack(side=LEFT, fill=BOTH)

        file = open(r'1.txt','rb')
        line = file.readline()
        tree.insert('', 'end', values=line)
        line = line[:-1]
        while line:
            line = file.readline()
            tree.insert('', 'end', values=line)

        self.root.mainloop()

    # def sort(self):
    #         Label(self).grid(row=0, stick=W, pady=10)
    #         Label(self, text='参观者身份').grid(row=1, stick=W, pady=10)
    #         Entry(self, textvariable=self.l1).grid(row=1, column=1, stick=E)
    #         Label(self, text='联系方式').grid(row=2, stick=W, pady=10)
    #         Entry(self, textvariable=self.l2).grid(row=2, column=1, stick=E)
    #         Label(self, text='参观日期').grid(row=3, stick=W, pady=10)
    #         Entry(self, textvariable=self.l3).grid(row=3, column=1, stick=E)
    #         Label(self, text='参观时间').grid(row=4, stick=W, pady=10)
    #         Entry(self, textvariable=self.l4).grid(row=4, column=1, stick=E)
    #         Label(self, text='参观时长').grid(row=5, stick=W, pady=10)
    #         Entry(self, textvariable=self.l5).grid(row=5, column=1, stick=E)
    #         Button(self, text='录入', command=self.Input).grid(row=12, column=1, stick=E, pady=10)
