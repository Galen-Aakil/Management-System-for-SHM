from tkinter import *
from PIL import Image,ImageTk
from resize import *
from notice import *
import os
import xlwt

def Reservation():
    root1 = Toplevel()
    root1.wm_state('zoomed')
    root1.title('博物馆预约系统')

#背景
    w_box1 = 1920
    h_box1 = 1080
    imgpath1 = 'E:\\课设一\\bg.gif'
    img1 = Image.open(imgpath1)
    w1, h1 = img1.size
    img_resized1 = resize(w1, h1, w_box1, h_box1, img1)
    tk_image1 = ImageTk.PhotoImage(img_resized1)
    label_bg1 = Label(root1, image=tk_image1, width=w_box1, height=h_box1)
    label_bg1.pack()

# 标签
    L_R_titile = Label(root1, text='欢  迎  使  用  博  物  馆  预  约  系  统', bg='lightblue')
    L_R_titile.config(font='宋体 -45 bold', fg='white')
    L_R_titile.place(x=960, y=50, anchor="center")

    L_name = Label(root1, text='姓    名',bg='lightblue')
    L_name.config(font='宋体 -30', fg='black')
    L_name.place(x=600,y=200,anchor='center')

    L_phone = Label(root1, text='联系方式', bg='lightblue')
    L_phone.config(font='宋体 -30', fg='black')
    L_phone.place(x=600,y=290,anchor='center')

    L_date = Label(root1, text='参观日期', bg='lightblue')
    L_date.config(font='宋体 -30', fg='black')
    L_date.place(x=600,y=380,anchor='center')

    L_date_example = Label(root1, text='例:20181206', bg='lightblue')
    L_date_example.config(font='宋体 -30', fg='black')
    L_date_example.place(x=1100, y=380, anchor='center')

    L_time = Label(root1, text='参观时长', bg='lightblue')
    L_time.config(font='宋体 -30', fg='black')
    L_time.place(x=600,y=470,anchor='center')

    L_time_example = Label(root1, text='例:1 h', bg='lightblue')
    L_time_example.config(font='宋体 -30', fg='black')
    L_time_example.place(x=1100, y=470, anchor='center')

    L_remark = Label(root1, text='备    注', bg='lightblue')
    L_remark.config(font='宋体 -30', fg='black')
    L_remark.place(x=600,y=560,anchor='center')

#文本框
    S1 = StringVar()
    S2 = StringVar()
    S3 = StringVar()
    S4 = StringVar()
    S5 = StringVar()

    E1 = Entry(root1,textvariable=S1,bg='white',width=15)
    E1.config(font='宋体 -30')
    E1.place(x=740,y=182)

    E2 = Entry(root1, textvariable=S2,bg='white',width=15)
    E2.config(font='宋体 -30')
    E2.place(x=740, y=272)

    E3 = Entry(root1,textvariable=S3, bg='white',width=15)
    E3.config(font='宋体 -30')
    E3.place(x=740, y=362)

    E4 = Entry(root1,textvariable=S4, bg='white',width=15)
    E4.config(font='宋体 -30')
    E4.place(x=740, y=452)

    E5 = Entry(root1,textvariable=S5, bg='white', width=30)
    E5.config(font='宋体 -30')
    E5.place(x=740, y=542)

    # 按钮
    L_button = Button(root1, text="提 交", width=6, height=1, bg='lightblue',font='宋体 -30 bold', fg='black',
                      command=lambda :file_write(S1.get(),S2.get(),S3.get(),S4.get(),S5.get())).place(x=940, y=850)

    mainloop()


def file_write(s1,s2,s3,s4,s5):
    filename = '预约信息.xls'
    if os.path.exists(filename):
        os.remove(filename)

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('data')

    style = xlwt.XFStyle()
    a1 = xlwt.Alignment()
    a1.horz = 0x02
    a1.vert = 0x01
    style.alignment = a1

    worksheet.write(0, 0, '姓名',style)
    worksheet.write(0, 1, '联系方式',style)
    worksheet.write(0, 2, '预约日期',style)
    worksheet.write(0, 3, '预约时长',style)
    worksheet.write(0, 4, '备注',style)

    worksheet.col(0).width = 3333
    worksheet.col(1).width = 6666
    worksheet.col(2).width = 5555
    worksheet.col(3).width = 5555
    worksheet.col(4).width = 8888
    worksheet.col(0).w = 49995

    worksheet.write(1, 0, s1, style)
    worksheet.write(1, 1, s2, style)
    worksheet.write(1, 2, s3, style)
    worksheet.write(1, 3, s4, style)
    worksheet.write(1, 4, s5, style)

    workbook.save('预约信息.xls')
    Notice()

