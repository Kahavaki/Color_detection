import tkinter as tk
# from tkinter import ttk
import tkinter as ttk
from picture import take_image
from PIL import ImageTk, Image  

img_name = ""

def new_image():
    global r,g,b, blacks
    take_image()
    datas = import_csv("datas.csv")
    r = int(datas.split(",")[0])
    g = int(datas.split(",")[1])
    b = int(datas.split(",")[2])
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
    resize_scale = (600, 400)
    global color_img, masked_1_img, masked_2_img, masked_3_img, masked_4_img, masked_5_img
    color = Image.open('D:\Projegteg\Color_detection\images_color\{}.png'.format(file_name))
    color_resize = color.resize(resize_scale)
    color_img = ImageTk.PhotoImage(color_resize)
    color_img_label.config(image = color_img)

    masked_1 = Image.open('D:\Projegteg\Color_detection\masked_1\{}_.png'.format(file_name))
    masked_1_resize = masked_1.resize(resize_scale)
    masked_1_img = ImageTk.PhotoImage(masked_1_resize)
    masked_1_label.config(image = masked_1_img)

    masked_2 = Image.open('D:\Projegteg\Color_detection\masked_2\{}_.png'.format(file_name))
    masked_2_resize = masked_2.resize(resize_scale)
    masked_2_img = ImageTk.PhotoImage(masked_2_resize)
    masked_2_label.config(image = masked_2_img)

    masked_3 = Image.open('D:\Projegteg\Color_detection\masked_3\{}_.png'.format(file_name))
    masked_3_resize = masked_3.resize(resize_scale)
    masked_3_img = ImageTk.PhotoImage(masked_3_resize)
    masked_3_label.config(image = masked_3_img)

    masked_4 = Image.open('D:\Projegteg\Color_detection\masked_4\{}_.png'.format(file_name))
    masked_4_resize = masked_4.resize(resize_scale)
    masked_4_img = ImageTk.PhotoImage(masked_4_resize)
    masked_4_label.config(image = masked_4_img)

    masked_5 = Image.open('D:\Projegteg\Color_detection\masked_5\{}_.png'.format(file_name))
    masked_5_resize = masked_5.resize(resize_scale)
    masked_5_img = ImageTk.PhotoImage(masked_5_resize)
    masked_5_label.config(image = masked_5_img)

    color_label.config(background = rgb_hack((r,g,b)))

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb



root = tk.Tk()
root.config(background="lightgrey")
root.title("Main")
root.state("zoomed")
root.iconbitmap("icon.ico")

no_images = ImageTk.PhotoImage(Image.open("no_images.png"))

datas_frame = ttk.Frame(root)

# in datas_frame
color_label = ttk.Label(datas_frame, text="asdasd")
color_label.pack()

image_frame_2 = ttk.Frame(root)
image_frame_2.pack(side="bottom", pady=0)

image_frame_1 = ttk.Frame(root)
image_frame_1.pack(side="bottom", pady=0)

# in image_frame
color_img_label = ttk.Label(image_frame_1, image=no_images)
color_img_label.pack(side="left", padx=2, pady=2)

masked_1_label = ttk.Label(image_frame_1, image=no_images)
masked_1_label.pack(side="left", padx=2, pady=2)

masked_2_label = ttk.Label(image_frame_1, image=no_images)
masked_2_label.pack(side="left", padx=2, pady=2)

masked_3_label = ttk.Label(image_frame_2, image=no_images)
masked_3_label.pack(side="left", padx=2, pady=2)

masked_4_label = ttk.Label(image_frame_2, image=no_images)
masked_4_label.pack(side="left", padx=2, pady=2)

masked_5_label = ttk.Label(image_frame_2, image=no_images)
masked_5_label.pack(side="left", padx=2, pady=2)

datas_frame.pack(side="bottom", pady=10)

ttk.Button(root, text="Next image", command=new_image).pack()
root.mainloop()