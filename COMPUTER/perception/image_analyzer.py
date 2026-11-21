import cv2
import numpy as np

def analyze_image(frame):
    size = frame.shape
    data_type = frame.dtype
    color = frame.shape[2] if frame.ndim == 3 else 1
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts to grayscale
    brightness = np.mean(gray_frame)
    
    if brightness <= 85:
        lighting = "Dark"
    elif brightness <= 170:
        lighting = "Normal"
    else:
        lighting = "Bright"
        
    blue_channel = np.mean(frame[:, :, 0])
    green_channel = np.mean(frame[:, :, 1])
    red_channel = np.mean(frame[:, :, 2])
    dominant_intensity = max(blue_channel, green_channel, red_channel)
    dominant_color = []
    if blue_channel >= green_channel and blue_channel >= red_channel:
        dominant_color.append("Blue")
    if red_channel >= green_channel and red_channel >= blue_channel:
        dominant_color.append("Red")
    if green_channel >= blue_channel and green_channel >= red_channel:
        dominant_color.append("Green")
    
    return size, data_type, color, brightness, lighting, blue_channel, green_channel, red_channel, dominant_intensity, dominant_color
    