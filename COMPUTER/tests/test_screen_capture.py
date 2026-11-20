import cv2

from ..perception.screen_capture import get_monitors, capture_screen
from ..perception.image_analyzer import analyze_image

if __name__ == "__main__":
    frame = capture_screen() # takes a screenshot 
    t_size, t_data_type, t_color = analyze_image(frame)

    print(f"Size: {t_size}, Data Type: {t_data_type}, Color: {t_color}")
    
def test_get_monitors():
    monitors = get_monitors()
    assert isinstance(monitors, list)
    assert len(monitors) > 0 