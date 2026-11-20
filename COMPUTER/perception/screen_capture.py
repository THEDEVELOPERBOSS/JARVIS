import cv2
import numpy as np 
import mss 


def get_monitors():
    with mss.mss() as sct:
        _monitors = sct.monitors[1:]
        return _monitors

def capture_screen(monitor_index=0):
    with mss.mss() as sct:
        # select the monitor that you want to take a screenshot of
        selected_monitor = sct.monitors[monitor_index + 1]
        # take the screenshot
        screenshot = sct.grab(selected_monitor)
        # convert screenshot into a NumPy array
        frame = np.array(screenshot)
        # converst it into BGR from BGRA
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        return frame

