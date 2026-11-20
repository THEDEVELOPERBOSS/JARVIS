import cv2
import numpy as np

def analyze_image(frame):
    size = frame.shape
    data_type = frame.dtype
    color = frame.shape[2] if frame.ndim == 3 else 1
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts to grayscale
    brightness = np.mean(gray_frame)
    
    return size, data_type, color, brightness
    