import io
from tkinter import *
from PIL import Image,ImageTk

def resize(w,h,w_box,h_box,photo):
    f1 = 1.0*w_box/w
    f2 = 1.0*h_box/h
    factor = min([f1,f2])
    width = int(w*factor)
    height = int(h*factor)
    return photo.resize((width,height),Image.ANTIALIAS)

