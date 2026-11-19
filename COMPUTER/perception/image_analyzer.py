def analyze_image(frame):
    size = frame.shape
    data_type = frame.dtype
    color = frame.shape[2] if frame.ndim == 3 else 1
    return size, data_type, color 
    