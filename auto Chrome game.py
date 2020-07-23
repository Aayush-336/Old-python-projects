import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
import time


# THIS WILL WORK FOR GOOGLE DARK MODE

def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    for i in range(755, 765):  # These values can be different for other PC's
        for j in range(270, 320):
            if data[i, j] > 100:  # Check if data[i,j] means a set of pixels array on screen is white or not
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # image.show()
        # break
