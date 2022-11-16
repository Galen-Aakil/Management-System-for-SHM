from tkinter import *
from resize import *

def Judge():
    return 1

def Notice():
    if Judge()==1:
        root2 = Tk()
        sw = root2.winfo_screenwidth()
        sh = root2.winfo_screenheight()
        ww = 300
        wh = 500
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        root2.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    #标签
        L_success = Label(root2, text='预约成功！')
        L_success.config(font='宋体 -40 bold',fg='black')
        L_success.place(x=60,y=150)

    #按钮
        B_success = Button(root2,text="确 定",width=5,height=1,command=sys.exit)
        B_success.config(font='宋体 -20',fg='black')
        B_success.place(x=120,y=300)

    mainloop()


