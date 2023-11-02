from datetime import datetime
import numpy as np
import cv2
import os
import csv

cap = cv2.VideoCapture(0)
img = cv2.imread('raw_images/teszt.PNG')


def read_analyze_img(image):
    # white and the shades of yellow
    result_1 = mask_frame(np.array([0,14,0]), np.array([40,31,255]), image)
    result_2 = mask_frame(np.array([22,9,0]), np.array([40,31,255]), image)
    result_3 = mask_frame(np.array([0,39,0]), np.array([40,255,255]), image)
    result_4 = mask_frame(np.array([0,24,0]), np.array([40,38,255]), image)
    result_5 = mask_frame(np.array([0,24,0]), np.array([40,50,255]), image)
    return result_1, image, result_2, result_3, result_4, result_5

def read_analyze_video():
    _, frame = cap.read()
    # white and the shades of yellow
    result_1 = mask_frame(np.array([0,14,0]), np.array([40,31,255]), frame)
    result_2 = mask_frame(np.array([22,9,0]), np.array([40,31,255]), frame)
    result_3 = mask_frame(np.array([0,39,0]), np.array([40,255,255]), frame)
    result_4 = mask_frame(np.array([0,24,0]), np.array([40,38,255]), frame)
    result_5 = mask_frame(np.array([0,24,0]), np.array([40,50,255]), frame)
    return result_1, frame, result_2, result_3, result_4, result_5

def mask_frame(lower, upper, image):
    # convert the frame colors to HSV colors
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

# sorts black pixels from other colored pixels
def color_sort(frame):
    colors = []
    black_pxl = 0
    for row in frame:
            for i in row:
                if i[0] != 0 and i[1] != 0 and i[2] != 0:
                    colors.append(i)
                else:
                    black_pxl+=1
    return colors, black_pxl

def save_image(frame, result_1, result_2, result_3, result_4, result_5):
    now = datetime.now()
    name = "{}.png".format(f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}-{now.microsecond}")
    masked_name = "{}_.png".format(f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}-{now.microsecond}")
    cv2.imwrite(os.path.join("D:\projegteg\Color_detection\masked_1", masked_name), result_1)
    cv2.imwrite(os.path.join("D:\projegteg\Color_detection\masked_2", masked_name), result_2)
    cv2.imwrite(os.path.join("D:\projegteg\Color_detection\masked_3", masked_name), result_3)
    cv2.imwrite(os.path.join("D:\projegteg\Color_detection\masked_4", masked_name), result_4)
    cv2.imwrite(os.path.join("D:\projegteg\Color_detection\masked_5", masked_name), result_5)

    cv2.imwrite(os.path.join("D:\projegteg\Color_detection\images_color", name), frame)
    return name

def save_datas(colors, black_pxl, name):
    data = [colors[0], colors[1], colors[2], black_pxl, name]
    with open("datas.csv", "a+", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def take_image():
    result_1, image, result_2, result_3, result_4, result_5 = read_analyze_img(img)
    colors, black_pxl = color_sort(result_1)
    avg_color = np.average(colors, axis=0)
    color_averages = np.array(avg_color, dtype=np.uint8)
    color_averages_list = color_averages.tolist()
    save_datas(color_averages_list, black_pxl, save_image(image, result_1, result_2, result_3, result_4, result_5))

#TODO tartományok színeinek száma
#TODO Tartományok adatait kiírni a képek alá
#TODO elérhető kamerák közül kiválasztani hogy melyik kamera képét használja
#TODO kiválasztani hogy fájlból olvasson be vagy kamera képét jelenítse meg
#TODO OpenCV filterelési lehetőségeknek utánna nézni UwU
#TODO help button, kezelői felület dizájnolása