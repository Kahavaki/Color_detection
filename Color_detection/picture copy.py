from datetime import datetime
import numpy as np
import cv2
import os
import csv
cap = cv2.VideoCapture(0)

def read_analyze_img(cap):
    ret, frame = cap.read()
    
    # convert the frame colors to HSV colors
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # white and the shades of yellow
    lower = np.array([20,0,168])
    upper = np.array([172,111,255])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result, frame

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

def save_image(frame):
    now = datetime.now()
    directory = "D:\projegteg\Color_detection\datas"
    name = "{}.png".format(f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}-{now.microsecond}")
    cv2.imwrite(os.path.join(directory, name), frame)

def take_image():
    masked, frame = read_analyze_img(cap)
    colors, black_pxl = color_sort(masked)
    avg_color = np.average(colors, axis=0)
    color_averages = np.array(avg_color, dtype=np.uint8)
    save_image(frame)


"""
while True:
    if not paused:
        paused = True
        

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)

    if key == 32:
        paused = False
    elif key == 27:
        break


szöveggé alakítani a számot
elmenteni a képet dátum és idővel
kiírni a képernyőre az átlag színt, megjelenítve, tömb elemeit listába átrakni
help button, kezelői felület dizájnolása

"""