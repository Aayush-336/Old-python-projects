import pyautogui
from PIL import Image, ImageGrab
import time
import keyboard


def collide(data):
    for j in range(550, 650):  # These values can be different for other PC
        for i in range(755, 760):  # These values can be different for other PC
            if data[i, j] < 50:  # Check if data[i,j] means a set of pixels array
                # on screen is BLACK or not
                pyautogui.click(i, j)
                return
        for i in range(855, 860):  # These values can be different for other PC
            if data[i, j] < 50:
                pyautogui.click(i, j)
                return
        for i in range(1055, 1060):  # These values can be different for other PC
            if data[i, j] < 50:
                pyautogui.click(i, j)
                return
        for i in range(1155, 1160):  # These values can be different for other PC
            if data[i, j] < 50:
                pyautogui.click(i, j)
                return


time.sleep(3)

while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    collide(data)

    if keyboard.is_pressed('q'):
        break
    # image.show()
    # break
