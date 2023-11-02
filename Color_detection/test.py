import sys
from picture import take_image
from PIL import ImageTk, Image  
from PyQt5.QtWidgets import QApplication, QPushButton

r, g, b, blacks, img_name = 0, 0, 0, 0, ""

def new_image():
    take_image()
    datas = import_csv("datas.csv")
    r = datas.split(",")[0]
    g = datas.split(",")[1]
    b = datas.split(",")[2]
    blacks = datas.split(",")[3]
    img_name = datas.split(",")[4]
    img_name = img_name[:len(img_name)-5]
    place_img(img_name)

def import_csv(filename):
    with open(filename,'r',encoding='UTF-8') as f:
        data = f.readlines() 
        last_row = data[-1] 
    return last_row

def place_img(file_name):
    global img
    img = ImageTk.PhotoImage(Image.open('D:\Projegteg\Color_detection\images_color\{}.png'.format(file_name)))
    

app = QApplication(sys.argv)

button1 = QPushButton("Click me", )
button1.move(64,32)

app.exec()