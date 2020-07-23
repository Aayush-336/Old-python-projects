import pyautogui
import win32api, win32con
import keyboard


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# time.sleep(3)
# pyautogui.displayMousePosition()
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(750, 700)[0] == 0:
        pyautogui.click(750, 700)
    if pyautogui.pixel(900, 700)[0] == 0:
        pyautogui.click(900, 700)
    if pyautogui.pixel(1025, 700)[0] == 0:
        pyautogui.click(1025, 700)
    if pyautogui.pixel(1170, 700)[0] == 0:
        pyautogui.click(1170, 700)
