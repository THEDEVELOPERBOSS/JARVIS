import pyautogui
import time

while True:
    time.sleep(5)
    image_1 = pyautogui.locateOnScreen("chrome.png")
    image_2 = pyautogui.locateOnScreen("chrome_w_profile.png") # get the updated image
    pyautogui.click(image_1 | image_2)
    