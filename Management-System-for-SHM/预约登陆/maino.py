from LoginInterface import *
from PIL import Image,ImageTk

def play():
    root = Toplevel()
    root.title('讲解团登录系统')
    LoginInterface(root)
    root.mainloop()

