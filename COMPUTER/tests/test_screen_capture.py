import cv2

from COMPUTER.perception.screen_capture import get_monitors, capture_screen

if __name__ == "__main__":
    frame = capture_screen()

    print("Image dimensions:", frame.shape)
    print("Image data type:", frame.dtype)

    cv2.imshow("JARVIS Screen Capture", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def test_get_monitors():
    monitors = get_monitors()
    assert isinstance(monitors, list)
    assert len(monitors) > 0 