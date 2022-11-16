from tkinter import *
from PIL import Image,ImageTk
from resize import *
from Reservation import *
from maino import *


def ui_process():
    root = Tk()
    root.wm_state('zoomed')
    root.title('博物馆预约系统')


#背景
    w_box = 1920
    h_box = 1080
    img = Image.open('E:\\课设一\\bg.gif')
    w,h = img.size
    img_resized = resize(w,h,w_box,h_box,img)
    tk_image = ImageTk.PhotoImage(img_resized)
    label_bg = Label(root, image=tk_image, width=w_box, height=h_box)
    label_bg.pack()

#标签
    L_titile = Label(root,text='哈尔滨工业大学（威海）博物馆预约',bg='lightblue')
    L_titile.config(font='宋体 -40 bold',fg='blue')
    L_titile.place(x=960,y=50,anchor="center")

#文本框(单行)

#文本框(多行)

#预约须知
    L_guide = Label(root,text='预约须知\n\n1、考虑到博物馆的参观效果，超过30人的团队需要分批次参观。\n\n2、在博物馆内请保持安静，禁止吸烟，未经允许禁止拍照。\n\n'
                              '3、开馆时间为每周一至周六8：00--17：30。\n\n4、参观需提前三个工作日进行预约。\n\n'
                              '5、预约时间按照网站提供的时间段进行选择，如有疑问请联系178XXXX9983。\n\n',justify=LEFT,bg='lightblue')
    L_guide.config(font='楷体 -30',fg='black')
    L_guide.place(x=960,y=350,anchor='center')

#按钮
    B_0 = Button(root,text="预约入口",width=14,height=2,bg='lightblue',command=Reservation)
    B_0.place(x=800,y=750)
    B_0.config(font='宋体 -40 bold',fg='grey')

    B_1 = Button(root, text="人员登陆", width=10, height=1, bg='lightblue', command=play)
    B_1.place(x=1770, y=920)
    B_1.config(font='宋体 -20 bold', fg='grey')


#按钮对应函数入口

    mainloop()

ui_process()

