from time import sleep
import win32gui, win32con
from PIL import ImageGrab


def screenshot():
    return ImageGrab.grab(bbox=(0,150,1980,980))


inp = "take"
while 1:
    inp = input()
    if inp != "take" :
        break
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_HIDE)

    sleep(1)
    scr = screenshot()

    # scr.show()
    print("ScreenShot taken.")
    win32gui.ShowWindow(Minimize, win32con.SW_NORMAL)

    # scr.show()
    name = input("Enter File Name:")
    if name == "exit":
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        continue
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    save_path = "D:\Screenshot files\ "
    scr.save(save_path + name + ".jpg", 'JPEG')

